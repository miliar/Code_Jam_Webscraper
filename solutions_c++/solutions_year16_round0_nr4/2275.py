//~  Inshaallah
/*
ID: omarmuh1
PROG: test
LANG: C++
*/
#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>

using namespace std;
using namespace __gnu_pbds;

#define ll long long
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define pp pop_back
#define pii pair<int ,int>
#define pll pair<ll , ll>
#define mid(x , y)	(x+y)/2
#define sz(x) int(x.size())
#define db		cout << "****" << endl;
#define all(x) 	x.begin() , x.end()
#define lgn 	19
#define N 		100007
#define INF 	1000000007
#define LLINF 	1000000000000000009
#define tr(i, c) for(__typeof((c).begin()) i = (c).begin(); i!=(c).end(); i++)
#define Help_me  ios_base::sync_with_stdio(false);

typedef tree<int,null_type,less<int>,rb_tree_tag,tree_order_statistics_node_update> omar;

template<class T> bool umin(T& a, T b) { if(a > b){ a = b;return 1;}return 0;}
template<class T> bool umax(T& a, T b) { if(a < b){ a = b;return 1;}return 0;}


ll a , b , c , d[N] , n , m , t , K , C , S;

int main()
{
	freopen("frac.in" , "r" , stdin);
	freopen("frac.out" , "w",  stdout);
	
	scanf("%lld" , &t);
	
	for(ll j = 1 ; j <= t ; j++)
	{
		a = 1;
		scanf("%lld%lld%lld" , &K , &C , &S);
		
		printf("Case #%lld: " , j);
		
		for(ll i = 1 ; i < S ; i++)	printf("%lld " , i);
		for(ll i = 1 ; i <= C ; i++)	a *= K;
		printf("%lld\n" , a);
	}
	
	return 0;
}
