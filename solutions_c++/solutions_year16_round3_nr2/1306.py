#include<cstdio>
#include<iostream>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<queue>
#include<stack>
#include<map>
#include<set>
#include<vector>
using namespace std;
#define Enter putchar(10)
#define Space putchar(32)
#define rep(x,y) for(x=0;x<(y);++x)
#define rep1(x,y) for(x=1;x<=(y);++x)
#define rep1o(x,y) for(x=1;x<(y);++x)
#define Rep(x,y) for(int x=0;x<(y);++x)
#define Rep1(x,y) for(int x=1;x<=(y);++x)
#define Rep1o(x,y) for(int x=1;x<(y);++x)
#define cin1(x) scanf("%d",&(x))
#define cin2(x1,x2) scanf("%d%d",&(x1),&(x2))
#define cout1(x) printf("%d",x)
#define cout2(x,y) printf("%d %d",x,y)
#define fin1(x) scanf("%lf",(x))
#define fin2(x1,x2) scanf("%lf%lf",&(x1),&(x2))
#define sin1(x) scanf("%s",(x))
#define aryclr(array,sign) memset((array),(sign),sizeof(array))
#define MAX(x,y) (((x)>(y))?(x):(y))
#define MIN(x,y) (((x)<(y))?(x):(y))
#define filll(X,Y) fill(X,X+(sizeof(X)/sizeof(X[0])),(Y))//��ס��һ��Ҫ��һά����ı�����
typedef pair<int,int> P;
typedef long long ll;
typedef unsigned long long ull;
//���ﶨ�峣����
const int dx[4]={1,0,-1,0},dy[4]={0,1,0,-1};//��������ϵ������������
const int MAX_N=3500; //�ύ֮ǰ�ĳ�20020
//������������
void in();
void solve();
//���ﶨ��ȫ�ֱ���
ll T,t;
ll B,M;
int grid[55][55];
/*��ʽ��������￪ʼ*/
int main()
{
#ifndef ONLINE_JUDGE
	freopen("B-small-attempt2.in","r",stdin);
	freopen("output.txt","w",stdout);
#endif
memset(grid,0,sizeof(grid));
scanf("%lld",&T);
for(t=1;t<=T;++t)
{
	in();
	for(int i=1;i<B;++i)
	{
		for(int j=i+1;j<=B;++j)
		{
			grid[i][j]=1;
		}
	}
	solve();
}
	return 0;
}
void in()
{
	scanf("%lld%lld",&B,&M);
}
void solve()
{
	printf("Case #%lld: ",t);
	if(((ll)1<<(B-2))<M)
	{
		printf("IMPOSSIBLE\n");
	}
	else
	{
		printf("POSSIBLE\n");
		ll x=((ll)1<<(B-2))-M;
		ll ni=2;
		while(x)
		{
			if(x&1)
			{
				grid[ni][B]=0;
			}
			++ni;
			x>>=1;
		}
		for(int i=1;i<=B;++i)
		{
			for(int j=1;j<=B;++j)
			{
				printf("%d",grid[i][j]);
			}Enter;
		}
	}
	
}



