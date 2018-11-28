#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
#include<cctype>
#include<cstdlib>
#include<algorithm>
#include<bitset>
#include<cstdio>
#include<cstring>
#include<string>
#include<cctype>
#include<cstdlib>
#include<algorithm>
#include<bitset>
#include<vector>
#include<list>
#include<deque>
#include<queue>
#include<map>
#include<set>
#include<stack>
#include<cmath>
#include<sstream>
#include<fstream>
#include<iomanip>
#include<ctime>
#include<complex>
#include<functional>
#include<climits>
#include<cassert>
#include<iterator>
using namespace std;


int t;

set<int> s;


int main(){
	cin >> t;
	int tt = 0;
	while (t--){
		tt++;
		long long int n;
		scanf("%lld", &n);
		long long int tmp = n;
		printf("Case #%d: ", tt);
		int T = 100;
		s.clear();
		bool ok = false;
		while (T--){
			long long int k = n;
			while (k){
				s.insert(k % 10LL);
				k /= 10LL;
			}
			if (s.size() == 10){
				ok = true;
				break;
			}
			else{
				n += tmp;
			}
		}
		if (ok == false){
			puts("INSOMNIA");
			continue;
		}
		printf("%lld\n", n);
	}
	return 0;
}