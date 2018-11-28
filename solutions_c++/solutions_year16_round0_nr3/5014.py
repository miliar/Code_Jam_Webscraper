#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
using namespace std;
long long int divisor(long long int n) {
	int i;
	for(i = 3; i <= sqrt(n); i++){
		if(!(n%i))
			return i;
	}
	return 1;
}
void add(char *s) {
	int i, c = 1;
	for(i= strlen(s) - 2; i>0; i--) {
		if(c){
			if(s[i] == '1') {
				s[i] = '0';
			}
			else {
				s[i] = '1';
				c = 0;
				break;
			}
		}
	}
}
int main() {
	long long int t,n,j,i, div[10],a, k,l;
	char s[100],final[100];
	char *p;
	p = NULL;
	scanf("%lld",&t);
	for(k = 1; k<=t; k++) {
		scanf("%lld %lld",&n,&j);
		l = j;
		cout << "Case #"<<k<<": "<<"\n";
		for(i = 1; i< n - 1; i++) {
			s[i] = '0';
			final[i] = '1';
		}
		s[0] = final[0] = s[n-1] = final[n-1] = '1';
		s[n] = final[n] = '\0';
		while(l && strcmp(s,final)) {
			for(i = 2; i<=10; i++) {
				div[i] = 0;
				a = strtoll(s,&p,i);
				div[i] = divisor(a);
				if(div[i] == 1){
					break;	
				}
			}
			if(i == 11) {
				printf("%s ",s);
				for(i = 2; i<10; i++)
					printf("%lld ",div[i]);
				printf("%lld\n",div[i]);
				l--;
			}	
			add(s);
		}
	}
	return 0;
}
