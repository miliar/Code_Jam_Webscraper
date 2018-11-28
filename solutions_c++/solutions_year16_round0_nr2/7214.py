#include <cmath>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

typedef long long ll;

#define mem0(x) memset(x, 0, sizeof(x))
#define mem1(x) memset(x, -1, sizeof(x))

char str[105];

int main(){
	int t, ans, pre, _case = 1;
	scanf("%d", &t);
	while(t--)
	{
		ans = 0;
		scanf("%s", str);
		int len = strlen(str);
		pre = str[0]=='+';
		for(int i = 0; i < len;){
			if(str[i]=='-'){
				while(str[i]=='-'&&i<len) i++;
				if(pre==1) {
					ans += 2;
				}
				else {
					ans += 1;
					pre = 1;
				}
			}
			while(str[i]=='+') i++;
		}
		printf("Case #%d: ", _case++);
		printf("%d\n", ans);
	}
}

