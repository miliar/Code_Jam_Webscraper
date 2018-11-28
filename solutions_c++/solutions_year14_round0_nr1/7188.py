/*
	+AmitBaranwal
	amitbaranwal53@gmail.com
*/
#include <bits/stdc++.h>

using namespace std;

int temp,i,j,k,T;

#define CASE s(T);while(T--)
#define FOR(I,A,B) for(I=A;I<B;++I)
#define REP(i,n) FOR(i,0,n)
#define FORR(I,J,K) for(I=J;I>K;--I)
#define JAM(N) printf("Case #%d: ",N)
#define INPUT(A) freopen(A,"r",stdin);
#define OUTPUT(A) freopen(A,"w",stdout);

#define all(x) x.begin(), x.end()
#define fill(a, val) memset(a, val, sizeof(a))
#define INDEX(a, val) (lower_bound(all(a), val) - a.begin())

#define EXP 1e-10
#define INF (int)1e9

#define F first
#define S second
#define MP make_pair
#define PB push_back

typedef long long LL;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef pair<LL,LL> PLL;
typedef pair<int,PII> TRI;
typedef unsigned long long ULL;

#define deb(n) cout<<"(<<< DEBUG "<<n<<" >>>)"<<endl;

#define s(n)					scanf("%d",&n)
#define sl(n) 					scanf("%ld",&n)
#define sll(n) 					scanf("%%I64d",&n)
#define sf(n) 					scanf("%f",&n)
#define slf(n) 					scanf("%lf",&n)
#define ss(n) 					scanf("%s",n)

LL pow_r(LL d,LL n)
{
	LL x=1ll;
	while(n>0)
	{
		if(n&1)	x=(x*d);
		d=(d*d);
		n>>=1;
	}
	return x;
}

inline int next(){
    char c;int num=0;
    #ifndef ONLINE_JUDGE
    s(num);return num;
    #else
    c=getchar_unlocked();
    while(!(c>='0' && c<='9')) c=getchar_unlocked();
    while(c>='0' && c<='9'){
        num=(num<<3)+(num<<1)+c-'0';
        c=getchar_unlocked();
    }
    return num;
    #endif
}

//main code is here
int a[17],cnt,ans,ca,cb,tmp;
main()
{
	INPUT("A-small-attempt0.in");
	OUTPUT("output.txt");
	int k=1;
	CASE
	{
		cnt=0;
		fill(a,0);
		s(ca);
		--ca;
		REP(i,4)
		{
			REP(j,4)
			{
				s(tmp);
				if(ca == i)
				a[tmp]=1;
			}
		}
		s(cb);
		--cb;
		REP(i,4)
		{
			REP(j,4)
			{
				s(tmp);
				if(cb == i)
				{
					if(a[tmp])
					{
						ans=tmp;
						++cnt;
					}
				}
			}
		}
		JAM(k);
		switch(cnt)
		{
			case 0:puts("Volunteer cheated!");break;
			case 1:cout<<ans<<endl;break;
			default :puts("Bad magician!");
			
		}
		++k;
	}
	return 0;
}
