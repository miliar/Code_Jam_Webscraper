#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cctype>
#include<algorithm>
#include<queue>
#include<stack>
#include<vector>
#include<string>
#include<cstring>
#include<ctime>
#include<map>
#include<set>
#include<list>
#include<deque>
#include<iterator>
#include<utility>
#include<climits>
#include<iomanip>
 
#define LL long long 
#define sn(n) scanf("%d",&n) ;
#define slld(n) scanf("%lld",&n) ;
#define sc(n) scanf(" %c",&n) ;
#define ss(n) scanf(" %s",n) ;
#define all(n) n.begin() , n.end()
#define pb push_back
#define vi vector<int> 
#define vLL vector<LL >
#define vvi vector<vi >
#define vvLL vector<vLL >
#define vc vector<char>
#define vvc vector<vc >
#define vb vector<bool>
#define vvb vector<vb > 
#define pii pair<int , int> 
#define fi first 
#define se second
#define mp make_pair
#define vpii vector<pii >
#define vvpii vector<vpii >
#define rep(i , a , b) for(int (i) = (a) ; (i) < (b) ; ++(i))
#define rev(i , a , b) for(int (i) = (a)-1 ; (i) >= (b) ; --(i))
#define tr(container , it) for(typeof(container.begin()) it = container.begin() ; it != container.end() ; ++it)
#define mii map<int , int>
#define msi map<string , int>
#define mci map<char , int>
#define INF (1<<31)
#define fast_io ios::sync_with_stdio(0) ; cin.tie(0) ; 
#define max_array 100001
#define in() freopen("input.txt" , "r" , stdin) ;
#define out() freopen("output.txt" , "w" , stdout) ;
#define MOD 1000000007
#define max_val 10000000
#define debug() cout << "HI" << endl ;
 
using namespace std ;

int main()
{
	#ifndef ONLINE_JUDGE
	    in() ;
	    out() ;
	#endif
	fast_io ;
	int t, test = 1 ;
	cin >> t ;
	while(t--)
	{
		int max_s ;
		cin >> max_s ;
		string s ;
		int cnt = 0 ;
		cin >> s ;
		int ans = 0 ;
		rep(i, 0, s.size())
		{
			cnt += s[i]-'0' ;
			if(cnt <= i)
			{
				++ans ;		
				++cnt ;
			}
		}
		cout << "Case #" << test << ": " << ans << endl ;
		++test ;
	}

	return 0 ;
}