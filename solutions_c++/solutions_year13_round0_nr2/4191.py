#include <cstdio>
#include <algorithm>
#include <fstream>
#include <iostream>
#include <vector>
#include <queue>
#include <map>
#include <cstring>
#include <string>


#define pb push_back
#define mp make_pair
#define f first
#define s second
#define ll long long

const int MAXN = 110;

using namespace std;

int N, M, T;
int A[MAXN][MAXN], line[MAXN], col[MAXN];

void clear() {

	for (int i = 1; i < MAXN; ++i)
		line[i] = col[i] = 0;

}
int main() {
	ifstream cin("test.in");
	ofstream cout("test.out");
	
	cin >> T;
	
	
	for (int test = 1; test <= T; ++test) {
		cin >> N >> M;
			
		for (int i = 1; i <= N; ++i) {
			for (int j = 1; j <= M; ++j)
				cin >> A[i][j];
		}
		
		clear();
		
		for (int i = 1; i <= N; ++i)
			for (int j = 1; j <= M; ++j)
				line[i] = max(line[i] , A[i][j]);
		
		for (int j = 1; j <= M; ++j)
			for (int i = 1; i <= N; ++i)
				col[j] = max(col[j], A[i][j]);

		string ans = "YES";
		for (int i = 1; i <= N; ++i)
			for (int j = 1; j <= M; ++j)
				if(line[i] != A[i][j] && col[j] != A[i][j])
					ans = "NO";
		cout << "Case #" << test << ": " << ans << "\n";
	}

	return 0;
}
