#include <cstdio>
#include <algorithm>
#include <vector>
#include<iostream>
#define fru(j,n) for(int j=0;j<n;++j)
#define tr(it,x) for(typeof(x.begin())it=x.begin();it!=x.end();++it)
#define x first
#define y second

using namespace std;
typedef pair<int,int> pii;
typedef long long LL;
typedef double D;

const int MAXN = 100005;
void solve()
{
	D C,F,X,time=0.0,in=2.0,wyn;
	scanf("%lf%lf%lf",&C,&F,&X);
	wyn=X/in;
	while(1)
	{
		D temp;
		time+=C/in;
		in+=F;
		temp=time+X/in;
		if(temp<wyn){wyn=temp;}
		else break;
	}
	printf("%.7lf\n",wyn);
}

int main()
{
	int t;
	scanf("%d",&t);
	fru(i,t){printf("Case #%d: ",i+1);solve();}
    return 0;
}
