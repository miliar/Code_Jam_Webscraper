#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<string>
#include<vector>
#include<iostream>
#include<fstream>
#define REP(i, N) for(int i = 0; i<(N); i++)

using namespace std;


int N;


int main() {

	freopen("B-small-attempt0.in", "r", stdin);
	ofstream cout("out.out");
	int C = 0;
	cin >> C;


	//cout << (int)'a' << endl; 97
	for (int cases = 1; cases <= C; cases++){
		string str = "";
		cin >> str;
		while (str.size() > 0 && str.back() == '+')str.pop_back();
		if (str.size() == 0) {
			cout << "Case #" << cases << ": " << 0 << endl;
			continue;
		} else {
			int ans = 0;
			for (int i = 0; i < str.size() - 1; i++) {
				if (str[i] != str[i + 1])ans++;
			}
			cout << "Case #" << cases << ": " << ans+1 << endl;
		}
		
	}
	return 0;
}