#include<iostream>
#include<cstring>
#include<string>
#include<memory>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<cmath>
using namespace std;
const int max_n = 700 + 10 ;
int cnt[max_n];
int main(){
	int tc;
	cin >> tc;
	for ( int test_case = 1 ; test_case <= tc ; test_case ++ ){
		int n , disc ;
		cin >> n >> disc ;
		memset(cnt,0,sizeof cnt);
		int max_value = -10000 ;
		for ( int i=0 ; i<n ;i++ ){
			int a;
			cin >> a;
			max_value = max ( max_value , a ) ;
			cnt[a] ++ ;
		}
		int answer = 0;
		for ( int i=0 ; i<=max_value ; i++ )
			while ( cnt[i] > 0){
				cnt[i] -- ;
				int best = -1 , max_size ;
				for ( int j=0 ; j<=max_value ; j++ ){
					if ( cnt[j] == 0 ) continue ;
					if ( j + i <= disc ){
						if ( best == -1 ){
							best = j ;
							max_size = i + j;
						}
						else if ( i + j > max_size ){
							best = j;
							max_size = i + j;
						}
					}
				}
				if ( best != -1 ) cnt[best]--;
				answer ++ ;
			}
		cout << "Case #" << test_case << ": " << answer << endl;
	}
	return 0 ;
}
