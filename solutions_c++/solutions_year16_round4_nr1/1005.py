#include<cstdio>
#include<cstring>
#include<algorithm>
#define mem(a,b) memset(a,b,sizeof(a))
using namespace std;

char path[3][5010], str1[4] = "PRS";
int cou, n, r, p, s, tt;
int num[3];
char str[2][5010];

void dfs(int cnt, int win)
{
	if(cnt == n)
	{
		num[win] ++;
		path[tt][cou++] = str1[win];
		return;
	}
	if(win == 0)
	{
	    int s = cou;
		dfs(cnt + 1,0);
		dfs(cnt + 1,1);
		int e = cou;
		int len = (e - s) / 2;
		for(int i = 0; i < len; i ++)
        {
            str[0][i] = path[tt][s + i];
            str[1][i] = path[tt][s + len + i];
        }
        if(strcmp(str[0],str[1]) > 0)
        {
            for(int i = 0; i < len; i ++)
            {
                path[tt][s + i] = str[1][i];
            }
            for(int i = 0; i < len; i ++)
            {
                path[tt][s + len + i] = str[0][i];
            }
        }
	}
	else if(win == 1)
	{
        int s = cou;
        dfs(cnt + 1, 2);
        dfs(cnt + 1, 1);
		int e = cou;
		int len = (e - s) / 2;
		for(int i = 0; i < len; i ++)
        {
            str[0][i] = path[tt][s + i];
            str[1][i] = path[tt][s + len + i];
        }
        if(strcmp(str[0],str[1]) > 0)
        {
            for(int i = 0; i < len; i ++)
            {
                path[tt][s + i] = str[1][i];
            }
            for(int i = 0; i < len; i ++)
            {
                path[tt][s + len + i] = str[0][i];
            }
        }
	}
	else
	{
		int s = cou;
        dfs(cnt + 1,0);
		dfs(cnt + 1,2);
		int e = cou;
		int len = (e - s) / 2;
		for(int i = 0; i < len; i ++)
        {
            str[0][i] = path[tt][s + i];
            str[1][i] = path[tt][s + len + i];
        }
        if(strcmp(str[0],str[1]) > 0)
        {
            for(int i = 0; i < len; i ++)
            {
                path[tt][s + i] = str[1][i];
            }
            for(int i = 0; i < len; i ++)
            {
                path[tt][s + len + i] = str[0][i];
            }
        }
	}
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
	int t;
	scanf("%d",&t);
	for(int ii = 1; ii <= t; ii ++)
	{
		scanf("%d%d%d%d",&n,&r,&p,&s);
		mem(num,0);
		cou = 0;
		tt = 0;
		dfs(0, 0);
		if(num[0] == p && num[1] == r && num[2] == s)
		{
		    path[tt][cou] = '\0';
		    tt ++;
		}
		mem(num,0);
		cou = 0;
		dfs(0, 1);
		if(num[0] == p && num[1] == r && num[2] == s)
		{
		    path[tt][cou] = '\0';
			tt ++;
		}
		mem(num,0);
		cou = 0;
		dfs(0, 2);
		if(num[0] == p && num[1] == r && num[2] == s)
		{
		    path[tt][cou] = '\0';
			tt ++;
		}
		if(tt == 0)
        {
            printf("Case #%d: IMPOSSIBLE\n",ii);
            continue;
        }
        int no = 0;
		for(int i = 1; i < tt; i ++)
        {
            if(strcmp(path[i], path[no]) < 0)
            {
                no = i;
            }
        }
		printf("Case #%d: %s\n",ii,path[no]);
	}
}
