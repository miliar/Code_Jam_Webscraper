#include<bits/stdc++.h>
#define M 1000001
#define ll long long int
using namespace std;
void inserta(char p[],char c){
	int i,j,k=strlen(p);
	p[k]=c;
	p[k+1]='\0';
}
void insertb(char p[],int c){
	int i,j,k,n=strlen(p);
	char z[M];
	z[0]=c;
	for(i=1;i<=strlen(p);i++){
		z[i]=p[i-1];
	}
	z[n+1]='\0';
	for(i=0;i<=strlen(z);i++){
		p[i]=z[i];
	}
}
void findLastWord(char s[]){
	int i,j,k;
	char p[M];
	p[0]=s[0];
	p[1]='\0';
	char c,d,e;
	for(i=1;i<strlen(s);i++){
		c='a';
		for(j=1;j<strlen(p);j++){
			if(p[j]!=p[0]){
				c=p[j];
				break;
			}
		}
		if(s[i]>p[0]){
			insertb(p,s[i]);
		}
		else if(s[i]==p[0]){
			if(c!='a'){
				if(c<s[i]){
					insertb(p,s[i]);
				}
				else{
					inserta(p,s[i]);
				}
			}
			else{
				inserta(p,s[i]);
			}
		}
		else{
			inserta(p,s[i]);
		}
	}
	printf("%s\n",p);
}
int main(){	
	freopen("A-large.in","r",stdin);
    freopen("A-large-output.out","w",stdout);
	int i,j,k,t,n;
	cin>>t;
	char s[M];
	for(i=1;i<=t;i++){
		cin>>s;
		printf("Case #%d: ",i);
		findLastWord(s);
	}
	return 0;
}
