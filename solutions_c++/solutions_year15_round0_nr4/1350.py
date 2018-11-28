#include<bits/stdc++.h>

using namespace std;


#define LL 				"%I64d"
#define sz(a) 			int((a).size())
#define pb 				push_back
#define mp 				make_pair
#define F				first
#define S				second
#define all(c) 			(c).begin(),(c).end()
#define tr(c,i) 		for(typeof(c.begin()) i = c.begin(); i != c.end(); i++)
#define present(c,x) 	((c).find(x) != (c).end())
#define cpresent(c,x) 	(find(all(c),x) != (c).end()) 
#define INF				(int(1e9))
#define INFL			(int(1e18))
#define EPS				1e-12
const int inf = 100010;
const int MOD = 1000000007;
const double pi=acos(-1.0);


#define iabs(x)  ((x) > 0 ? (x) : -(x))

#define clear1(A, X, SIZE) memset(A, X, sizeof(A[0]) * (SIZE))
#define clearall(A, X) memset(A, X, sizeof(A))
#define memcopy1(A , X, SIZE) memcpy(A , X ,sizeof(X[0])*(SIZE))
#define memcopyall(A, X) memcpy(A , X ,sizeof(X))
#define max( x, y )  ( ((x) > (y)) ? (x) : (y) )

#define rep(i,a)	for(i=0;i<a;i++)
#define FOR(i,a,b)	for(i=a;i<b;i++)

int gcd(int a,int b) {return (b==0?a:gcd(b,a%b));}
int lcm(int a,int b) {return (a*(b/gcd(a,b)));}
int fx[]={0,0,1,-1};
int fy[]={-1,1,0,0};


int main() {
	ios_base::sync_with_stdio(0);
	int i=0,j;
	int n,t,cnt=0;
	freopen("D-small-attempt1.in","r",stdin);
	freopen("D-small.out","w",stdout);
	
	cin>>t;
	int x,r,c;
	FOR(i,1,t+1) {
		cin>>x>>r>>c;
		
		if(x==1) {
			cout<<"Case #"<<i<<": GABRIEL\n";
		}
		else if(x == 2) {
			
			if((r*c)&1 ) {
				cout<<"Case #"<<i<<": RICHARD\n";
			}
			else {
				cout<<"Case #"<<i<<": GABRIEL\n";
			}
		}
		
		else if(x == 3) {
			
			if(r*c <= x) {		//3X1
				cout<<"Case #"<<i<<": RICHARD\n";
			}
			else {
				if(r == 3 || c == 3)	//3x3,3x2,3x4
					cout<<"Case #"<<i<<": GABRIEL\n";
				else {					//2x2,2x4
					cout<<"Case #"<<i<<": RICHARD\n";
				}
			}
		
		}
		
		else {	//x=4
			
			if((r*c)%x || r*c == x || r*c == 2*x) {
				cout<<"Case #"<<i<<": RICHARD\n";
			}
			else {
				cout<<"Case #"<<i<<": GABRIEL\n";
			}
		}
		
	}
	return 0;
}	
