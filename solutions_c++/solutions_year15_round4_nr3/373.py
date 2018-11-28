#include <stdio.h>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <iostream>

#define N 10010

using namespace std;

int tip[4000], perm[4000];
char s[100000], line[100000];

int main (void) {
	int t, c, i, j, n;
	ios::sync_with_stdio(false);
	cin.getline(line, N);
	sscanf (line,"%d", &t);
	for (c = 1; c <= t; c++) {
		vector<int> v[20];
		map<string, int> m;
		cin.getline(line, N);
		sscanf (line,"%d", &n);
		int sz = 0;
		for (i = 0; i < n; i++) {
			cin.getline(line, N);
			int pos = 0, k;
			int len = strlen(line);
			while (pos < len) {
				sscanf (line+pos, "%s%n", s, &k);
				string st(s);
				if (!m.count(st))	m[st] = sz++;
				v[i].push_back(m[st]);
				pos += k;
			}
		}
		// for (map<string, int>::iterator it = m.begin(); it != m.end(); it++) {
		// 	cout << it->first << " " << it->second << endl;
		// }
		int ans = 0;
		if (n == 2) {
			set<int> ss;
			for (i = 0; i < v[0].size(); i++) {
				ss.insert(v[0][i]);
			}
			for (i = 0; i < v[1].size(); i++) {
				if (ss.find(v[1][i]) != ss.end())	ans++;	
			}
		} else {
			memset(perm, -1, sizeof perm);
			int pp = 0;
			for (i = 0; i < v[0].size(); i++)	perm[v[0][i]] = 0; //en
			for (i = 0; i < v[1].size(); i++) { //fr
				if (perm[v[1][i]] == 0) {
					pp++;
					perm[v[1][i]] = 2;
				} else if (perm[v[1][i]] == -1)
					perm[v[1][i]] = 1;
			}
			int mx = 1<<(n-2);
			ans = 1000000000;
			for (int mask = 0; mask < mx; mask++) {
				memset(tip, -1, sizeof tip);
				int curr = pp;
				for (i = 0; i < n-2; i++) {
					int ii = i+2;
					if ((mask>>i)&1) { //fr
						for (j = 0; j < v[ii].size(); j++) {
							int w = v[ii][j];
							if (perm[w] == 2 || tip[w] == 2)	continue;
							if (tip[w] == -1) {
								tip[w] = 1;
							}
							if (tip[w] == 0 || perm[w] == 0) {
								tip[w] = 2;
								curr++;
							}
						}
					} else { //en
						for (j = 0; j < v[ii].size(); j++) {
							int w = v[ii][j];
							//printf ("%d w %d %d %d\n",mask, w, tip[w], perm[w]);
							if (perm[w] == 2 || tip[w] == 2)	continue;
							if (tip[w] == -1) {
								tip[w] = 0;
							}
							if (tip[w] == 1 || perm[w] == 1) {
								tip[w] = 2;
								curr++;
							}
						}
					}
				}
				//printf ("%d %d\n", mask, curr);
				ans = min(ans, curr);
			}
		}
		cout << "Case #"<< c << ": "<< ans << "\n";
	}
}