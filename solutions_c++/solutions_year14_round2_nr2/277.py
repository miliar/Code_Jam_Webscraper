#include<iostream>
#include<cstring>
#include<map>
#include<vector>
#include<string>
#include<set>
#include<queue>
#include<algorithm>
#include<cmath>

using namespace std;
int a[40] ;
int b[40];
int k[40];
long long dp[40][2][2][2];
int max_a , max_b , max_k;
long long f ( int pos , int aa , int bb , int kk ){
	//cerr << "+" << pos << " " << aa << " " << bb << " " << kk  << endl;
	if ( pos == -1 ){
		return aa==0&&bb==0&&kk==0 ;
	}
	long long & ret = dp [pos][aa][bb][kk];
	if ( ret != -1 ) return ret;
	ret = 0 ;
	
	for ( int i=0 ; i<2 ; i++ )
		for ( int j=0 ; j<2 ; j++ ){
			int temp = (i&j);
			if ( temp > k[pos] && kk==1 )
				continue ;
			if ( i > a[pos] && aa == 1 )
				continue ;
			if ( j > b[pos] && bb == 1 )
				continue ;
			int naa = aa, nbb = bb, nkk = kk;
			if ( i < a[pos] ) naa = 0 ;
			if ( j < b[pos] ) nbb = 0 ;
			if ( temp < k[pos] ) nkk = 0 ;
			ret += f(pos-1,naa,nbb,nkk);
		}
	//cerr << "-" << pos << " " << aa << " " << bb << " " << kk  << endl;
	//cerr << pos << " " << aa << " " << bb << " " << kk << " " << ret << endl;
	return ret;
}
int main(){
	//cout << (1<<30) << endl;
	int tc;
	cin >> tc;
	
	for ( int test_case=1 ; test_case<=tc ; test_case++ ){
		int A , B , K ;
		cin >> A >>  B >> K ;
		memset(a,0,sizeof a);
		memset(b,0,sizeof b);
		memset(k,0,sizeof k);
		max_a = -1, max_b = -1 , max_k = -1 ;
		for ( int i=0 ; i<=30 ; i++ ){
			if ( A&(1<<i) ){
				a[i] = 1;
				max_a = i;
			}
			if ( B&(1<<i) ){
				b[i] = 1;
				max_b = i;
			}
			if ( K&(1<<i) ){
				k[i] = 1;
				max_k = i ;
			}
		}
		//for ( int i=0 ; i<30 ; i++ )
		//	cerr << a[i] << " " << b[i] << " " << k[i] << endl;
		memset(dp,-1,sizeof dp);
		long long ret = f(30,1,1,1);
		cout << "Case #" << test_case << ": " << ret << endl;
	}
}
