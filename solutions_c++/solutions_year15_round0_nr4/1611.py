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

const int M=6;


int main(){
     freopen("inp_bs.txt","r",stdin);
    freopen("out_bs.txt","w",stdout);    
    //ios_base::sync_with_stdio(false);
    char g[M][M][M];
    memset(g,'n',sizeof g);
    g[1][1][1]='g',g[2][1][1]='r',g[3][1][1]='r',g[4][1][1]='r';
    
    g[1][1][2]='g',g[2][1][2]='g',g[3][1][2]='r',g[4][1][2]='r';
    
    g[1][1][3]='g',g[2][1][3]='r',g[3][1][3]='r',g[4][1][3]='r';
    
    g[1][1][4]='g',g[2][1][4]='g',g[3][1][4]='r',g[4][1][4]='r';
    
    
    
    g[1][2][2]='g',g[2][2][2]='g',g[3][2][2]='r',g[4][2][2]='r';
    
    g[1][2][3]='g',g[2][2][3]='g',g[3][2][3]='g',g[4][2][3]='r';
    
    g[1][2][4]='g',g[2][2][4]='g',g[3][2][4]='r',g[4][2][4]='r';
    
    
    g[1][3][3]='g',g[2][3][3]='r',g[3][3][3]='g',g[4][3][3]='r';
    g[1][3][4]='g',g[2][3][4]='g',g[3][3][4]='g',g[4][3][4]='g';
    
    g[1][4][4]='g',g[2][4][4]='g',g[3][4][4]='r',g[4][4][4]='g';
    int t,tt=1,x,r,c;
    cin>>t;
    while(t--){
		cin>>x>>r>>c;
		if(r>c)
		swap(r,c);
		if(g[x][r][c]=='g')
		cout<<"Case #"<<tt++<<": GABRIEL"<<endl;
		else if(g[x][r][c]=='r')
		cout<<"Case #"<<tt++<<": RICHARD"<<endl;
		else
		cout<<"Case #"<<tt++<<": -1"<<endl;
	}
    
    return 0;
}
