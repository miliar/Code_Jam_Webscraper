#include <iostream>
#include <cstring>
#include <stdio.h>
#include <algorithm>
#include <cmath>
#include <map>
#include <vector>
using namespace std;


char s[110];
int main() {
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	scanf("%d",&T);
	int C = 1;
	while(T --) {
        scanf("%s",s);
        int n = strlen(s);
        int turns = 0;
        for (int i = 1;i < n;i ++) {
        	if(s[i] != s[i - 1]) {
        		turns ++;
			}
		} 
		if(s[n - 1] != '+') {
			turns ++;
		}
        printf("Case #%d: %d\n",C++,turns);
	}
}













































































