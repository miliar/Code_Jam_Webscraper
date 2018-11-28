#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <algorithm>
using namespace std;
void main(){
#ifdef TRAINING
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif
	int T, n;
	cin >> T;
	string s;
	for(int t = 1; t<=T; ++t){
		cin >> n >> s;
		int result = 0, count = 0, need = 0;
		for (int i = 0; i <= n; ++i){
			need = max(i - count,0);
			result += need;
			count += s[i] - '0' + need;
		}
		printf("Case #%d: %d\n", t, result);
	}
	
}