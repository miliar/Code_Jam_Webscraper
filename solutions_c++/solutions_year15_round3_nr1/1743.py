#include<bits/stdc++.h>
using namespace std;
#define s(n) scanf("%d",&n)
#define sl(n) scanf("%lld",&n)
#define ss(n) scanf(" %s",n)
#define s2(a,b) scanf("%d %d",&a,&b)
#define pb push_back
#define mp make_pair
#define vi vector<int>
#define ii pair<int,int>
#define F first
#define S second
#define P printf
#define E <<endl
#define ll long long

int solve(int r,int c,int w)
{
	if(w==c)
		return c;
	else
	{
		return (ceil((c*1.0)/w) -1 + w);
	}
}

int main()
{
     //freopen("A-larg.in", "r",stdin);
     //freopen("A-op-large.txt", "w" ,stdout);
     int t,o;
     s(t);
     for(o=1;o<=t;o++)
     {
          int r,c,w;
          scanf("%d %d %d",&r,&c,&w);
          ll ans=solve(r,c,w);
          P("Case #%d: %lld\n",o,ans);
     }
}
