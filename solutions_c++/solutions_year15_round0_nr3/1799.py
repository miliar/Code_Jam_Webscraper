#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <set>
#define PB push_back
#define lc (k<<1)
#define rc ((k<<1)|1)
using namespace std;
typedef long long ll;
typedef unsigned long long ull;

int cha[5][5], L, X, sheng;
int a[10033], qian[10033], hou[10033];
vector<int> q,h;

/*
void cax(int &x,int y,int ans)
{
	int f=1;
	if(ans<0) f=-f,ans=-ans;
	if(y<0)   f=-f,y=-y;
	for(int i=1;i<=4;i++)
	{
		if(cha[i][y]==ans)  {x= f*i;return;}
		if(cha[i][y]==-ans) {x=-f*i;return;}
	}
}//*/

void cay(int x,int &y,int ans)
{
	int f=1;
	if(ans<0) f=-f,ans=-ans;
	if(x<0)   f=-f,x=-x;
	for(int i=1;i<=4;i++)
	{
		if(cha[x][i]==ans)  {y= f*i;return;}
		if(cha[x][i]==-ans) {y=-f*i;return;}
	}
}

int cal(int x, int y)
{
	if(!x || !y) return x+y;
	int t=1;
	if(x<0) t=-t,x=-x;
	if(y<0) t=-t,y=-y;
	return t*cha[x][y];
}

bool pan(int qn,int hn)
{
	if(qn+hn>L*X) return false;

	sheng=X-qn/L; qn%=L;
	sheng-=hn/L;  hn%=L;
	int now=0, sum=qian[L];
	if(qn+hn>L || sheng>=2)
	{
		sheng-=2; sheng%=4;
		now=hou[qn+1];
		for(int i=1;i<=sheng;i++) now=cal(now,sum);
		now=cal(now,qian[L-hn]);
	}
	else
	{
		cay(qian[qn],now,qian[L-hn]);
	}

	if(now==2) return true;
	return false;
}

int main()
{
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);

	cha[1][1]=cha[2][2]=cha[3][3]=-4;
	cha[1][4]=1;cha[2][4]=2;cha[3][4]=3;
	cha[4][1]=1;cha[4][2]=2;cha[4][3]=3;cha[4][4]=4;
	cha[1][2]=3;cha[2][1]=-3;
	cha[2][3]=1;cha[3][2]=-1;
	cha[3][1]=2;cha[1][3]=-2;

	int cas; scanf("%d",&cas);
	for(int t=1;t<=cas;t++)
	{
		scanf("%d%d",&L,&X);
		for(int i=1;i<=L;i++)
		{
			char ch=' ';
			while(ch!='i'&&ch!='j'&&ch!='k')
				ch=getchar();
			a[i]=ch-'i'+1;
		}

		printf("Case #%d: ",t);
		if(L*X<3) {puts("NO");continue;}
		if(L==1)  {puts("NO");continue;}

		q.clear(); h.clear();
		qian[1]=a[1]; hou[L]=a[L];
		for(int i=2;i<=L;i++)
			qian[i]=cal(qian[i-1],a[i]);
		for(int i=L-1;i>=1;i--)
			hou[i]=cal(a[i],hou[i+1]);
		int sum=qian[L];
		for(int i=1;i<=L;i++)
		{
			if(qian[i]==1) q.PB(i);
			else if(cal(sum,qian[i])==1) q.PB(L+i);
			else if(qian[i]==-1) q.PB(L*2+i);
			else if(cal(sum,qian[i])==-1) q.PB(L*3+i);

			if(hou[i]==3) h.PB(L-i+1);
			else if(cal(hou[i],sum)==3) h.PB(L*2-i+1);
			else if(hou[i]==-3) h.PB(L*3-i+1);
			else if(cal(hou[i],sum)==-3) h.PB(L*4-i+1);
		}
		/*
		for(int i=0;i<q.size();i++)
			printf("%d ",q[i]);puts("");
		for(int i=0;i<h.size();i++)
			printf("%d ",h[i]);puts("");
		//*/
		bool ok=false;
		for(int i=0;i<q.size()&&!ok;i++)
			for(int j=0;j<h.size()&&!ok;j++)
				if(pan(q[i],h[j])) ok=true;
		if(ok) puts("YES"); else puts("NO");
	}
	return 0;
}