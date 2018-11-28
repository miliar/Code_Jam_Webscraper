#include<algorithm>
#include<cassert>
#include<cctype>
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<deque>
#include<iostream>
#include<list>
#include<map>
#include<queue>
#include<set>
#include<string>
#include<vector>
using namespace std;

typedef long long LL;
typedef long double LD;

#define dprintf(...) fprintf(stderr, __VA_ARGS__)

int cond = 1;
#define DB(X) {if(cond){cerr<<"Line:"<<__LINE__<<", "<<#X<<" = "<<X<<endl;}}
const static int NMAX = 103;
int main() {
	int t; cin >> t;
	string res[2] = {"YES\n", "NO\n"};
	int a[NMAX][NMAX], max_in_row[NMAX], max_in_col[NMAX];
	for(int q = 1; q <= t; ++q){
		int N, M; cin >> N >> M;
		for(int i = 0; i< N; ++i)
			for(int j = 0; j < M; ++j)
				cin >> a[i][j];
		for(int i = 0; i < N; i++) {
			int act_max = 0;
			for(int j = 0; j < M; j++) {
				if (a[i][j] > act_max) act_max = a[i][j];
			}
			max_in_row[i] = act_max;
		}
		for(int i = 0; i < M; i++) {
			int act_max = 0;
			for(int j = 0; j < N; j++) {
				if (a[j][i] > act_max) act_max = a[j][i];
			}
			max_in_col[i] = act_max;
		}
		/*
		for(int i = 0; i < M; i++) cout <<  max_in_col[i] << " ";
		for(int i = 0; i < N; i++) cout << endl << max_in_row[i] ;
		*/
		int r = 0;
		for(int i = 0; i< N; ++i)
			for(int j = 0; j < M; ++j)
				if (a[i][j] != min(max_in_row[i], max_in_col[j])) {
					r = 1;
					break;
				}
		cout << "Case #" << q << ": " << res[r];
	}
	return 0;
}
