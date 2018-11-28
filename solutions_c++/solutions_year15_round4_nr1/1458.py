#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>
#include <vector>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <numeric>
#include <ctime>
#include <fstream>
#include <iomanip>
#include <stdexcept>
#include <functional>
#include <math.h>
#include <utility>

#pragma comment(linker, "/STACK:133217728")

using namespace std;

int f(int a, int b, int n, int m) {
	if(a < 0 || b < 0 || a == n || b == m) return 0;
	return 1;
}
int main() {  
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	cin >> T;
	string x[100];
	int cnt1[111], cnt2[111];
	vector <char> rr[111], cc[111];
	for(int t=1; t <= T; t++) {
		cout << "Case #" << t << ": ";
		int n, m;
		cin >> n >> m;
		for(int i=0; i<n; i++)
			cin >> x[i];

		if(n == 1 && m == 1) {
			if(x[0][0] == '.')
				cout << 0 << endl;
			else
				cout << "IMPOSSIBLE" << endl;
			continue;
		}

		
		for(int i=0; i<=100; i++) 
		{
			cnt1[i] = cnt2[i] = 0;
			rr[i].clear();
			cc[i].clear();
		}

		for(int i=0; i<n; i++)
			for(int j=0; j<m; j++) 
				if(x[i][j] != '.')
				{
					if(x[i][j] == '>' || x[i][j] == '<') 
						rr[i].push_back(x[i][j]); 
					else
						cc[j].push_back(x[i][j]);
					cnt1[i]++;
					cnt2[j]++;
				}

		int ans = 0;
		bool ok = 1;
		for(int i=0; i<n; i++)
			for(int j=0; j<m; j++) 
			{
				if(x[i][j] == '.') continue;
				
				if(cnt1[i] == 1 && cnt2[j] == 1) ok = 0;
			}

		for(int i=0; i<n; i++)
			for(int j=0; j<m; j++) 
			{
				if(x[i][j] == '.') continue;
				bool was = 0;
				int di = 0, dj = 0;

				if(x[i][j] == '>') dj = 1;
				if(x[i][j] == '<') dj = -1;
				if(x[i][j] == 'v') di = 1;
				if(x[i][j] == '^') di = -1;

				int a = i + di, b = j + dj;
				while(f(a, b, n, m)) {
					if(x[a][b] != '.') was = 1;
					if(was) break;
					a += di;
					b += dj;
				}

				if(!was) { ans++; }
			}
		if(!ok) cout << "IMPOSSIBLE" << endl; else
		cout << ans << endl;
	}
 	return 0;
}

