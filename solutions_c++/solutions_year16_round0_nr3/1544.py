#include <bits/stdc++.h>
#include <tr1/unordered_set>

using namespace std;
using namespace tr1;

typedef long long int64;
typedef unsigned long long uint64;

int n, j;

int64 _sieve_size;
bitset < 20000012 > bs;
unordered_set < int64 >  primes;
vector < pair < int64, vector < int64 > > > ans;

void sieve( int64 upperbound ){
    _sieve_size = upperbound + 1;
    bs[0] = bs[1] = 1;
    for( int64 i = 2; i <= _sieve_size; i++ ){
        if( !bs[i] ){
            for( int64 j = i * i; j <= _sieve_size; j += i ) bs[j] = 1;
            primes.insert(i);
        }
    }
}

int64 getDiv( int64 val ){
	int64 maxP = (int64) sqrtl(val) + 2;
	for(int64 i = 2; i <= maxP; i++ ){ 
		if ( val % i == 0LL ) { 
			return i;
		}
	}
	return -1;
}

long long converteBase( int64 val, int64 base ){
	int64 ans = 0LL;
	string str = "";
	while( val ){
		str += ((val & 1) ? ("1") : ("0"));
		val >>= 1LL;
	}
	reverse(str.begin(), str.end());
	for( int i = 0; i < str.size(); i++ ){
		ans = ans * base + (str[i] - '0');
	}
	return ans;
}

void solve( int64 val ){
	vector < int64 > bases;
	
	for( int i = 2; i <= 10; i++ ){
		int64 lo = converteBase(val, i);
		int64 hi = converteBase(lo, 10);
		bases.push_back(lo);
		if( primes.count(hi) ) return;
	}

	vector < int64 > divs;
	for( int i = 0; i < bases.size(); i++ ){
		int64 ret = getDiv( bases[i] );
		if( ret == -1 ) return;
		divs.push_back(ret);
	}

	ans.push_back(make_pair(val, divs));
}



int main(){
	ios::sync_with_stdio(false);
	int t,  k = 1;
	cin >> t;
	sieve(20000000);
	while( t-- ){
		cin >> n >> j;

		for( int64 i = 0; i < (1LL<< (n-2)); i++ ){
			solve(((i|(1<<(n-2)))<<1LL)|1);
			if( ans.size() >= j ) break;
		}

		cout << "Case #" << k++ << ":\n";
		for( int i = 0; i < j; i++ ){
			int64 val = ans[i].first;
			string str = "";
			while( val ){
				str += ((val & 1) ? ("1") : ("0"));
				val >>= 1LL;
			}
			reverse(str.begin(), str.end());
			cout << str;
			for( int z = 0; z < ans[i].second.size(); z++ ){
				cout << " " << ans[i].second[z];
			}
			cout << '\n';
		}
	}
	return 0;
}