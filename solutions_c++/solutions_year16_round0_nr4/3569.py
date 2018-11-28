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
int main()
{
	//   freopen("C:\\Users\\screw_1011\\Desktop\\input.txt","r",stdin);
	  //  freopen("C:\\Users\\screw_1011\\Desktop\\output.txt","w",stdout);
	int t , k , c , s; 
	cin >> t;
	for(int ii=1; ii <= t;ii++){ printf("Case #%d: ", ii ); cin >> k >> c >> s; for(int i =1; i<=k;i++) printf("%d ", i); printf("\n"); }
	return 0 ;
}