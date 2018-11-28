#include <bits/stdc++.h>

using namespace std;
	
typedef long long unsigned llu;
typedef long long lld;
typedef long ld;

#define vi 		vector < int >
#define vld 	vector < ld >
#define vlld 	vector < lld >
#define vllu 	vector < llu >
#define pii 	pair <int, int>
#define plld 	pair<lld, lld>
#define vpii 	vector< pii >
#define vplld 	vector< plld >

#define gc 		getchar
#define pc 		putchar
#define rr 		freopen("B-large.in", "r", stdin)
#define wr 		freopen("outputB22.txt", "w", stdout)

#define MOD 	1000000007
#define INF 	1LL<<57LL
#define MAX 	1000000
#define pi 		M_PI
#define ESP 	(1e-9)

#define ff 			first
#define ss 			second
#define clr 		clear()
#define square(x) ((x)*(x))
#define pb 			push_back
#define mp 			make_pair
#define gcd(a,b)  	__gcd(a,b)
#define sz(a) 		((int)(a.size()))
#define len(a) 		((int)a.length())
#define all(vi) 	vi.begin(), vi.end()
#define mem(i,n) 	memset(i,n,sizeof(i))
#define IOS 		ios_base::sync_with_stdio(false); cin.tie(NULL);
#define IN          int t; cin >> t; while(t--)

char s[1005];
int l;
int lasti()
{
	for(int i=l-1;i>=0;--i)
		if(s[i]=='-')
		return i;
		
		return 0;
}
void flip(int p)
{
	for(int i=0;i<=p;++i)
		{
			if(s[i]=='-')s[i]='+';
			else if(s[i]=='+')s[i]='-';
		}
}
int strchk()
{
	for(int i=0;i<l;++i)
		{
			if(s[i]=='-')return 0;
		}
		return 1;
}
int main()
{
	rr;
	wr;
    int ans,cc=1;
    
    IN
    {
		scanf("%s",s);
		l=strlen(s);
		ans=0;
		while(!strchk())
		{
			flip(lasti());
			ans++;
		}
		cout << "Case #" << cc++ << ": " << ans <<"\n";
	}
    return 0;    
}
