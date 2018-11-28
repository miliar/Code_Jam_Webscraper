#include<stdio.h>
#include<string.h>
#include<math.h>
#include<iostream>
#include<algorithm>
#include<map>
#include<vector>
using namespace std;
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define inf 0xfffffff
typedef long long lld;
#define eps 1e-8
#define pi acos(-1.0)
#define mod 1000002013
#define inv2 500001007
struct Node
{
	lld x,y,s;
	Node(){}
	Node(lld x0,lld y0,lld s0):x(x0),y(y0),s(s0){}
	void in()
	{
		cin >> x >> y >> s;
	}
}pp[8000010];
bool cmp(Node a,Node b)
{
	return a.x < b.x;
}
int qq;
lld N;
lld sum(lld x,lld y)
{
	lld a=(x+y)%mod;
	lld b=(y-x+1)%mod;
	lld T=(a*b*inv2)%mod;
	return T;
}
lld calc()
{
	lld T=0;
	for(int i=0;i<qq;i++)
	{
		lld t=pp[i].y-pp[i].x-1;
		if(t != -1)
		{
			lld add=sum(N-t,N);
			add=(add*pp[i].s)%mod;
			T=(T+add)%mod;
		}
	}
	return T;
}
int main()
{
	int cas;
	scanf("%d",&cas);
	for(int cc=1;cc<=cas;cc++)
	{
		int n;
		cin >> N >> n;
		qq=n;
		for(int i=0;i<n;i++)
			pp[i].in();
		lld A=calc();
		while(1)
		{
			bool doing=false;
			for(int i=0;i<qq;i++)if(pp[i].s != 0 && pp[i].x != pp[i].y)
				for(int j=0;j<qq;j++)if(pp[j].s != 0 && pp[j].x != pp[j].y && i != j)
				{
					if(pp[i].x < pp[j].x && pp[j].x <= pp[i].y && pp[i].y < pp[j].y)
					{
						lld mm=min(pp[i].s,pp[j].s);
						pp[i].s-=mm;
						pp[j].s-=mm;
						pp[qq++]=Node(pp[i].x,pp[j].y,mm);
						pp[qq++]=Node(pp[j].x,pp[i].y,mm);
						doing=true;
					}
					if(pp[j].x < pp[i].x && pp[i].x <= pp[j].y && pp[j].y < pp[i].y)
					{
						lld mm=min(pp[i].s,pp[j].s);
						pp[i].s-=mm;
						pp[j].s-=mm;
						pp[qq++]=Node(pp[i].x,pp[j].y,mm);
						pp[qq++]=Node(pp[j].x,pp[i].y,mm);
						doing=true;
					}
				}
			if(!doing)
				break;
		}
//		for(int i=0;i<qq;i++)
//			cout << pp[i].x << " " << pp[i].y << " " << pp[i].s << endl;
		lld B=calc();
		lld ans=(A-B+mod)%mod;
		printf("Case #%d: %I64d\n",cc,ans);
	}
	return 0;
}
/*
3
6 2
1 3 1
3 6 1
6 2
1 3 2
4 6 1
10 2
1 7 2
6 9 1

 */
