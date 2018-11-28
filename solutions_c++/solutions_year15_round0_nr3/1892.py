#include<cstdio>
#include<cstring>
#include<cmath>
#include<iostream>
#include<algorithm>
#include<set>
#include<map>
#include<stack>
#include<vector>
#include<queue>
#include<string>
#include<sstream>
#define eps 1e-9
#define ALL(x) x.begin(),x.end()
#define INS(x) inserter(x,x.begin())
#define FOR(i,j,k) for(int i=j;i<=k;i++)
#define MAXN 1005
#define MAXM 40005
#define INF 0x3fffffff
#define PB push_back
#define MP make_pair
#define X first
#define Y second
#define lc (k<<1)
#define rc ((k<<1)1)
using namespace std;
typedef long long LL;
int i,j,k,n,m,x,y,T,ans,big,cas,num,len;
bool flag;
const int ch[5][5]={{0,0,0,0,0},
                {0,1,2,3,4},
                {0,2,-1,4,-3},
                {0,3,-4,-1,2},
                {0,4,3,-2,-1}};
map<char ,int> mp;
int l,xl,sat,cur;
char s[1000000];
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&T);
	mp['i']=2;
	mp['j']=3;
	mp['k']=4;
	while (T--)
    {
        scanf("%d%d",&l,&x);
        scanf("%s",s);
        cur=1;

        sat=2;
        flag=false;
        printf("Case #%d: ",++cas);
        for (y=0;y<x;y++)
            for (i=0;i<l;i++)
            {
            	if (cur>1) cur=ch[cur][mp[s[i]]]; else
            	if (cur==1) cur=mp[s[i]]; else
            	if (cur==-1) cur=-mp[s[i]];else
            	if (-cur==mp[s[i]]) cur=1;else
            	if (cur<0) cur=ch[mp[s[i]]][-cur];
            	
                if (cur==sat)
                {
                	cur=1;
                	if (sat==1 && i==l-1 && y==x-1)
                    {
                        printf("YES\n");
                        flag=true;
                        break;
                    }
                	if (sat!=1)
                	{
                    	sat++;
                    	if (sat==5)
                    	{
                        	if (i==l-1 && y==x-1)
                        	{
                            	printf("YES\n");
                            	flag=true;
                            	break;
                        	}else sat=1;
                    	}else
                    	if (sat==1 && i==l-1 && y==x-1)
                    	{
                        	printf("YES\n");
                        	flag=true;
                        	break;
                    	}
                	}
                }
            }
        if (!flag)
        {
            printf("NO\n");
        }
    }
	return 0;
}
