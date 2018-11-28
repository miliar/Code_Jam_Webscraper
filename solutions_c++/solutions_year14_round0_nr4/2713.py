#include <iostream>
#include <fstream>
#include <cstdlib>
#include <vector>
#include <iomanip>
#include <cstdio>
#include <algorithm>
#include <memory.h>
#include <sstream>
#include <string>

using namespace std;

bool vst[1001];

int fun(string s){
	s.resize(5 , '0');
	stringstream ss(s);
	int n;
	ss >> n;
	return n;
}

int main() {
	freopen("D-large.in", "r", stdin);
	freopen("output.in", "w", stdout);
	int T;
	cin >> T;
	int k = 1;
	while (T--) {
		int n;
		cin >> n;
		vector<int> Naomi(n);
		vector<int> Ken(n);
		int a , b;
		string s;
		for (int i = 0; i < n; ++i) {
			scanf("%d.", &b);
			cin >> s;
			a = fun(s);
			Naomi[i] = a;
		}
		for (int i = 0; i < n; ++i) {
			scanf("%d.", &b);
			cin >> s;
			a = fun(s);
			Ken[i] = a;
		}

		sort(Naomi.begin() , Naomi.end());
		sort(Ken.begin() , Ken.end());

		int warScore = 0 , beg = 0;
		memset(vst , 0 , sizeof vst);
		for(int i = 0 ; i < n ; ++i){
			bool find = 0;
			for(int j = 0 ; j < n ; ++j){
				if(vst[j])continue;
				if(Ken[j] > Naomi[i]){
					find = 1;
					vst[j] = 1;
					break;
				}
			}
			if(!find){
				for(int j = 0 ; j < n ; ++j){
					if(!vst[j]){
						vst[j] = 1;
						break;
					}
				}
				warScore++;
			}
		}
		beg = 0;
		int endN = n - 1 , endK = n - 1 , dWarScore = 0;
		while(beg <= endN){
			while(endN >= 0 && endK >= 0 && Naomi[endN] > Ken[endK]){
				endN--;
				endK--;
				dWarScore++;
			}
			beg++;
			endK--;
		}
		cout << "Case #" << k << ": " << dWarScore << ' ' << warScore << endl;
		k++;
	}
	return 0;
}
