#include<iostream>
#include<bits/stdc++.h>
#define sd(n) scanf("%d",&n)
#define sld(n) scanf("%lld",&n)
#define ss(s) scanf("%s",s)
#define f(n) for(int i=0;i<n;i++)

using namespace std;
char revch(char c){
	if(c=='-') return '+';
	else return '-';
}
void rev(char s[101],int pos){
	int len=strlen(s),i=0;
	char c;
	while(i<=pos){
		c=s[i];
		s[i]=revch(s[pos]);
		s[pos]=revch(c);
		i++;
		pos--;
	}
}
int main(){
	int test; sd(test);
	for(int t=1;t<=test;t++){
		char s[101]; ss(s);
		printf("Case #%d: ",t);
		int l=strlen(s),c=0,i,pos;
		if(l==1 && s[0]=='+') printf("0\n");
		if(l==1 && s[0]=='-') printf("1\n");
		if(l==1) continue;
		while(true){
			for(i=0;i<l-1;i++)	if(s[i]!=s[i+1]) break;
            pos=i;
			if(pos==l-1 && s[0]=='+') break;
			if(pos==l-1 && s[0]=='-') pos=l-1;
			rev(s,pos);
			c++;
		}
		printf("%d\n",c);
	}
	return 0;
}
