#include<bits/stdc++.h>
using namespace std;
#define w(t) while(t--)
#define ll long long
#define S(x) scanf("%d",&x)
#define SLL(x) scanf("%lld",&x)
#define P(x) printf("%d\n",x)
#define fl(i , a, b) for(i = (int)a; i<(int)b; i++)
#define mem(a , value) memset(a , value , sizeof(a))
#define tr(c, itr) for(itr = (c).begin(); itr != (c).end(); itr++)
string convertstring(ll n) { stringstream ss; ss << n ; return ss.str(); }
#define MOD 1000000007
#define MAX 1000000010
#define all(v) v.begin(),v.end()
#define mp make_pair
#define pb push_back
#define f first
#define s second
typedef pair<int,int> pp;
string s;
std::vector<char> v;
int main()
{
	int t, i ;
	cin >> t;
	for(int tt = 1 ; tt<=t;tt++)
	{
		int p= 0;
		printf("Case #%d: ", tt );
		cin >> s;
		v.clear();
		v.pb(s[0]); 
		fl(i, 1 , s.size()){
			if(s[i] == s[i-1]) continue;
			v.pb(s[i]);
		}	
		fl(i , 0, v.size()) if(v[i] == '-') p++;
		if(v[0] == '+') p = 2*p;
		else p = 2*p-1 ; 
		printf("%d\n", p);
	}
	return 0 ;
}