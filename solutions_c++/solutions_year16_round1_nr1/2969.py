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
	string S,Res,Ans;
	cin >> S;
	Res.push_back(S[0]);
	for(int i=1;i<S.length();i++)
	{
		if(S[i]>=Res[0])
		{
			Ans.push_back(S[i]);
			Ans.append(Res);
			Res=Ans;
			Ans.clear();
		}
		else
			Res.push_back(S[i]);
	}
	cout << Res << endl;
}


void FileIO()
{
	freopen("A-large.in","r",stdin);
	freopen("1Large_Output.txt","w",stdout);
}

int main()
{
	FileIO();
	int Tc,T=1;
	scanf("%d",&T);
	for(Tc=1;Tc<=T;Tc++)
	{
		printf("Case #%d: ",Tc);
		Solve();
	}
	return 0;
}
