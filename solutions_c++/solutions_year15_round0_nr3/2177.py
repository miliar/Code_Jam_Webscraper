#include<cstdio>
#include<cstring>
#include<cmath>
#include<vector>
#define rep(i,n) for(int i=0;i<(n);i++)
#define repd(i,n) for(int i=n-1;i>=0;i--)
#define pb push_back
#define mp make_pair
#define x first
#define y second
using namespace std;
const int Mul[4][4]=
{
	1,2,3,4,
	2,-1,4,-3,
	3,-4,-1,2,
	4,3,-2,-1
};
char s[10086];
int num[10086];
int pre[10086];
int L;
long long X;
int min(int a,int b){if(a<b)return a;return b;}
int abs(int a){if(a<0)return -a;return a;}
int s2num(char c)
{
	if(c=='i')return 2;
	if(c=='j')return 3;
	return 4;
}
char mul(int a,int b)
{
	int ret=Mul[abs(a)-1][abs(b)-1];
	if(a*b>0)return ret;
	else return -ret;
}
void init()
{
	rep(i,L)num[i]=s2num(s[i]);
	pre[0]=num[0];
	for(int i=1;i<L;i++)pre[i]=mul(pre[i-1],num[i]);
}
bool check1()
{
	int Xp=X%4;
	int ans=1;
	rep(i,Xp)ans=mul(ans,pre[L-1]);
	return ans==-1;
}
pair<long long,int> check2()
{
	int ans=1;
	rep(i,min(X,4))
	{
		rep(j,L)
		{
			ans=mul(ans,num[j]);
			if(ans==2)return mp(i,j);
		}
	}
	return mp(-1,-1);
}
pair<long long,int> check3()
{
	int ans=1;
	rep(i,min(X,4))
	{
		repd(j,L)
		{
			ans=mul(num[j],ans);
			if(ans==4)return mp(X-1-i,j);
		}
	}
	return mp(-1,-1);
}

int main()
{
	freopen("C-small-attempt2.in","r",stdin);
	freopen("C-small-attempt2.out","w",stdout);
	int T,P=0;
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d%lld",&L,&X);
		scanf("%s",s);
		init();
		bool flag;
		if(check1())
		{
			pair<long long,int> p1=check2(),p2=check3();
			if(p1.y==-1 || p2.y==-1)flag=false;
			else if(p1.x+1<p2.x)flag=true;
			else if(p1.x+1==p2.x)
			{
				if(p1.y==L-1 && p2.y==0)flag=false;
				else flag=true;
			}
			else if(p1.x==p2.x && p1.y+1<p2.y)flag=true;
			else flag=false;
		}
		else flag=false;
		if(flag)printf("Case #%d: YES\n",++P);
		else printf("Case #%d: NO\n",++P);
	}
	return 0;
}
