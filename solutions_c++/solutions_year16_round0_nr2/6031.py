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
void Solve()
{
	string K;
	cin >> K;
	vector<int> Arr;
	K[0]=='-'?Arr.push_back(0):Arr.push_back(1);
	int i,j,Count=0;
	for(i=1;i<K.sz();i++)
	{
		if(K[i]!=K[i-1])
		{
			K[i]=='-'?Arr.push_back(0):Arr.push_back(1);
		}
	}
	i=Arr.sz()-1;
	while(i>=0)
	{
		if(Arr[i]==0)
		{
			for(j=i;j>=0;j--)
				Arr[j]=!Arr[j];
			Count++;
		}
		while(i>=0 && Arr[i]==1)
			i--;
	}
	printf("%d\n",Count);
}


void FileIO()
{
	freopen("B-large.in","r",stdin);
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
