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
    freopen("inp_as.txt","r",stdin);
    freopen("out_as.txt","w",stdout);    
    //ios_base::sync_with_stdio(false);
    i64 tt=1,x,y,n,t,a[M];
    cin>>t;
    while(t--){
		cin>>n;
		i64 mx=-1;
		for(int i=0;i<n;i++){
			cin>>a[i];
			mx=max(mx,a[i]);
		}	
		
		x=0,y=inf;
		for(int i=0;i<n-1;i++){
			if(a[i+1]<a[i])
			x+=(a[i]-a[i+1]);			
		}
		i64 mn=-1;
		for(int i=0;i<n-1;i++){
			if(a[i+1]<a[i])
			mn=max(mn,a[i]-a[i+1]);
		}
		
		//cout<<mn<<endl;
		if(mn!=-1){
			for(int j=mn;j<=mn;j++){
				i64 yy=0;
				for(int i=0;i<n-1;i++){
					if(a[i]!=0){
						yy+=min(a[i],(i64)j);
						//trace3(i,j,yy);
					}
				}
				y=min(yy,y);
				//trace2(y,yy);
			}
		}
		if(mn==-1)
		y=0;
		cout<<"Case #"<<tt++<<": "<<x<<" "<<y<<endl;
	}
    return 0;
}
