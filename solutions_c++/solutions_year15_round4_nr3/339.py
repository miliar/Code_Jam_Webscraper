#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<string>
#include<map>
#include<cmath>
#include<iostream>
#include<vector>
#include<ctime>
#include<algorithm>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> per;
#define mp(x,y) make_pair(x,y)
inline int readT(){
    int ret = 0; char c;
    while(c = getchar(), c < '0' || c > '9') ; ret = c - 48;
    while(c = getchar(), c >= '0' && c <= '9') ret = ret * 10 + c - 48;
    return ret;
}
const int MOD = 1000000007;
const int INF = 1000000007;
const int M = 100005;
const int N = 20105;
char s[205][N];
int a[205][N],t[205];
bool u[4105][2],g[4105][2],fg[4105];
map<ull,int>lzs;
int main()
{
	//ios_base::sync_with_stdio(0);
	freopen("C-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T,ca=1;
	scanf("%d",&T);
	while(T--)
	{
		printf("Case #%d: ",ca++);
		cerr << "T: " << T << endl;
		lzs.clear();
		memset(u,0,sizeof(u));
		int nd=0;
		int n;
		scanf("%d",&n);
		getchar();
		for(int i=0;i<n;i++)
		{
			gets(s[i]);
			int le=strlen(s[i]),k=0;
			for(int j=0;j<le;j++)
			{
				if(s[i][j]==' ')continue;
				ull v=0;
				for(;j<le&&s[i][j]!=' ';j++)
				{
					v=v*31+(s[i][j]-'a')+1;
				}
				int id=lzs[v];
				if(!id)id=lzs[v]=++nd;
				a[i][k++]=id;
				//printf("%d ",id);
			}
			//puts("");
			t[i]=k;
			//printf("i:%d k:%d \n",i,k);
		}
		for(int i=0;i<2;i++)
		{
			for(int j=0;j<t[i];j++)
			{
				u[a[i][j]][i]=true;
			}
		}
		int m=(1<<(n-2)),ret=INF;
		for(int i=0;i<m;i++)
		{
			for(int j=0;j<n;j++)
			{
				for(int h=0;h<t[j];h++)
				{
					g[a[j][h]][0]=g[a[j][h]][1]=false;
					fg[a[j][h]]=false;
				}
			}
			for(int j=0;j<n-2;j++)
			{
				int p;
				if(i&(1<<j))p=0;
				else p=1;
				for(int h=0;h<t[j+2];h++)
				{
					g[a[j+2][h]][p]=true;
				}
			}
			int tmp=0;
			for(int j=0;j<n;j++)
			{
				for(int h=0;h<t[j];h++)
				{
					int x=a[j][h];
					if((g[x][0]||u[x][0])&&(g[x][1]||u[x][1]))
					{
						if(!fg[x])tmp++;
						fg[x]=true;
					}
				}
			}
			if(ret>tmp)ret=tmp;
		}
		printf("%d\n",ret);
	}
    return 0;
}




















