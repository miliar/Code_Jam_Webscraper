#include <iostream>
#include <fstream>
#include <string>
#include <cstdio>
using namespace std;

int Smax;
string s;
int main(){
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int T;
	cin >> T;
	for (int tc = 1; tc <= T; tc++){
		cin >> Smax;
		cin >> s;

		int stood = 0;
		int ans = 0;
		for (int i = 0; i < s.length(); i++){
			int x = s[i] - '0';
			if (stood < i && x>0){
				int add = i - stood;
				stood += add;
				ans += add;
				stood += x;
			}
			else{
				stood += x;
			}
		}

		printf("Case #%d: %d\n", tc, ans);
	}
	fclose(stdin);
	fclose(stdout);
}
	
