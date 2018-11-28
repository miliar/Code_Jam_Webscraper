#include <bits/stdc++.h>
#define X first
#define Y second
#define PI pair<int,int>
using namespace std;
char str[1010];
int a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("1.out","w",stdout);
	scanf(" %d",&t);
	for(l=1;l<=t;l++){
		printf("Case #%d: ",l);
		scanf(" %s",str);
		n=strlen(str);
		f=0;
		s=0;
		for(i=n-1;i>=0;i--){
			if(str[i]=='-'&&f==0)f=1,s++;
			else if(str[i]=='+'&&f==1)f=0,s++;
		}
		printf("%d\n",s);
	}
	return 0;
}