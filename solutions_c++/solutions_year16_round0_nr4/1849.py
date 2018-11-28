#include<bits/stdc++.h>
using namespace std;

#define sd(mark) scanf("%d",&mark)
#define ss(mark) scanf("%s",&mark)
#define sl(mark) scanf("%lld",&mark)
#define debug(mark) printf("check%d\n",mark)
#define clr(mark) memset(mark,0,sizeof(mark))
#define F first
#define S second
#define MP make_pair
#define PB push_back
#define ll long long
void go(ll l,ll r,ll k,ll pos)
{
	if(l==r)
	{
		printf("%lld ",l+1);
		return;
	}
	ll len=r-l+1;
	len/=k;
	ll st=pos*len;
	ll en=(pos+1)*len-1;
	go(l+st,l+en,k,pos);
}
int main()
{
	//freopen("1.in","r",stdin);
	//freopen("1.out","w",stdout);
	int t,c,i,s;
	ll k;
	sd(t);
	for(int tt=1;tt<=t;++tt)
	{
		printf("Case #%d: ",tt);
		sl(k);sd(c);sd(s);
		ll len=1;
		for(i=0;i<c;++i)
			len=len*k;
		for(i=0;i<k;++i)
			go(0,len-1,k,i);
		printf("\n");
	}
}