#pragma comment(linker, "/STACK:108777264")
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cmath>
#include <vector>
#include <deque>
#include <map>
#include <set>
#include <bitset>
#include <utility>
#include <algorithm>
using namespace std;

int const MAX_N = 1024;
int const MAX_CH = 100100;

char st[MAX_CH];
int N, s[64][64], revs[64][64], new_s[64][64];

int GD = 0;
int p[64],car[64];

void rec(int from) {
	if (!GD) return;

	if (from >= N) {
		for (int j=0; j<N; j++)
			if (!car[j]) GD = 0;
		return;
	}

	int can_move = 0;

	for (int j=0; j<N; j++)
		if (!car[j] && new_s[p[from]][j]) {
			can_move = 1;

			car[j] = 1;
			rec(from+1);

			if (!GD)
				return;

			car[j] = 0;
		}

	if (!can_move)
		GD = 0;
}

void check() {
	for (int j=0; j<N; j++) car[j] = 0;
	rec(0);
}

int all_good() {
	GD = 1;
	for (int i=0; i<N; i++) p[i] = i;
	check();
	while (next_permutation(p,p+N)) check();
	return GD;
}

void solve_slow() {
	for (int i=0; i<N; i++)
		for (int j=0; j<N; j++)
			revs[i][j] = 1-s[i][j];

	int g = 0;
	for (int i=N-1; i>=0; i--)
		for (int j=N-1; j>=0; j--)
			g = g*2 + revs[i][j];

	int mn_pay = MAX_CH;

	for (int msk=g; ; msk=(msk-1)&g) {
		int cnt_pay = 0;
		int XX = msk;
		while (XX) {
			cnt_pay += XX&1;
			XX>>=1;
		}

		if (cnt_pay >= mn_pay && msk!=0) continue;

		int num = 0;
		for (int i=0; i<N; i++)
			for (int j=0; j<N; j++) {
				new_s[i][j] = s[i][j];
				if ((msk>>num)&1)
					new_s[i][j] = 1;
				num++;
			}
		
		if (all_good())
			if (cnt_pay < mn_pay)
				mn_pay =min(mn_pay, cnt_pay);

		if (msk==0)  break;
	}

	cout<<" "<<mn_pay;
}

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	gets(st);
	int tst_count;
	sscanf(st,"%d",&tst_count);
	for (int qqq=1; qqq<=tst_count; qqq++) {
		cerr<<"\r"<<qqq<<"     ";
		printf("Case #%d:",qqq);

		//
		gets(st);
		sscanf(st,"%d",&N);
		for (int i=0; i<N; i++) {
			gets(st);
			for (int j=0; j<N; j++) s[i][j] = st[j]-'0';
		}

		solve_slow();
		//

		printf("\n");
	}
	return 0;
}