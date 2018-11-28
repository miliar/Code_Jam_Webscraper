#include <bits/stdc++.h>
using namespace std;

char s[111];
int t;

int main() {
    scanf("%d",&t);
    for(int k = 1; k<=t; ++k){
    	scanf("%s",s);
    	int res = 0;
    	for(int i = 1; s[i]; ++i){
    		if(s[i] != s[i-1]){
    			++res;
    		}
    	}
    	int n = strlen(s);
    	if(s[n-1] == '-') ++res;
    	printf("Case #%d: %d\n",k,res);
    }
	return 0;
}
