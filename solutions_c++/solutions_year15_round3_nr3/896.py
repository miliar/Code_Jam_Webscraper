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

const int M=100005;

int main(){
	freopen("inp.txt","r",stdin);
    freopen("out.txt","w",stdout);    
    //ios_base::sync_with_stdio(false);
	int t,tt=1,c,d,v,a[7];
	vector<int>vv;
	
	cin>>t;
	while(t--){
		cin>>c>>d>>v;
		vv.clear();
		for(int i=0;i<d;i++){
			cin>>a[i];
			vv.pb(a[i]);
		}
		
		for(int i=1;i<=v;i++){
			bool  f=0;
			for(int mask=0;mask<(1<<vv.size());mask++){
				int s=0;
				for(int j=0;j<vv.size();j++){
					if(mask&(1<<j)){
						s+=vv[j];
					}
				}
				//cout<<i<<" "<<mask<<" "<<s<<endl;	
				if(s==i)
				{f=1;break;};
			}
			//cout<<i<<" "<<f<<endl;;
			if(f==0)
			vv.pb(i);
		}
		cout<<"Case #"<<tt++<<": "<<vv.size()-d<<endl;
	}
    return 0;
}

