#include <bits/stdc++.h>

using namespace std;

#define LL long long
#define ULL unsigned long long


#define VI vector < int >
#define PB push_back


#define CLR(a,x) memset(a,x,sizeof(a))


#define tr(container , it) for(typeof(container.begin()) it=container.begin() ; it!=container.end() ; it++)
#define FOR(i,a,b) for(i=a;i<b;i++)


#define PII pair < int , int >
#define MP make_pair


#define what_is(x) cout << #x << " is " << (x) << endl
#define s( x )  scanf("%d", &(x) )
#define sll( x ) scanf("%lld", &(x) )


#define BIT(n) (1<<(n))
#define AND(a,b) ((a) & (b))
#define OR(a,b) ((a) | (b))
#define XOR(a,b) ((a) ^ (b))
#define sqr(x) ((x) * (x))


#define clear_buffer(c) while ( (c = getchar()) != '\n' && c != EOF ) { }

#define epsilon 1e-6
#define INF 100000000000000
#define MOD 1000000007

int gcd(int a, int b) { return b == 0 ? a : gcd(b, a%b); }
int abs( int k) { return (k>0) ? (k) : (k*(-1)); }


int main()
{
	
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t, mx, ans, tot, cs=0; 
	string s;

	cin >> t;
	while (t--) {
		cs++;

		cin >> mx;
		cin >> s;


		ans=tot=0;
		tot += (s[0] - '0');

		for (int i = 1; i < s.length(); ++i) {
			if (tot < i) ans += i-tot, tot=i;
			tot += (s[i]-'0');
		}

		cout << "Case #" << cs << ": " << ans << endl;
	}

	return 0;
}
