#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std ;

// P-R-S

#define P4 pair<pair<int,int>,pair<int,string>>
#define MP(a,b) make_pair(a,b)
#define MP4(a,b,c,d) MP(MP(a,b),MP(c,d))
#define itemL first
#define itemR second
#define item1 itemL.itemL
#define item2 itemL.itemR
#define item3 itemR.itemL
#define item4 itemR.itemR

int N , R , P , S ;
P4 DP[15][3] ;

void Solve() {
	DP[0][0] = MP4(1,0,0,"P") ;
	DP[0][1] = MP4(0,1,0,"R") ;
	DP[0][2] = MP4(0,0,1,"S") ;
	
	for ( int i = 1 ; i <= N ; i ++ ) {
		for ( int j = 0 ; j < 3 ; j ++ ) {
			int k = (j+1) % 3 ;
			P4 tmp = MP4( DP[i-1][j].item1 + DP[i-1][k].item1 ,
			              DP[i-1][j].item2 + DP[i-1][k].item2 ,
						  DP[i-1][j].item3 + DP[i-1][k].item3 ,
						  "" ) ;
			string s1 = DP[i-1][j].item4 ;
			string s2 = DP[i-1][k].item4 ;
			if ( s1 <= s2 ) tmp.item4 = s1+s2 ;
			else            tmp.item4 = s2+s1 ;
			DP[i][j] = tmp ;
			
			//cout << i << "," << j << " : " << DP[i][j].item1 << "," << DP[i][j].item2 << "," << DP[i][j].item3 << "," << DP[i][j].item4 << "\n" ;
		}
	}
	
	string ans = "IMPOSSIBLE" ;
	for ( int j = 0 ; j < 3 ; j ++ )
		if ( DP[N][j].item1 == P && DP[N][j].item2 == R && DP[N][j].item3 == S ) {
			if ( ans == "IMPOSSIBLE" || DP[N][j].item4 < ans )
				ans = DP[N][j].item4 ;
		}
	cout << ans << "\n" ;
}

int main() {
	//freopen("A-small-attempt0.in" , "r" , stdin) ;
	//freopen("A-small-attempt0.out", "w" ,stdout) ;
	
	int Test ; cin >> Test ;
	for ( int i = 1 ; i <= Test ; i ++ ) {
		cin >> N >> R >> P >> S ;
		cout << "Case #" << i << ": " ;
		Solve() ;
	}
}