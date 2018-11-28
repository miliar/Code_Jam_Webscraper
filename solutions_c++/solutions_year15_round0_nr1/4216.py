#include <cstdio>
#include <iostream>
#include <cmath>
#include <vector>
#include <stack>
#include <queue>
#include <algorithm>
#include <string.h>
#include <cmath>
#include <sstream>
#include <map>
#include <bitset>
#include <cstdlib>
#include <cstring>
#include <set>
#include <ctype.h>
#include <string>
using namespace std;

typedef long long ll;
typedef vector<int> vi;


int main(){
#ifndef ONLINE_JUDGE
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
#endif
	int t, smax, ans = 0, stand=0, cc=1;
	string aud;
	cin >> t;
	while(t--){
		cin >> smax >> aud;
		ans = 0;
		stand = 0;
		for (int i = 0; i < smax+1; i++){
			if(i>stand && aud[i]-'0' > 0){
				ans += (i-stand);
				stand += (i-stand);
			}
			stand += aud[i]-'0';
		}
		printf("Case #%d: %d\n", cc++, ans);
	}
	return 0;
}