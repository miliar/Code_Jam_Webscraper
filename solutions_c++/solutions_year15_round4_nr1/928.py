#include<bits/stdc++.h>
using namespace std;

//#pragma comment (linker, "/STACK:256000000")

typedef long long ll ;
typedef vector<ll> VI ;
typedef pair<ll,ll>  PP;
typedef vector<PP>  VPP ;

#define endl '\n'
#define  MP make_pair
#define PB push_back
#define F first
#define S second
#define sz(x) ((int)(x).size())
#define forn(i,n) for(int i=0;i<n;i++)
#define fileio freopen("in.txt","r",stdin); freopen("out.txt","w",stdout);
#define boost  ios_base::sync_with_stdio(false);cin.tie(0);
#define trace1(x)                cerr << #x << ": " << x << endl;
#define trace2(x, y)             cerr << #x << ": " << x << " | " << #y << ": " << y << endl;
#define trace3(x, y, z)          cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << endl;

ll mod = 1e9 + 7 ;
ll powmod(ll a,ll b) {ll res=1;a%=mod;for(;b;b>>=1){if(b&1)res=res*a%mod;a=a*a%mod;}return res;}
ll gcd(ll a , ll b){return b==0?a:gcd(b,a%b); }

/*---------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*                                                              SNIPPETS DONE
/*---------------------------------------------------------------------------------------------------------------------------------------------------------------*/


int g[105][105][4] ;

char in[105][105] ;

int r , c ;

void cancel(int i , int j , int x)
{


	if( (i<0) || (i>=r) || (j<0) || (j>=c) ) return ;
	
	
	if(in[i][j]!='.') 
	{
		g[i][j][x] = 1 ;
		return ;
	}
	
//	if(i==1||j==1)cout<<i<<" "<<j<<" "<<x<<endl;
	
	if(x==0) cancel(i,j-1,x);
	else if(x==1) cancel(i-1,j,x);
	else if(x==2) cancel(i,j+1,x);
	else cancel(i+1,j,x) ;

}

int main()
{
freopen("in.txt","r",stdin); freopen("out.txt","w",stdout);

int t  , i , j , k;

cin >> t ;
int tt = 0 ;
while(t--)
{
	tt++;
	
	for(i=0;i<=100;i++)
	for(j=0;j<=100;j++)
	for(k=0;k<4;k++) g[i][j][k] = 0 ;
	
	cin >> r >> c ;
	for(i = 0 ; i<r;i++) cin >> in[i] ;
	
	
    // o is allowed
	// 1 is not allowed
	
	for(j=0;j<c;j++) 
	{
		
        cancel(0,j,3);  
	    cancel(r-1,j,1);
    }

	for(j=0;j<r;j++) 
	{
		cancel(j,0,2);
	    cancel(j,c-1,0);	
    }

	
int ans = 0 ;
int x = 0 ;


for(i=0;i<r;i++)
{

for(j=0;j<c;j++)
{
	if(x==-1) break ;
	else x = 0 ;
	for(k=0;k<4;k++)   if(g[i][j][k]) x++;	
	if(x==4) x = -1 ;
	if(x==-1) break ;
	if(in[i][j]=='<'&&g[i][j][2]) ans ++ ;
	else if(in[i][j]=='>'&&g[i][j][0]) ans ++ ;
	else if(in[i][j]=='^'&&g[i][j][3]) ans ++ ;
	else if(in[i][j]=='v'&&g[i][j][1]) ans ++ ;	
}	
	
	
}
cout<<"Case #"<<tt<<": ";
if(x==-1) cout<<"Impossible\n";
else cout<<ans<<endl;	
	
}


return 0 ;

}


