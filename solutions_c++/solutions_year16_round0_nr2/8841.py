#include<cstdio>
#include <iostream>

using namespace std;

char s[102];
int main(){
	int t;
	scanf("%d",&t);
	for (int time = 1; time <= t; time++) {
		fill(s,s+102,'+');
		scanf("%s",s);
		int count=0;
		for ( int i = 0; i < 102; i++) {
			if (s[i]!='+' && s[i]!='-') {
				s[i]='+';
			}
		}
		for (int i = 0; i < 100; i++) {
			if(s[i]!=s[i+1])count++;
		}
		printf("Case #%d: %d\n",time,count );
	}
}
