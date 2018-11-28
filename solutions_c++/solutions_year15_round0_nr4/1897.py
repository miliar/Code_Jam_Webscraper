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
	//freopen("in.in", "r", stdin);
	freopen("D-small-attempt1.in", "r", stdin);
	freopen("D-small.out", "w", stdout);
#endif
	int t, x,r,c, cc=1;
	cin >> t;
	while(t--){
		bool ans = false;
		cin >> x >> r >> c;

		if(x<3){
			ans = (r*c % x) == 0;
		}else if(x==3){
			ans = (r*c % x) == 0 && (r>1 && c>1);
		}else if(x==4){
			ans = (r>2 && c==4) || (c>2 && r==4);	
		}

		if(ans)
			printf("Case #%d: GABRIEL\n", cc++);
		else
			printf("Case #%d: RICHARD\n", cc++);
			
	}
	return 0;
}