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
int n,tot;
LL  m,p[mn];
LL  ans;

bool Check1( LL x )
{
	LL l=x;
	rp( i,1,tot-1 )
	{
		l--;
		l/=2;
		if ( l==0 ) return true;
	}
	return false;
}

bool Check2( LL x )
{
	LL l=x , tmp=m;
	LL temp=p[n-1];
	while ( temp )
	{
		if ( tmp<=temp )
		{
			l=(l+1)/2;
			if ( l>=temp ) return false;
		} else
		{
			if ( (l+1)/2<temp ) return true;
			tmp-=temp;
			l-=temp;
		}
		if ( l==0 ) return true;
		temp/=2;
	}
	if ( l==0 ) return true;
	return false;
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	cin >> Case;
	p[0]=1;
	rp( i,1,60 ) p[i]=p[i-1]<<1;
	rp( Casei,1,Case )
	{
		cin >> n >> m;
		if ( m==p[n] )
		{
			cout << "Case #" << Casei << ": " << m-1 << " " << m-1 << endl;
			continue;
		}
		LL tmpmm=m;
		tot=0;
		dp( i,n-1,0 ) if ( m<=p[i] )
		{
			tot=n-i;
			break;
		} else m-=p[i];
		m=tmpmm;
		LL l=1 , r=1;
		r<<=n;
		r-=1;
		while ( l<=r )
		{
			LL mid=l+r >> 1;
			if ( Check1( mid ) ) l=mid+1; else r=mid-1;
		}
		cout << "Case #" << Casei << ": " << l-1 << " ";
		l=1 , r=1;
		r<<=n;
		r-=1;
		while ( l<=r )
		{
			LL mid=l+r >> 1;
			if ( Check2( mid ) ) l=mid+1; else r=mid-1;
	//		cout << l << " " << r << endl;
		}
		cout << l-1 << endl;
	}
}
