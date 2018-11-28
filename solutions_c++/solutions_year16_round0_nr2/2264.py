#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int t;
char s[111];
int f(int n,char tag){
	if (n==0) return 1-(tag==s[n]);
	char rev;
	if (tag == '+') rev = '-';
	else rev = '+';
	if (s[n] == tag)
		return f(n-1,tag);
	else return f(n-1,rev)+1;
}
int main(){
	freopen("skj.in", "r", stdin);
	freopen("skj.out", "w", stdout);
	scanf("%d",&t);
	int cas=0;
	while (t--){
		scanf("%s",s);
		int len = strlen(s);
		printf("Case #%d: %d\n",++cas,f(len-1,'+'));
	}
} 
