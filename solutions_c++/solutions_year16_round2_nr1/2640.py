#include<bits/stdc++.h>

#define ff first
#define ss second
#define pb push_back
#define mp make_pair
#define len(s) s.length()
#define forp(i,a,b) for( i=a;i<=b;i++)
#define rep(i,n)    for( i=0;i<n;i++)
#define ren(i,n)    for( i=n-1;i>=0;i--)
#define forn(i,a,b) for( i=a;i>=b;i--)
#define all(v) v.begin(),v.end()
#define b(v) v.begin()
#define e(v) v.end()
#define mem(n,m) memset(n,m,sizeof(n))
#define lb lower_bound
#define ub upper_bound
#define pii pair<int,int>
#define pll pair<long long,long long>
#define vii vector<int>
#define vll vector<long long>
#define gl(cin,s)  getline(cin,s);
#define bitc(n) __builtin_popcountll(n)
#define present(s,x) (s.find(x) != s.end()) 
#define cpresent(s,x) (find(all(s),x) != s.end()) 
#define tr(container, it) for(__typeof(container.begin()) it = container.begin(); it != container.end(); it++) 

#define boost ios_base::sync_with_stdio(0)
#define MOD 1000000007
#define EPSILON 1e-9
#define PI 3.14159265358979323846
#define SIZE 100000

typedef long long  ll;
typedef unsigned long long ull;
typedef long double  ldo;
typedef double  db ;
using namespace std;
int main()
{  	
	freopen("route.in","r",stdin);
	freopen("route.out","w",stdout);
	boost;
	//cin.tie(0);
	// cout<<"Case #"<<i<<": 2"<<endl;
	int t;
	cin>>t;
	for(int tt=1;tt<=t;tt++){
		string s;
		int c1=0,c2=0,c3=0,c4=0,c5=0,c6=0,c7=0,c8=0,c9=0,c10=0;
		cin>>s;
		int ans[10]={0};
		for(int i=0;i<len(s);i++){
			if(s[i]=='X')
			c1++;
			if(s[i]=='W')
			c2++;
			if(s[i]=='Z')
			c3++;
			if(s[i]=='U')
			c4++;
			if(s[i]=='F')
			c5++;
			if(s[i]=='G')
			c6++;
			if(s[i]=='S')
			c7++;
			if(s[i]=='H')
			c8++;
			if(s[i]=='I')
			c9++;
			if(s[i]=='O')
			c10++;
		}
		ans[6]=c1;
		ans[2]=c2;
		ans[4]=c4;
		ans[5]=c5-c4;
		ans[0]=c3;
		ans[8]=c6;
		ans[3]=c8-c6;
		ans[9]=c9-c1-c5+c4-c6;
		ans[7]=c7-c1;
		ans[1]=c10-c4-c2-c3;
		cout<<"Case #"<<tt<<": ";
		for(int i=0;i<10;i++){
			for(int j=0;j<ans[i];j++)
			cout<<i;
		}
		cout<<endl;
	}
	return 0;
}
