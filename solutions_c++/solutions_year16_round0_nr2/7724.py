#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;
char s[110];
int main() {
	int x,n,c=1;
	cin>>x;
	while(x--) {
		cin>>s;
        int len = strlen(s);
        int answer = 0, flag = 0;
		for(int i= len-1; i >= 0; i--) {
			if(s[i] == '+' && flag == 0) {
				continue;
		    } else if(s[i] == '+' && flag == 1) {
		    	answer++;
		    	flag = 0;
		    } else if(s[i] == '-' && flag == 0) {
		    	answer++;
		    	flag = 1;
		    } else if(s[i] == '-' && flag == 1) {
		    	continue;
		    }								
		}
        printf("Case #%d: %d\n",c++,answer);
	}
	return 0;
}
