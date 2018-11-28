#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <climits>
#include <vector>
#include <iterator>
#include <set>
#include <bitset>
#include <ctime>
#include <iomanip>
#include <map>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	int t;
	cin>>t;
	for(int test = 1; test <= t; test++) {
		int a, b, k, ans = 0;
		cin>>a>>b>>k;
		for(int i=0; i<a; i++) {
			for(int j=0; j<b; j++) {
				if((i&j) < k)
					ans++;
			}
		}
		cout<<"Case #"<<test<<": "<<ans<<"\n";
	}
	return 0;
}