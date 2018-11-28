#include <stdio.h>
#include <iostream>
#include <string>
using namespace std;
typedef long long LL;
void main(){
	
	freopen("last.in", "r", stdin);
    freopen("last.out", "w", stdout);
    ios_base::sync_with_stdio(0); cin.tie(0);
    int T; cin >> T;
	string s;
	char *s2;
	for (int t = 1; t <= T; t++){
		cin >> s;
		s2 = new char[3000]();
		char f = s[0];
		s2[1000]=f;
		int f1=1000;
		for (int i = 1; i < s.size(); i++){
			if(s2[f1] > s[i]){
				s2[f1+i] = s[i];
			}
			else {
				f1--;
				s2[f1] = s[i];
			}
		}

		cout << "Case #" << t << ": ";
		for(int i =0; i < 3000; i++){
			if (s2[i]==0) continue;
			cout << s2[i];
		}
		cout << endl;
	}
}