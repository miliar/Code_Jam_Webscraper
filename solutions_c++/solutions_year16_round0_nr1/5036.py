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
string convertstring(ll n) { 
	if(n == 0 ) return "0";
 stringstream ss; ss << n ; return ss.str(); }
#define MOD 1000000007
#define MAX 1000000010
#define all(v) v.begin(),v.end()
#define mp make_pair
#define pb push_back
#define f first
#define s second
typedef pair<int,int> pp;
int vis[201]; 
int main()
{
	//   freopen("C:\\Users\\screw_1011\\Desktop\\input.txt","r",stdin);
	  //  freopen("C:\\Users\\screw_1011\\Desktop\\output.txt","w",stdout);
	int tt , i ;	
	ll n ; 
	cin >> tt;
	for(int ttt = 1;ttt<=tt;ttt++ ) {
		printf("Case #%d: ", ttt);
		mem(vis, 0 ); 
		SLL(n); 
		ll ans = n ;
		string t1 = convertstring(n);
		for(int j =0  ; j < t1.size(); j++){
			if(!vis[t1[j] -'0']) vis[t1[j] - '0'] = 1; 
		} 
		ll n1; 
		for(i = 2; i <= 1000000 ;i++)
		{
			n1 = i * n ; 
			t1 = convertstring(n1);
			for(int j =0 ;j < t1.size() ;j++)
			{
				if(!vis[t1[j] -'0'])
				{
					ans = n1 ; 
					vis[t1[j] - '0'] = 1;
				} 
			} 
			int ok=1;
			for(int j =0 ; j < 10 ; j++){ if(!vis[j]) ok = 0 ; } 
			if(ok) break; 
		}
		bool ok =1;
		fl(i,0,10){
			if(!vis[i]) ok = 0 ; 
		}
		if( !ok ) printf("INSOMNIA\n");
		else printf("%lld\n", ans);
	}
	return 0 ;
}