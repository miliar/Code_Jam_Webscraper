#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<iostream>
#include<algorithm>
using namespace std;
#define INF 0x3f3f3f3f
#define LL long long
const double eps = 1e-8;
struct AhoCorasick
{
    const static int MAXN = 105;
    const static int CHSET = 26;
    int size, root, next[MAXN][CHSET], fail[MAXN], que[MAXN];
    int dcnt, dic[128];
    //dcnt对应字符的种类;dic存放每个字符在trie中的下标,不存在为-1;
    int val[MAXN];
    void init()
    {
        size = dcnt = 0;
        memset(dic, -1, sizeof(dic));
        newNode(root);
    }
    void newNode(int &x)
    {
        x = size++;
        memset(next[x], -1, sizeof(next[x]));
        fail[x] = -1;
        val[x] = 0;
    }
    int getIdx(char ch)
    {
        if(dic[ch] == -1)   dic[ch] = dcnt++;
        return dic[ch];
    }
    void insert(const char s[], int v)
    {
        int i = 0, idx;
        int cur = root;
        while(s[i])
        {
            idx = getIdx(s[i]);
            if(next[cur][idx] == -1)
                newNode(next[cur][idx]);
            cur = next[cur][idx];
            i++;
        }
        //不同的题此处不同
        val[cur] += v;
    }
    void build()
    {
        int i, cur, p, head = 0, tail = 0;
        que[tail++] = root;
        while(head < tail)
        {
            cur = que[head++];
            for(i = 0; i < CHSET; i++)
            {
                p = (fail[cur] == -1) ? root : next[fail[cur]][i];
                if(next[cur][i] != -1)
                {
                    fail[next[cur][i]] = p;
                    //统计fail节点所包含的val信息
                    //val[next[cur][i]] |= val[p];
                    que[tail++] = next[cur][i];
                }
                else
                    next[cur][i] = p;
            }
        }
    }
}ac;

const int M = 105;
double dp[M][M][M];
char keyboard[M], target[M];
int K, L, S, cnt[26];
//匹配对应的solve, HDU 2222
double solve()
{
	memset(cnt, 0, sizeof(cnt));
	for(int i = 0; i <= K; i++)
		cnt[keyboard[i] - 'A']++;
	
	for(int i = 0; i <= S; i++)
		for(int j = 0; j <= S; j++)
			for(int k = 0; k <= ac.size; k++)
				dp[i][j][k] = -INF;
	
	dp[0][0][ac.root] = 1.0;
	for(int i = 0; i < S; i++)
	{
		for(int j = 0; j <= S; j++)
			for(int k = 0; k < ac.size; k++)
			{
				if(dp[i][j][k] > -eps)
				{
					for(int p = 0; p < 26; p++)
					{
						if(cnt[p] == 0)
							continue;
						int go = ac.next[k][ac.getIdx('A' + p)];
						
						if(dp[i + 1][j + ac.val[go]][go] > -eps)
							dp[i + 1][j + ac.val[go]][go] += dp[i][j][k] * cnt[p] / K;
						else
							dp[i + 1][j + ac.val[go]][go] = dp[i][j][k] * cnt[p] / K;	
					}
				}
			}
	}
	int maxv = 0;
	double given = 0;
	for(int j = 0; j <= S; j++)
		for(int k = 0; k < ac.size; k++)
		{
			if(dp[S][j][k] > -eps)
			{
				given += dp[S][j][k] * j;
				maxv = max(maxv, j);
			}
		}
	//cout << maxv << " " << given << endl;
	return abs(maxv * 1.0 - given);
}
int main()
{
    int t, cas = 1;
    scanf("%d", &t);
    while(t--)
    {
    	scanf("%d%d%d", &K, &L, &S);
        scanf("%s", keyboard);
        scanf("%s", target);
        ac.init();
        ac.insert(target, 1);
        ac.build();
        printf("Case #%d: %.9lf\n", cas++, solve());
    }
    return 0;
}
/*
1
2 3 4
AA
AAA

*/
