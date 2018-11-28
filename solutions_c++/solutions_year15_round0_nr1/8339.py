/////////////////////////////////////////////////   IN THE NAME OF GO
#include <bits/stdc++.h>

using namespace std;

//#pragma comment(linker, "/STACK:1024000000,1024000000")

#define     For(i,a,b)        for (int i=(int)a; i<(int)b; i++)
#define     Rep(i,a)          for (int i=0; i<(int)a; i++)
#define     ALL(v)            (v).begin(),(v).end()
#define     Set(a,x)          memset((a),(x),sizeof(a))
#define     EXIST(a,b)        find(ALL(a),(b))!=(a).end()
#define     Sort(x)           sort(ALL(x))
#define     UNIQUE(v)         Sort(v); (v).resize(unique(ALL(v)) - (v).begin())
#define     SF                scanf
#define     PF                printf
#define     timestamp(x)      printf("Time : %.3lf s.\n", clock()*1.0/CLOCKS_PER_SEC)
#define     INF               1e11
#define     pii               pair < int , int >
#define     MP                make_pair
#define     MOD               1000000007
#define     EPS               1e-11
#define     ll                long long
#define     MAXN              100000+10
#define     Dbug              cout<<""
#define     PI                3.1415926535897932384626433
//int month[]={0,31,28,31,30,31,30,31,31,30,31,30,31};

bool check ( int x , vector < int > &t ){
	int sum = x + t[0] ;
	For ( i , 1 , t.size() ){
		if ( i <= sum ){
			sum += t[i] ;
			continue ;
		}
		return 0 ;
	}
	return 1 ;
}

int main()
{
    ios::sync_with_stdio(false);
#ifndef ONLINE_JUDGE
    freopen ( "input.txt" , "r" , stdin ) ;
    freopen ( "output.txt" , "w" , stdout ) ;
#endif
    int t , tc = 1 ;
    cin >> t ;
    while ( t-- ){
    	int a , ans = 0 ;
    	string per ;
    	vector < int > num ;
    	cin >> a >> per ;
    	Rep ( i , per.size() ) num.push_back( (int)per[i]-'0' ) ;
    	int f = 0 , l = 1111 ;
    	while ( f < l ){
    		int mid = ( f + l ) / 2 ;
    		if ( check ( mid , num ) ){
    			ans = mid ;
    			l = mid ;
    		}
    		else f = mid + 1 ;
    	}

    	cout << "Case #" << tc++ << ": " << ans << endl ;
    }
    return 0;
}
