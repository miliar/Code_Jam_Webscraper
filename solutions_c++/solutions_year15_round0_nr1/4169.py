#include<bits/stdc++.h>
using namespace std;
int main(){
  	freopen("AL.in", "r", stdin);
  	freopen("out.txt", "w", stdout);
	int t,n,j;
	char s[1003];
	scanf("%d",&t);
	int r,p;
	for(j=1;j<=t;j++){
		r=0;
		
		scanf("%d %s",&n,s);
		p=s[0]-'0';
		for(int i=1;i<=n;i++){
			if(i>p){
				r += i-p;
				p = i; 
			}
			p = p+s[i]-'0';
			
		}
		printf("Case #%d: %d\n",j,r);
	}
}
