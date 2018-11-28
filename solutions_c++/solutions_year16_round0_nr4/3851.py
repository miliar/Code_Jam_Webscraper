#include<bits/stdc++.h>
using namespace::std;

const int  Max = 1e5+1;
const int  Mod = 1e9+7;

#define ll  long long
#define ull unsigned ll
#define LD long double

#define mp make_pair
#define bs binary_search
#define gcd __gcd
#define PI  M_PI
#define pb push_back
#define pp pop_back
#define sz size
#define ln length
#define ff first
#define ss second

#define mset(a,v) 		memset(a,v,sizeof(a))
#define mcpy(a,b)  		memcpy(a,b,sizeof(a))
#define mcmp(a,b)   	memcmp(a,b,sizeof(a))
#define CountSetBits(x) __builtin_popcount(x)
#define SetBit(x,pos)   x=((x) | (1<<pos))
#define UnsetBit(x,pos) x=((x) & ~(1<<pos))
#define CheckBit(x,pos) ((x)&(1<<(pos)))?1:0
#define all(a) 			a.begin(),a.end()
#define vsort(a) 		sort(all(a))
#define vfind(a,e) 		bs(all(a),e)
#define ModVal(a,M)	    (a%M+M)%M
#define lbnd(A, x)		(lower_bound(all(A), x) - A.begin())
#define ubnd(A, x) 		(upper_bound(all(A), x) - A.begin())


/* Code Starts Here */

ll POWER(ll base,ll exp)
{
   ll Ans=1;
   base = base;
   while(exp>0)
   {
      if(exp&1)
         Ans = (Ans*base);
      exp = exp >> 1LL;
      base = (1LL*base*base);
   }
   return Ans;
}

void Solve()
{
	ll i,j,K,C,S;
	cin >> K >> C >> S;
	if(K==1)
	{
		cout << "1" << endl;
	}
	else if (C==1)
	{
		for(i=1;i<K;i++)
			cout << i << " ";
		cout << K << endl;
	}
	else
	{
		for(i=1,j=2;i<K-1;i++,j=j+(K+1))
		{
			cout << j << " ";
		}
		cout << j << endl;
	}
}


void FileIO()
{
	freopen("D-small-attempt2.in","r",stdin);
	freopen("output.txt","w",stdout);
}

int main()
{
	FileIO();
	int i,T=1;
	scanf("%d",&T);
	for(i=1;i<=T;i++)
	{
		printf("Case #%d: ",i);
		Solve();
	}
	return 0;
}
