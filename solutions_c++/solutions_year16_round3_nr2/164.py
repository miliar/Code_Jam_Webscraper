#pragma comment(linker, "/STACK:108777216")
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cmath>
#include <vector>
#include <deque>
#include <algorithm>
using namespace std;

int const MAX_N = 55;
int const MAX_CH = 100100;

int n, FND = 0;
long long M;

char st[MAX_CH];
int sm[MAX_N][MAX_N];

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	gets(st);
	int tst_count;
	sscanf(st,"%d",&tst_count);
	for (int qqq=1; qqq<=tst_count; qqq++) {
		cerr<<"\r"<<qqq<<"       ";

		printf("Case #%d: ",qqq);

		cin>>n>>M;
		FND = 0;
		
		//
		long long max_ANS = 1LL;
		for (int i=0; i<n-2; i++) max_ANS *= 2LL;

		if (M > max_ANS) FND = 0;
		else {
			FND = 1;

			for (int i=0; i<n; i++)
				for (int j=0; j<n; j++)
					sm[i][j] = 0;

			for (int i=0; i<n-1; i++)
				for (int j=0; j<i; j++)
					sm[j][i] = 1;

			if (max_ANS == M) {
				for (int i=0; i<n-1; i++)
					sm[i][n-1] = 1;
			}
			else {
				for (int i=1; i<n-1; i++)
					if ((M>>(i-1))&1)
						sm[i][n-1] = 1;
			}
		}
		//

		if (!FND) printf("IMPOSSIBLE");
		else {
			printf("POSSIBLE");
			for (int i=0; i<n; i++) {
				printf("\n");
				for (int j=0; j<n; j++) printf("%d",sm[i][j]);
			}
		}
		printf("\n");
	}
	return 0;
}


































//void dfs(int v, int stt) {
//	nnew[v] = 1;
//	for (int i=0; i<lst_len[v]; i++)
//		if (nnew[lst[v][i]] && lst[v][i] == stt)
//			is_CYC = 1;
//		else
//			if (!nnew[lst[v][i]])
//				dfs(lst[v][i], stt);
//}
//
//int is_cycle() {
//	for (int i=0; i<n; i++) lst_len[i] = 0;
//	for (int i=0; i<loc_e_len; i++)
//		lst[loc_e[i].first][lst_len[loc_e[i].first]++] = loc_e[i].second;
//
//	is_CYC = 0;
//	for (int i=0; i<n; i++) {
//		for (int j=0; j<n; j++) nnew[j] = 0;
//		dfs(i,i);
//	}
//	return is_CYC;
//}
//
//long long calc_cnt() {
//	int mx_mom =  max(n*3/2+3,loc_e_len+10);
//
//	for (int i=0; i<=mx_mom+2; i++)
//		for (int j=0; j<n; j++)
//			dd[i][j] = 0;
//
//	dd[0][0] = 1;
//
//	for (int i=0; i<n; i++) lst_len[i] = 0;
//	for (int i=0; i<loc_e_len; i++)
//		lst[loc_e[i].first][lst_len[loc_e[i].first]++] = loc_e[i].second;
//
//	
//	for (int mnt = 0; mnt < mx_mom; mnt++)
//		for (int i=0; i<n; i++)
//			if (dd[mnt][i] > 0)
//				for (int j=0; j<lst_len[i]; j++)
//					dd[mnt+1][lst[i][j]] += dd[mnt][i];
//
//	long long sum = 0;
//	for (int mnt=0; mnt <= mx_mom; mnt++)
//		sum += dd[mnt][n-1];
//	return sum;
//
//}