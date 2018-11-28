#include <cstring>
#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
using namespace std;

int main(){
	int T;
	cin >> T;
	for(int t=1; t<=T; t++){
		int Smax;
		cin >> Smax;
		string s;
		cin >> s;
		int n = 0;
		int res = 0;
		for(int i=0; i<=Smax; i++){
			int x = s[i]-'0';
			if(n < i){
				res += i-n;
				n += i-n;
			}
			n += x;
		}
		printf("Case #%d: %d\n", t, res);
	}
	
	return 0;
}
