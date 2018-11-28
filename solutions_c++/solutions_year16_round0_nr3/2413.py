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


ll a , b ,p , c , ans , d[50] , n , m , rr[12] , J , t;
vector <ll> E[1000];

ll calc(int y)
{
	a = 0 , b = 1;
	
	for(int i = 1 ; i <= n ; i++)
		a += b*d[i] , b *= y;
	
	for(int i = 2 ; i <= sqrt(a) ; i++)
		if(a % i == 0)
			return i;
	
	return 0;
}

void f(int x)
{
	if(x == n)
	{
		bool foo = 0;
		memset(rr , 0 , sizeof rr);
		c = 0 , p = 1;
		
		for(int i = 1 ; i <= n ; i++)
			c += p*d[i] , p *= 10;
		
		for(int i = 2 ; i <= 10 ; i++)
		{
			rr[i] = calc(i);
			if(!rr[i])	foo = 1;
		}
		
		if(!foo)
		{
			++ans;
			E[ans].pb(c);
			for(int i = 2 ; i <= 10 ; i++)
				E[ans].pb(rr[i]);
		}
		
		return;
	}
	
	if(ans == J)	return;
	
	for(int i = 0 ; i < 2 ; i++)
	{
		if(ans == J)	return;
		d[x] = i;
		f(x+1);
	}
}


int main()
{
	freopen("jamcoin.in" , "r" , stdin);
	freopen("jamcoin.out" , "w",  stdout);
	
	scanf("%lld" , &t);
	scanf("%lld%lld" , &n ,&J);
	
	d[1] = d[n] = 1;
	f(2);
	
	puts("Case #1:");
	for(int i = 1 ; i <= J ; i++)
	{
		for(auto j : E[i])
			cout << j << " ";
		puts("");
	}
	
	return 0;
}
