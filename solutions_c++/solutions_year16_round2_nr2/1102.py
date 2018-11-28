//---------------------------------------------------------------------
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>

#include <vector>
#include <set>
#include <map>
#include <deque>
#include <string>
#include <bitset>

#include <algorithm>
#include <cmath>
#include <ctime>

using namespace std;

int const MAX_CH = 1010;
long long const LL_INF = 4000000000000000000LL;

char st[MAX_CH],a[MAX_CH],b[MAX_CH];
long long dp[MAX_CH][2];
long long DG_10[MAX_CH];
int from_sgn[MAX_CH][2],from_d1[MAX_CH][2],from_d2[MAX_CH][2];

int t;

int is_match(int a, char ch) {
	if (ch == '?')
		return 1;
	return a == ch-'0';
}

string form_it(long long aa, int n) {
	long long QQ = aa;

	char ms[40];

	for (int i=0; i<40; i++) ms[i] = '0';
	int ms_len = 0;

	while (QQ) {
		ms[ms_len++] = (QQ%10) + '0';
		QQ /= 10;
	}

	string ans = "";
	for (int d=0; d<n-ms_len; d++)
		ans += (char) '0';

	for (int ee=ms_len-1; ee>=0; ee--)
		ans += ms[ee];

	return ans;
}

void rec_ans(int i, int j, long long &CC, long long &DD) {
	CC = 0;
	DD = 0;

	int len = 0;

	while (i > 0) {
		int d1 = from_d1[i][j];
		int d2 = from_d2[i][j];
		
		int new_j = from_sgn[i][j];
		int new_i = i-1;

		CC += d1 * DG_10[len];
		DD += d2 * DG_10[len];

		len++;

		i = new_i;
		j = new_j;
	}
}


int cnt_dig(int x) {
	int cnt = 0;
	if (x == 0) cnt++;

	while (x) {
		cnt++;
		x/=10;
	}
	return cnt;
}

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	DG_10[0] = 1;
	for (int i=1; i<=18; i++)
		DG_10[i] = DG_10[i-1] * 10LL;

	gets(st);
	sscanf(st,"%d",&t);
	for (int q=0; q<t; q++) {
		gets(st);
		printf("Case #%d: ",q+1);

		sscanf(st,"%s %s",a,b);

		int n = (int) strlen(a);

		//
		cerr<<"\r"<<q<<"            ";
		int ans_a = -1, ans_b = -1;
		int mn  =1000000;
		char a_st_st[200],b_st_st[200];
		for (int j=0; j<n; j++) a_st_st[j] = a[j];
		for (int j=0; j<n; j++) b_st_st[j] = b[j];

		for (int a=0; a<=999; a++)
			if (cnt_dig(a) <= n) {
			for (int b=0; b<=999; b++)
				if (cnt_dig(b) <= n) {
					string a_st = form_it(a,n);
					string b_st = form_it(b,n);

					int Ok = 1;
					for (int j=0; j<n; j++) {
						if (!is_match(a_st[j]-'0',a_st_st[j])) Ok= 0;
						if (!is_match(b_st[j]-'0',b_st_st[j])) Ok= 0;
					}

					if (Ok) {
						int df = a-b;
						if (df < 0) df = -df;

						if (df < mn) {
							mn = df;
							ans_a =a;
							ans_b = b;
						}
					}
				}
			}
			else break;

			cout<<form_it(ans_a,n) <<" "<<form_it(ans_b,n)<<"\n";
			continue;
		//
		
		for (int i=0; i<=n; i++)
			dp[i][0] = dp[i][1] = LL_INF;

		dp[0][0][0] = dp[0][1][0] = 0;
		dp_len[0][0] = dp_len[0][1] = 1;

		for (int i=0; i<=n; i++)
			for (int sgn=0; sgn<2; sgn++) {
				from_sgn[i][sgn] = -1;
				from_d1[i][sgn] = -1;
				from_d2[i][sgn] = -1;
			}

		for (int j=1; j<=n; j++)
			for (int old_sgn = 0; old_sgn < 2; old_sgn++)
				if (dp[j-1][old_sgn] < LL_INF)
					for (int d1=0; d1<10; d1++)
						if (is_match(d1,a[j-1]))
							for (int d2=0; d2<10; d2++)
								if (is_match(d2,b[j-1])) {
									long long new_val = dp[j-1][old_sgn];
									if (old_sgn)
										new_val = -new_val;

									new_val += (d1-d2)*DG_10[n-j];

									if (new_val >= 0) {
										if (new_val < dp[j][0]) {
											dp[j][0] = new_val;
											from_sgn[j][0] = old_sgn;
											from_d1[j][0] = d1;
											from_d2[j][0] = d2;
										}
									}
									else {
										new_val = -new_val;

										if (new_val < dp[j][1]) {
											dp[j][1] = new_val;
											from_sgn[j][1] = old_sgn;
											from_d1[j][1] = d1;
											from_d2[j][1] = d2;
										}
									}
								}

		long long cc_1 = LL_INF,jj_1 = LL_INF,cc_2 = LL_INF ,jj_2 = LL_INF;

		if (dp[n][0] < LL_INF && dp[n][1] < LL_INF) {
			if (dp[n][0] < dp[n][1])
				rec_ans(n,0,cc_1,jj_1);
			else if (dp[n][0] > dp[n][1])
				rec_ans(n,1,cc_2,jj_2);
			else {
				rec_ans(n,0,cc_1,jj_1);
				rec_ans(n,1,cc_2,jj_2);
			}
		}
		else if (dp[n][0] < LL_INF)
			rec_ans(n,0,cc_1,jj_1);
		else if (dp[n][1] < LL_INF)
			rec_ans(n,1,cc_2,jj_2);

		int Ok = 0;
		if (cc_1 < cc_2 || (cc_1 == cc_2 && jj_1 < jj_2)) Ok = 1;

		if (!Ok) {
			swap(cc_1,cc_2);
			swap(jj_1,jj_2);
		}

		cout<<form_it(cc_1,n)<<" "<<form_it(jj_1,n);
		printf("\n");
	}
	return 0;
}