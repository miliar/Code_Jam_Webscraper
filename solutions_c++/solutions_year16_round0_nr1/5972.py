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
bool SET[10];
void Solve(ll N)
{
	ll Temp,Res=1,P;
	if(N==0)
	{
		puts("INSOMNIA");
		return;
	}
	memset(SET,0,sizeof(SET));
	int Count=0,Rem;
	ll K=1;
	P=N;
	while(Count!=10)
	{
		Temp=P;
		while(Temp)
		{
			Rem = Temp%10;
			Temp = Temp/10;
			if(!SET[Rem])
				SET[Rem]=1,Count++;
		}
		K++;
		P=N*K;
	}
	Res = N*(K-1);
	printf("%lld\n",Res);


}


void FileIO()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
}

int main()
{
	FileIO();
	int i,T=100;
	ll N;
	//ll Test=1000000;
	scanf("%d",&T);
	for(i=1;i<=T;i++)
	{
		printf("Case #%d: ",i);
		scanf("%lld",&N);
		Solve(N);
	}

	return 0;
}
