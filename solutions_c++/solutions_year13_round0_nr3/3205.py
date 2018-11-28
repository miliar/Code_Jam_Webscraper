#include<iostream>
#include<vector>
#include<string>
#include<math.h>
using std::sqrt;
using std::vector;
using std::cin;
using std::cout;
using std::endl;
using std::string;
bool isPalindrome(int k){
	vector<int> num;
	while(k != 0){
		num.push_back(k%10);
		k = k/10;
	}
	int size = num.size();
	int i=0;
	int j=size-1;
	while(j>=i){
		if(num[i] != num[j]){
			return false;
		}
		i++;
		j--;
	}
	return true;
}
int main(){
	int caseNo;
	int l, r;
	cin>>caseNo;
	for(int count = 0; count<caseNo; count++){
		cout<<"Case #"<<count+1<<": ";
		cin>>l>>r;
		int PalindromeNo=0;
		for(int i=(int)sqrt((float)l)-1; i*i <= r; i++){
			if((i*i >= l) && isPalindrome(i) && isPalindrome(i*i)){
				PalindromeNo++;
			}
		}
		cout<<PalindromeNo<<endl;
	}
	
	return 0;
}