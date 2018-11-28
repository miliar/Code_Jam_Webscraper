#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

string stack;

int main()
{
	int t,cas=1;
	cin >> t;
	while(t--) {
		cin >> stack;
		int ans = 0;
		int state = 0;
		for(int i = stack.size() - 1 ; i >= 0 ; i --) {
			if(stack[i] == '+') {
				if(state % 2) {
					ans ++;
					state ++;
				} 
			} else {
				if(state % 2 == 0) {
					ans ++;
					state++;
				}
			}
		}
		printf("Case #%d: %d\n",cas++,ans);		
	}
	return 0;
}

