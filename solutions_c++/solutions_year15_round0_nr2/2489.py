#include <bits/stdc++.h>
using namespace std;
 
#define gc getchar
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define i64 long long
#define MOD 1000000007
#define inf 2000000000
#define oo 9e18
#define TRACE
 
#ifdef TRACE
#define trace1(x)                cerr << #x << ": " << x << endl;
#define trace2(x, y)             cerr << #x << ": " << x << " | " << #y << ": " << y << endl;
#define trace3(x, y, z)          cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << endl;
#define trace4(a, b, c, d)       cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << endl;
#define trace5(a, b, c, d, e)    cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << endl;
#define trace6(a, b, c, d, e, f) cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << " | " << #f << ": " << f << endl;
 
#else
 
#define trace1(x)
#define trace2(x, y)
#define trace3(x, y, z)
#define trace4(a, b, c, d)
#define trace5(a, b, c, d, e)
#define trace6(a, b, c, d, e, f)
 
#endif
 
typedef pair<i64,i64> pll;
typedef pair<int,int> PII;

void scan(int &x)
{
    register int c = gc();
    x = 0;
    int neg = 0;
    for(;((c<48 || c>57) && c != '-');c = gc());
    if(c=='-') {neg=1;c=gc();}
    for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
    if(neg) x=-x;
}

const int M=1005;


int main(){
    freopen("inp_bs.txt","r",stdin);
    freopen("out_bs.txt","w",stdout);    
    //ios_base::sync_with_stdio(false);
    int t,d,p[M],ct[M],tt=1;
    cin>>t;
    while(t--){
		memset(ct,0,sizeof ct);
		cin>>d;
		int mx=-1;
		for(int i=0;i<d;i++){
			cin>>p[i];
			ct[p[i]]++;
			mx=max(mx,p[i]);
		}	
		int ans=inf;

		for(int j=1;j<=mx;j++){
			int an=0;
			for(int i=0;i<d;i++){
				if(p[i]>=j){
					an+=(p[i]+j-1)/j-1;
				}
			}
			ans=min(ans,an+j);
			//trace2(an,ans);
		}
		
		cout<<"Case #"<<tt++<<": "<<ans<<endl;
	}
    return 0;
}
