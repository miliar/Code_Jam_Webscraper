#define LOCAL
#define _CRT_SECURE_NO_WARNINGS
#include<cstdio>
#include<iostream>
#include <algorithm>
#include <string>
#include <cmath>
#include <map>
using namespace std;


int main(){
	std::ios_base::sync_with_stdio(false);

#ifdef LOCAL
	freopen("A-large.in", "r", stdin);
	freopen("result.in", "w", stdout);
#endif
	int res[10];
	int M;
	scanf("%d", &M);
	string input;
	getline(cin, input);
	for (int N = 1; N <= M; N++){
		getline(cin, input);
		map<char, int> m;
		for (int i = 0; i < input.length(); i++){
			if (m[input[i]] != 0) m[input[i]]++;
			else m[input[i]] = 1;
		}
		res[0] = m['Z'];
		res[2] = m['W'];
		res[4] = m['U'];
		res[1] = m['O'] - res[0] - res[2] - res[4];
		res[3] = m['R'] - res[0] - res[4];
		
		res[6] = m['X'];
		res[7] = m['S'] - res[6];
		res[5] = m['V'] - res[7];
		res[8] = m['T'] - res[2] - res[3];
		res[9] = m['I'] - res[5] - res[6] - res[8];
		cout << "Case #" << N << ": ";

		for (int i = 0; i < 10; i++){
			for (int j = 0; j < res[i]; j++){
				cout << i;
			}
		}
		cout << endl;
	}
	return 0;

}