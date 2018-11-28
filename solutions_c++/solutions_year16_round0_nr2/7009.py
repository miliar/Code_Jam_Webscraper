#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
char str[200] , res[120];
int main()
{
	//freopen("c.in" , "r" , stdin);
	//freopen("hhh.out" , "w" , stdout);
	int t;
	cin >> t;
	for(int ca = 1 ; ca <= t ; ca++) {
		cin >> str;
		int len = strlen(str) , s = 0 , ans = 0;
		char op = str[0];
		res[s++] = op;
		for(int i = 0 ; i < len ; i++) {
			if(op != str[i]) {
				op = str[i];
				res[s++] = op;
			}
		}
		for(int i = s - 1 ; i >= 0 ; i--) {
			if(res[i] == '-') {
				ans = i + 1;
				break;
			}
		}
		printf("Case #%d: %d\n" , ca , ans);

	}
}