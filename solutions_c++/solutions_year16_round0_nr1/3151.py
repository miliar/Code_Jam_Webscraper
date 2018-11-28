#include <bits/stdc++.h>
#define X first
#define Y second
#define PI pair<int,int>
using namespace std;
char str2[199100];
int str[199100],mul[199100];
set <int> S;
int a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("1.out","w",stdout);
	scanf(" %d",&t);
	for(l=1;l<=t;l++){
		printf("Case #%d: ",l);
		scanf(" %d",&n);
		if(n==0){
			printf("INSOMNIA\n");
			continue;
		}
		for(i=n;;i+=n){
			j=i;
			while(j){
				S.insert(j%10);
				j/=10;
			}
			if(S.size()==10)break;
		}
		printf("%d\n",i);
		S.clear();
	}
	return 0;
}