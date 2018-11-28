#include <stdio.h>
#include <iostream>
#include <string>
using namespace std;
typedef long long LL;
void main(){
	
	freopen("pancakeflip.in", "r", stdin);
    freopen("pancakeflip.out", "w", stdout);
    ios_base::sync_with_stdio(0); cin.tie(0);
    int T; cin >> T;
	string s;
	int c;
	for (int t = 1; t <= T; t++){
		cin >> s;
		int f=0;
		int l = s.size()-1;
		for (int i=l; i>=0; i--){
			if (s[i] == '+'){
				l--;
				continue;
			}
			else{
				for (int j =0; j < l; j++){
					s[j]=88-s[j];
					//l--;
				}
			}

			f++;
		}
		cout << "Case #" << t << ": ";
		cout << f << endl;
	}
}