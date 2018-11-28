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


int a , b , c , d[N] , n , m;
string s;

int main()
{
	freopen("pancake.in" , "r" , stdin);
	freopen("pancake.out" , "w",  stdout);
	
	scanf("%d" , &m);
	
	for(int k = 1 ; k <= m ; k++)
	{
		cin >> s;
		n = sz(s);
		char sf = s[0];
		
		a = (s[n-1] == '-' ? 1 : 0) , b = 0;
		
		for(int i = 1 ; i < n ; i++)
			if(s[i] != sf)	sf = s[i] , a++;
		
		reverse(all(s));
		
		for(int i = 0 ; i < n ; i++)	s[i] = (s[i] == '-' ? '+' : '-');
		b += (s[n-1] == '-' ? 1 : 0) + 1;
		
		sf = s[0];
		for(int i = 1 ; i < n ; i++)
			if(s[i] != sf)	sf = s[i] , b++;
		
		printf("Case #%d: " , k);
		printf("%d\n" , min(a , b));
	}
	
	return 0;
}
