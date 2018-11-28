#include <iostream>
#include <stdio.h>
#include <math.h>
#include <list>
#include <queue>
#include <vector>
#include <functional>
#include <stack>
#include <utility> 
#include <stdlib.h>
#include <map>
#include <string.h>
#include <algorithm>
typedef long long int ll;
#define SWAP(a, b) (((a) ^= (b)), ((b) ^= (a)), ((a) ^= (b)))
#define CLR(a) memset(a, 0, sizeof(a))
using namespace std;
int main() {
	freopen ("output.txt","w",stdout);
	freopen ("input.in","r",stdin);
	ll t, i, j, a, b, k, ans;
	cin>>t;
	for(ll lol = 1; lol <= t; ++lol) {
		cin>>a>>b>>k;
		ans = 0;
		for(i=0;i<a;++i) {
			for(j=0;j<b;++j) {
				ll xx = (i & j);
				if((xx) < k ) { ++ans; }
			}
		}
		cout<<"Case #"<<lol<<": "<<ans<<endl;
	}
	return 0;
}