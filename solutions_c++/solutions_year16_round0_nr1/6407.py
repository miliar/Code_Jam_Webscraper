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
#define rr 		freopen("A-large.in", "r", stdin)
#define wr 		freopen("outputlarge.txt", "w", stdout)

#define MOD 	1000000007
#define INF 	1LL<<57LL
#define MAX 	1000000
#define pi 		M_PI
#define ESP 	(1e-9)

#define tr(container, it) 	for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define sd(n) 		scanf("%d",&n)
#define sld(n) 		scanf("%ld",&n)
#define slld(n) 	scanf("%lld",&n)
#define pfd(n) 		printf("%d",n)
#define pfld(n) 	printf("%ld",n)
#define pflld(n) 	printf("%lld",n)

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

int a[10];

int f(llu x)
{
	int r,i;
	while(x)
	{
		r=x%10;
		a[r]=1;
		x/=10;
	}
	for(i=0;i<10;++i)
	if(a[i]==0)
	return 1;//if any  no is set 0
	
	return 0;//all are found;
} 

int main()
{
    rr;
    wr;
	llu ans,n,i;int ok,cc=1;
    IN
    {
		cin >> n;
		if(n==0)
		{
		cout << "Case #" << cc++ << ": INSOMNIA\n";
		continue;
		}
		mem(a,0);
		//f(n);
		ok=i=1;
		while(ok)
		{
			ans=i*n;
			ok=f(ans);
			i++;
			if(!ok)break;
		}
		cout << "Case #" << cc++ << ": " << ans <<"\n";
	}
    return 0;    
}
