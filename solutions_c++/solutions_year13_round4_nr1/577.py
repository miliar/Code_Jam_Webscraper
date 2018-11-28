#include<iostream>
#include<iomanip>
#include<cstring>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<string>
#include<set>
#include<map>
#include<list>
#include<algorithm>

using namespace std;

#define rp(i,l,r) for ( int i=(int)(l); i<=(int)(r); ++i )
#define dp(i,l,r) for ( int i=(int)(l); i>=(int)(r); --i )

typedef long long LL;

const int mn=1010;
const int mo=1000002013;

int Case;
int n,m;
LL  ans;

class Node{
public:
	LL l,r,v,pos;
} a[mn],b[mn],c[mn];

int num[mn];

bool cmp1( Node & a , Node & b )
{
	return a.l>b.l;
}

bool cmp2( Node & a , Node & b )
{
	return a.r<b.r;
}

int Count( LL x )
{
	LL ret=n*2-x+1;
	ret*=x;
	ret/=2;
	ret%=mo;
	return ret;
}

int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	cin >> Case;
	rp( Casei,1,Case )
	{
		cin >> n >> m;
		int ans=0;
		rp( i,1,m ) 
		{
			cin >> a[i].l >> a[i].r >> a[i].v ;
			ans+=Count(a[i].r-a[i].l)*a[i].v;
		}
		rp( i,1,m ) a[i].pos=i;
		rp( i,1,m ) b[i]=a[i];
		sort( a+1 , a+m+1 , cmp1 );
		sort( b+1 , b+m+1 , cmp2 );
		rp( i,1,m )
		{
			rp( j,1,m ) if ( b[j].v>0 && a[i].l<=b[j].r )
			{
				LL l=a[i].l;
				LL r=b[j].r;
				LL v=min( a[i].v , b[j].v );
				ans-=Count( r-l )*v;
				a[i].v-=v;
				b[j].v-=v;
				if ( a[i].v==0 ) break;
			}
		}
		cout << "Case #" << Casei << ": " << ans << endl;
	}
}
