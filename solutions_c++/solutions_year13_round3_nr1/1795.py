#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

string vowel="aeiou";

bool isconstonant(char c){
	for (int i = 0; i < 5; ++i)
	{
		if(c == vowel[i])
			return false;
	}
	return true;
}

int main(){
	int K;
	cin >> K;
	for (int k = 0; k < K; ++k)
	{
		string word;
		int n;
		cin >> word >> n;
		int count = 0;
		for(int s = 0; s <= word.length()-n; s++){
			int cln = 0;
			int maxclen = 0;
			for (int i = s; i < word.length(); i++){

				if(isconstonant(word[i])){
					cln++;
				} else {
					maxclen = max(cln, maxclen);
					cln = 0;
				}

				maxclen = max(cln, maxclen);

				if(maxclen >= n){
					count++;
				}
			}
		}
		cout << "Case #" << k+1 << ": " << count << endl;
	}
}