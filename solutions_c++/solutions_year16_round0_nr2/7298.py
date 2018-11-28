#include <iostream>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <vector>

using namespace std;

//#define SMALL
#define LARGE

int main(){

	#ifdef SMALL
	freopen("B-small-attempt0.in","rt",stdin);
	freopen("B-small-attempt0.out","wt",stdout);
	#endif
	#ifdef LARGE
		freopen("B-large.in","rt",stdin);
		freopen("B-large.out","wt",stdout);
	#endif
	int t, i, j, n;
	string s;
	int count;

	cin>> t;

	for(i = 1; i<=t; i++){
		count = 0;
		cin>> s;
		int l = s.length();

		while(1){
			for(j =0; j<s.length(); j++){
				if(s[j] != '+') break;
			}
			if(j == s.length()) break;

			count++;
			for(j = l -1; j>=0; j--){
				if(s[j] == '+'){
					l--;
				}
				else break;
			}
			for(j = 0; j<l; j++){
				if(s[j] == '+'){
					s[j] = '-';
				}
				else s[j] = '+';
			}
		}
		cout << "Case #"<< i<<": "<<count << endl;
	}

	return 0;
}
