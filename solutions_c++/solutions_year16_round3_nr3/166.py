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

int const MAX_N = 10;
int const MAX_CH = 100100;

int n, MX_MV = 0;
int cnt[MAX_N], sum = 0;
char st[MAX_CH];
int a,b,c,K;
int ms_len = 0;

int used[10000000];
int cnt_12[MAX_N][MAX_N], cnt_13[MAX_N][MAX_N], cnt_23[MAX_N][MAX_N];
vector<int> all_v[50];

struct tpp {
	int a,b,c, code;
} ans[1024*1024], loc_ans[1024*1024], ms[1024*1024];

bool operator < (const tpp &A, const tpp &B) {
	return A.code < B.code;
}

int encode(tpp xx) {
	return xx.a * 16 * 16 + xx.b * 16 + xx.c;
}

void rec(int from, int mv) {
	if (mv > MX_MV) {
		MX_MV = mv;
		for (int i=0; i<MX_MV; i++)
			ans[i] = loc_ans[i];
	}

	for (int i=from; i<ms_len; i++) {
		if (!used[ms[i].code])
			if (cnt_12[ms[i].a][ms[i].b] < K &&
				cnt_13[ms[i].a][ms[i].c] < K &&
				cnt_23[ms[i].b][ms[i].c] < K) {

				used[ms[i].code] = 1;
				cnt_12[ms[i].a][ms[i].b]++;
				cnt_13[ms[i].a][ms[i].c]++;
				cnt_23[ms[i].b][ms[i].c]++;

				loc_ans[mv] = ms[i];

				rec(from+1, mv+1);

				used[ms[i].code] = 0;
				cnt_12[ms[i].a][ms[i].b]--;
				cnt_13[ms[i].a][ms[i].c]--;
				cnt_23[ms[i].b][ms[i].c]--;
			}

		rec(from+1, mv);
	}

}

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	gets(st);
	int tst_count;
	sscanf(st,"%d",&tst_count);
	int USED_FLAG = 0;

	for (int qqq=1; qqq<=tst_count; qqq++) {
		cerr<<"\r"<<qqq<<"     ";
		printf("Case #%d:",qqq);

		//
		scanf("%d%d%d%d",&a,&b,&c,&K);
		int MX_VAL = c;

		MX_MV = 0;
		ms_len = 0;
		for (int i=1; i<=a; i++)
			for (int j=1; j<=b; j++)
				for (int k=1; k<=c; k++) {
					ms[ms_len].a = i;
					ms[ms_len].b = j;
					ms[ms_len].c = k;
					ms[ms_len].code = encode(ms[ms_len]);
					ms_len++;
				}
		sort(ms,ms+ms_len);

		for (int i=0; i<MAX_N; i++)
			for (int j=0; j<MAX_N; j++)
				cnt_12[i][j]=cnt_13[i][j]=cnt_23[i][j] = 0;

		for (int i=0; i<=ms_len; i++)
			all_v[i].clear();

		for (int code=0; code<(1<<ms_len); code++) {
			int x = code, cnt = 0;
			while (x) {
				cnt += x&1;
				x>>=1;
			}

			all_v[cnt].push_back(code);
		}

		int Ok = 0;

		for (int ee=ms_len; ee>=0 && !Ok; ee--)
			for (int rr=0; rr<(int) all_v[ee].size() && !Ok; rr++) {
				int code = all_v[ee][rr];
				int mv = 0;
				for (int i=0; i<ms_len; i++)
					if ((code>>i)&1) {
						loc_ans[mv] = ms[i];
						mv++;
					}

				for (int i=1; i<=MX_VAL; i++)
					for (int j=1; j<=MX_VAL; j++)
						cnt_12[i][j]=cnt_13[i][j]=cnt_23[i][j] = 0;

				USED_FLAG++;
				Ok = 1;
				for (int i=0; i<mv; i++)
					if (used[loc_ans[i].code] == USED_FLAG) {
						Ok = 0;
						break;
					}
					else
						used[loc_ans[i].code] = USED_FLAG;

				for (int i=0; i<mv; i++) {
					cnt_12[loc_ans[i].a][loc_ans[i].b]++;
					cnt_13[loc_ans[i].a][loc_ans[i].c]++;
					cnt_23[loc_ans[i].b][loc_ans[i].c]++;

					if (cnt_12[loc_ans[i].a][loc_ans[i].b] > K) {
						Ok = 0;
						break;
					}

					if (cnt_13[loc_ans[i].a][loc_ans[i].c] > K) {
						Ok = 0;
						break;
					}

					if (cnt_23[loc_ans[i].b][loc_ans[i].c] > K) {
						Ok = 0;
						break;
					}
				}

				if (Ok) {
					printf(" %d",mv);
					for (int i=0; i<mv; i++)
						printf("\n%d %d %d",loc_ans[i].a,loc_ans[i].b,loc_ans[i].c);
					break;
				}
			}
		//rec(0, 0);

		//printf(" %d",MX_MV);
		//for (int i=0; i<MX_MV; i++)
		//	printf("\n%d %d %d",ans[i].a,ans[i].b,ans[i].c);
		//

		printf("\n");
	}
	return 0;
}