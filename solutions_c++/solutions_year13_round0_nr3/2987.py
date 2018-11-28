#include <iostream>
#include <string>
#include <cmath>

using namespace std;

bool isPalindrome(int i){
	string word = std::to_string(i);
	int length = word.size();
	
	if (length>0){
		for(int i=0;i<(length);i++)
		{
			if(word[i] != word[length-1-i])
				return false;
		}
	}
	return true;
}


int main(){
	int k;
	cin >> k;
	for(int c = 0; c < k; ++c){
		int lower, upper;
		cin >> lower >> upper;
		
		int count= 0;
		double d_sqrt = sqrt( lower );
		int i_sqrt = d_sqrt;
		if ( d_sqrt == i_sqrt ){
			if(isPalindrome(lower) && isPalindrome(i_sqrt))
				++count;
		
		}
		
		for(int i = i_sqrt+1; i*i <= upper; ++i){
			if(!isPalindrome(i))
				continue;
			if(!isPalindrome(i*i))
				continue;
			++count;	
		}
		
		cout << "Case #" << c+1 << ": " << count << endl;
	}
}
	//




