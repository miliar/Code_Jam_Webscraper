#include<bits/stdc++.h>
using namespace std;
int od[20][3];
char ch[3]={'P','R','S'};
void print(int p,int lv){
	if(lv==0) putchar(ch[p]);
	else{
		if(od[lv-1][p]<od[lv-1][(p+1)%3]){
			print(p,lv-1);
			print((p+1)%3,lv-1);
		}
		else{
			print((p+1)%3,lv-1);
			print(p,lv-1);
		}
	}
}
int main(){
	for(int i=0;i<3;i++){
		od[0][i]=i;
	}
	for(int i=1;i<20;i++){
		for(int j=0;j<3;j++){
			od[i][j]=od[i-1][j]+od[i-1][(j+1)%3]-1;
		}
	}
	int T;
	scanf("%d",&T);
	for(int cs=1;cs<=T;cs++){
		int n,p,r,s,a=1,b=0,c=0;
		scanf("%d%d%d%d",&n,&r,&p,&s);
		for(int i=0;i<n;i++){
			int na=a+c,nb=a+b,nc=b+c;
			a=na,b=nb,c=nc;
		}
		printf("Case #%d: ",cs);
		if(a==p&&b==r&&c==s){
			print(0,n);
		}
		else if(a==r&&b==s&&c==p){
			print(1,n);
		}
		else if(a==s&&b==p&&c==r){
			print(2,n);
		}
		else printf("IMPOSSIBLE");
		puts("");
	}
	return 0;
}