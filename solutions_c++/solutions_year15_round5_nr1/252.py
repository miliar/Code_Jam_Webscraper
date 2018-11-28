#include <stdio.h>
#include <string.h>
#include <assert.h>
#include <algorithm>
#include <vector>

using namespace std;

const int MAXN = 1000000 + 100;
int N, D;
int S[MAXN], AS, CS, RS;
int M[MAXN], AM, CM, RM;
int R[MAXN];
int flag[MAXN];
int CNT;
vector<int> chd[MAXN];



bool cmp(const int& a, const int& b)
{
	return S[a] < S[b];
}

void mark(int id)
{
	if(flag[id] == -1) return;
	assert(flag[id] == 0);
	flag[id] = 1;
	++CNT;
	for(int i = 0; i < chd[id].size(); ++i)
	{
		mark(chd[id][i]);
	}
}
void demark(int id)
{
	if(flag[id] == 1)
		--CNT;
	flag[id] = -1;
	for(int i = 0; i < chd[id].size(); --i)
		demark(chd[id][i]);
	chd[id].clear();
}

int count_tree(int id)
{
	if(flag[id] != 0) return 0;
	int s = 1;
	for(int i = 0; i < chd[id].size(); ++i)
	{
		s += count_tree(chd[id][i]);
	}
	return s;
}


int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int ca = 1; ca <= T; ++ca)
	{
		scanf("%d %d", &N, &D);
		scanf("%d %d %d %d", &S[0], &AS, &CS, &RS);
		scanf("%d %d %d %d", &M[0], &AM, &CM, &RM);
		CS %= RS;
		CM %= RM;
		for(int i = 1; i < N; ++i)
		{
			S[i] = (S[i-1] * 1LL * AS + CS) % RS;
			M[i] = (M[i-1] * 1LL * AM + CM) % RM;
		}
		M[0] = -1;
		for(int i = 1; i < N; ++i)
			M[i] %= i;
		for(int i = 0; i < N; ++i)
		{
			R[i] = i;
			chd[i].clear();
		}
		for(int i = 1; i < N; ++i)
			chd[M[i]].push_back(i);
		sort(R, R+N, cmp);
		memset(flag, 0xff, sizeof(flag) );
		CNT = 0;
		int ret = 0;
		for(int i = 0, j = 0; i < N; ++i)
		{
			int id = R[i];
			flag[id] = 0;
			//if(id != 0)
			//{
			//	chd[M[id]].push_back(id);
			//	if(flag[M[id]] == 1)
			//		mark(id);
			//}
			//else
			//{
			//	mark(0);
			//}
			//printf("Added %d, CNT %d\n", id, CNT);
			while(S[id] - S[R[j]] > D)
			{
				flag[R[j]] = -1;
				++j;
				//int delid = R[j++];
				//demark(delid);
				//printf("Deleted %d, CNT %d\n", delid, CNT);
			}
			ret = max(ret, count_tree(0));
		}
		printf("Case #%d: %d\n", ca, ret);
	}
}
