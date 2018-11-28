//Naveen Sangtani
#include<bits/stdc++.h>
using namespace std;

typedef long long int          LL;
typedef unsigned long long     ULL;
typedef long double            LD;


#define pb                   push_back
#define ppb                  pop_back
#define mp                   make_pair
#define ff                   first
#define ss                   second


#define PI                   acos(-1.0)
#define e                    exp(1.0)
#define EPS                  1e-9


#define count_1(n)           __builtin_popcountll(n)


#define fr(i,a,b)            for(int i=a;i<=b;++i)
#define rev(i,b,a)           for(int i=b;i>=a;--i)
#define foreach(v,c)         for( typeof((c).begin()) v = (c).begin();  v != (c).end(); ++v)
#define CLR(A)               memset(A,false,sizeof(A))
#define FILL(A,n,val)        for(int i=0;i<n;++i) A[i]=val
#define all(x)               x.begin(),x.end()
#define TT()                 int tc;cin>>tc;while(tc--)


#define dbg(vari)            cout<<#vari<<" = "<<(vari)<<endl;
#define dbgA(A,n)            cout<<endl;fr(i,0,n-1) cout<<i<<" -- > "<<A[i]<<endl;
#define dbgV(V)              cout<<endl;fr(i,0,V.size()-1){cout<<i<<" --> "<<V[i].ff<<" "<<V[i].ss<<endl;}
#define dbgG(G,n)            cout<<endl;fr(i,1,n){cout<<i<<" --> ";fr(j,0,(G[i].size())-1) cout<<"("<<G[i][j].ff<<" , "<<G[i][j].ss<<")"<<"  ";cout<<endl;}
#define ns                  cout<<endl<<" ----- entered -----"<<endl;
#define SP                    system("pause");

#define maX(a,b)                ((a)>(b)?(a):(b))
#define miN(a,b)                ((a)<(b)?(a):(b))
#define abS(x)                  ((x)<0?-(x):(x))


typedef pair<int,int>          PII;
typedef vector<int>           VI;
typedef vector<PII>          VPII;
typedef vector<VPII>         VVPII;
typedef set<int>              SI;
typedef set<PII>             SPII;
typedef map<int,int>           MPII;


typedef pair<LL,LL>          PLL;
typedef pair<PLL,LL>         PPLL;
typedef vector<string>           VS;
typedef vector<PLL>          VPLL;
typedef vector<VPLL>         VVPLL;
typedef set<LL>              SL;
typedef set<PLL>             SPLL;
typedef map<LL,LL>           MPLL;


LL gcd(LL x, LL y) {return y == 0 ? x : gcd(y, x % y);}
bool isPalin(string x) {LL len = x.length();fr(i,0,(len/2)-1) {if (x[i] != x[len - 1 - i])return false;}return true;}
string tolowerStr(string x){string ret = "";fr(i,0,(LL)x.length()-1) {ret.pb(tolower(x[i]));}return ret;}
string toupperStr(string x) {string ret = "";fr(i,0,(LL)x.length()-1) {ret.pb(toupper(x[i]));}return ret;}
bool double_equals(double a, double b, double epsilon = 0.1){return std::abs(a - b) < epsilon;}


#define INF                 INT_MAX
#define LINF                LONG_LONG_MAX
#define MAX                 100007
#define mod                 1000000007


int main()
{
    freopen("inp2.txt","r",stdin);
    freopen("out2.txt","w",stdout);
    //ios_base::sync_with_stdio(false);
    int cnt = 0,x,r,c;
    TT()
    {
		
		cnt++;
		
		cin>>x>>r>>c;
		
		if(x==1)
		cout<<"Case #"<<cnt<<": "<<"GABRIEL"<<endl;
		else if(x==2)
		{
			if(r%2!=0 && c%2!=0)
			cout<<"Case #"<<cnt<<": "<<"RICHARD"<<endl;
			else
			cout<<"Case #"<<cnt<<": "<<"GABRIEL"<<endl;
		}
		
		else if(x==3)
		{
			if( (r==2 && c==3)  || (r==3 && c==2)  || (r==3 && c==3) || (r==4 && c==3) || (r==3 && c==4))
			cout<<"Case #"<<cnt<<": "<<"GABRIEL"<<endl;
			else
			cout<<"Case #"<<cnt<<": "<<"RICHARD"<<endl;
		}
		
		else if(x==4)
		{
			if((r==3 && c==4)  || (r==4 && c==3) || (r==4 && c==4))
			cout<<"Case #"<<cnt<<": "<<"GABRIEL"<<endl;
			else
			cout<<"Case #"<<cnt<<": "<<"RICHARD"<<endl;
		}
		
		
	}
    
return 0;
}
