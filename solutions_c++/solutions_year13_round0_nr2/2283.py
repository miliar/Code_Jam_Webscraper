#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <algorithm>
#include <map>
#include <cmath>
#include <queue>
#include <stack>

using namespace std;

#define FOR(i, A, B) for(int i=(A); i<(B); i++)
#define REP(i, N) for(int i=0; i<(N); i++)
#define SZ(v) ((int)(v).size())
#define ALL(v) (v).begin(), (v).end()
#define SORT(v) sort(ALL(v))
#define MP make_pair
#define PB push_back
#define VI vector<int>
#define VS vector<string>
#define PII pair<int, int>
#define X first
#define Y second

int aabs(int a) { return (a<0)?-a:a; }
int mmax(int a, int b) { return (a>b)?a:b; }
int mmin(int a, int b) { return (a<b)?a:b; }

int main(void)
{
	int T, N, M;
	int lawn[110][110];
	int maxr[110], maxc[110];

	cin >> T;
	for(int caso=0; caso < T; caso++) {
		cin >> N >> M;
		for(int i=0; i<N; i++) {
			maxr[i] = 0;
			for(int j=0; j<M; j++) {
				cin >> lawn[i][j];
				maxr[i] = mmax(maxr[i], lawn[i][j]);
			}
		}

		for(int i=0; i<M; i++) {
			maxc[i] = 0;
			for(int j=0; j<N; j++) {
				maxc[i] = mmax(maxc[i], lawn[j][i]);
			}
		}

		int ans=1;
		for(int i=0; ans and i<N; i++) {
			for(int j=0; ans and j<M; j++) {
				if(lawn[i][j] < maxr[i] and lawn[i][j] < maxc[j]) {
					ans=0;
					break;
				}
			}
		}

		if(ans) cout << "Case #" << caso+1 << ": YES\n";
		else cout << "Case #" << caso+1 << ": NO\n";

	}		
}