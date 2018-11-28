#include <set>
#include <map>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <cctype>
#include <cstdio>
#include <string>
#include <vector>
#include <cassert>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <iostream>
#include <algorithm>

using namespace std;

#define pb push_back
#define mp make_pair
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef pair<long long,long long> ll;
#define sz(a) int((a).size())
#define all(a) (a).begin(),(a).end()
#define sor(a) sort((a).begin(),(a).end())
#define FOR(a,b,c) for(int (a)=(b);(a)<(c);(a)++)

long long gcd(long long a,long long b){
	if( b == 0 ) return a;
	return gcd(b,a%b);
}

int main()
{
	freopen("p1_large.in","r",stdin);
	freopen("p1_large.out","w",stdout);
	
	int tc = 1;
	
	vector<long long> twos;
	long long tmp = 1;
	for(int i=0;i<40;i++){
		twos.pb(tmp);
		tmp *= 2LL;
	}
	
	int t;
	cin >> t;

	while(t--){
		cout << "Case #" << tc++ << ": ";
		string x;
		cin >> x;
		long long a=0,b=0;
		int k=0;
		while(x[k] != '/'){
			a *= 10LL;
			a += (long long)x[k] - '0';
			k++;
		}
		k++;
		while(k < sz(x) ){
			b *= 10LL;
			b += (long long)x[k] - '0';
			k++;
		}
		
		long long gg = gcd(a,b);
		a /= gg;
		b /= gg;
		
		k = 0;
		while(k<40 && twos[k]%b != 0){
			k++;
		}
		
		if( k == 40 ){
			cout << "impossible" << endl;
			continue;
		}

		a*= (twos[k]/b);
		b= twos[k];
		
		int base = floor(log(a)/log(2));
		long long val = 1LL << base;
		int ans = 0;
		while(val != b){
			val *= 2LL;
			ans++;
		}
		cout << ans << endl;
	}
}
