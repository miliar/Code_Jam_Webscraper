#include <stdio.h>
#include <cstring>
using namespace std;

int main(){
	int tc,l,count,start;
	char p[102];
	scanf("%d\n",&tc);
	for(int i=1; i<=tc; i++){
		count=0;
		scanf("%s\n",p);
		l = strlen(p);
		start=0;
		bool flag=1;
		while(start<l){
			if(p[start]=='-'){
				if(flag) count++;
				else count+=2;
				flag=0;
				while(p[start]=='-') start++;
			}else while(p[start]=='+') {flag=0; start++;}
		}
		printf("Case #%d: %d\n", i,count);
	}
}