#include <iostream>
#include <cstdio>
#include <ctime>
#include <cassert>
#include <cmath>
#include <stack>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <algorithm>
#include <utility>
#include <cstdlib>
#include <cstring>
#include <string>
using namespace std;

#ifdef WIN32
	#define lld "%I64d"
#else
	#define lld "%lld"
#endif

#define mp make_pair
#define pb push_back
#define put(x) { cout << #x << " = "; cout << (x) << endl; }

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
typedef double db;

const int M = 3 * 1e6;
const ll Q = 1e9 + 7;



int a[200][200];
int dx[5] = {0, -1, 0, 1, 0};
int dy[5] = {0, 0, 1, 0, -1};

int main(){
	srand(time(NULL));
	freopen("input.txt", "r", stdin);
	freopen("output1.txt", "w", stdout);

	int t;
	cin >> t;
	for (int tq = 0; tq < t; tq++){
		int n, m;
		cin >> n >> m;
		int ans = 0;
		for (int i = 0; i < n; i++){
			char s[200];
			scanf("%s", s);
			for (int j = 0; j < m; j++){
				if (s[j] == '.')
					a[i][j] = 0;
				if (s[j] == '^')
					a[i][j] = 1;
				if (s[j] == '>')
					a[i][j] = 2;
				if (s[j] == 'v')
					a[i][j] = 3;
				if (s[j] == '<')
					a[i][j] = 4;
			}
		}
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++){
				if (a[i][j]){
					int typ = a[i][j];
					int curx = i + dx[typ], cury = j + dy[typ];
					bool ok = false;
					while (1){
						if (0 > curx || curx >= n || 0 > cury || cury >= m)
							break;
						if (a[curx][cury])
							ok = true;
						curx += dx[typ];
						cury += dy[typ]; 
					}
					if (ok)
						continue;
					for (int tt = 1; tt <= 4; tt++){
						curx = i + dx[tt], cury = j + dy[tt];
						while (1){
							if (0 > curx || curx >= n || 0 > cury || cury >= m)
								break;
							if (a[curx][cury])
								ok = true;
							curx += dx[tt];
							cury += dy[tt]; 
						}
						
					}
					if (!ok)
						ans = -1;
					else{
						if (ans != -1)
							ans++;
					}	
				}
			}
		cout << "Case #" << tq + 1 << ": ";	
		if (ans == -1)
			cout << "IMPOSSIBLE\n";
		else
			cout << ans << endl;	
		cerr << tq + 1 << endl;	
	}

	return 0;
}	