/*
	amitbaranwal53@gmail.com
	IIT (BHU),VARANASI
*/
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <ctime>
#include <cmath>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <iostream>
#include <algorithm>

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
//#define sll(n) 					scanf("%lld",&n)
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
/*
inline int next(){
    char c;int num=0;
    c=getchar_unlocked();
    while(!(c>='0' && c<='9')) c=getchar_unlocked();
    while(c>='0' && c<='9'){
        num=(num<<3)+(num<<1)+c-'0';
        c=getchar_unlocked();
    }
    return num;
}
*/
//main code is here
int n,m,a[101][101],nm,done[101][101],mxr,mxc,flg;
TRI tr[10001],tmp;
main()
{
	INPUT("B-large.in");
	OUTPUT("amit.txt");
	int c=0;
	CASE
	{
		fill(done,0);
		k=0;
		flg=1;
		s(n);
		s(m);
		REP(i,n)REP(j,m)
		{s(a[i][j]);tr[k].F=a[i][j];tr[k].S.F=i;tr[k].S.S=j;++k;}
		nm=k;
		sort(tr,tr+nm);
		REP(k,nm)
		{
			tmp=tr[k];
			if(done[tmp.S.F][tmp.S.S]) continue;
			mxr=mxc=-1;
			REP(i,n) mxr=max(mxr,a[i][tmp.S.S]);
			REP(j,m) mxc=max(mxc,a[tmp.S.F][j]);
			if(mxr<=tmp.F)
			{
				REP(i,n) done[i][tmp.S.S]=1;
			}
			else if(mxc<=tmp.F)
			{
				REP(j,m) done[tmp.S.F][j]=1;
			}
			else
			{
				flg=0;
				break;
			}
			if(!flg) break;
		}
		JAM(++c);
		if(flg) puts("YES");
		else puts("NO");
	}
	return 0;
}