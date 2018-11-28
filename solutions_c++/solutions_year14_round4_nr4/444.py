#include <iostream>
#include <iomanip>
#include <cstdio>
#include <math.h>
#include <algorithm>
#include <queue>
#include <string>
#include <fstream>
#include <vector>
#include <stack>
#include <map>
#include <set>
#include <ctime>
#include <iomanip>

#define all(x) (x).begin(), (x).end()
#define pb push_back
#define mp make_pair
#define double long double
#define LL long long
#define itn int

using namespace std;

int main(){

	int T;
	cin >> T;
	for (int _ = 0; _ < T; _++){
		cout << "Case #" << _ + 1 << ": ";
		cerr << _ << "\n";
		int n, m;
		cin >> m >> n;
		vector<string> s(m);
		for (int i = 0; i < m; i++) cin >> s[i];
		int k = 1;
		for (int i = 0; i < m; i++) k *= n;
		int M = 0;
		int cnt = 0;
		for (int i = 0; i < k; i++){
			int j = i;
			vector<int> c(m);
			for (int ij = 0; ij < m; ij++){
				c[ij] = j % n;
				j /= n;
			}
			int mm = 0;
			set<string> st;
			for (int ij = 0; ij < n; ij++){
				for (int j = 0; j < m; j++){
					if (c[j] == ij){
						for (int ii = 0; ii <= s[j].length(); ii++){
							st.insert(s[j].substr(0, ii));
						}
					}
				}
				mm += st.size();
				st.erase(st.begin(), st.end());
				if (mm == M) cnt++; else 
				if (mm > M){
					M = mm;
					cnt = 1;
				}
			}
		}
		cout << M << " " << cnt << "\n";
	}

	return 0;
	
}