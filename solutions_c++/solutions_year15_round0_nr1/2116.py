#include<iostream>
#include<string>
#include<fstream>
//#include <cstdio>
using namespace std;

int main(){
	int t;
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	cin >> t;
	for(int i = 0 ;i < t; i++){
		int smax;
		cin >> smax;
		string s;
		cin >> s;
		int r = 0, ans = 0;
		for(int j = 0; j <= smax; j++){
			int k = s[j] - '0';
			if(k == 0)
				continue;
			if(r >= j)
				r += k;
			else{
				ans += (j - r);
				r += (j - r);
				r += k;
			}
		}
		cout << "Case #" << i + 1 << ": " << ans << endl;
	}
	return 0;
}