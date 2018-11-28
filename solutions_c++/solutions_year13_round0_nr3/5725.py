#include<iostream>
#include<stdio.h>
using namespace std;
#define ll long long
bool check(int i)
{
  	int oldi,newi;
	oldi = i;
	for(newi=0;oldi;)
 	{
    	newi=newi*10+oldi%10;
     	oldi=oldi/10;
	}
  	return (i == newi);
}
int qu[32];
int main(){
	freopen("C-small-attempt0.in","r",stdin);
	freopen("o.txt","w",stdout);
	int t,i,j,cas=0;
	int a,b,top=0;
	scanf("%d",&t);
	for(int i=1;i*i<=1000;i++){
		if(check(i) && check(i*i)){
			qu[top++]=i*i;
		}
	}
	while(t--){
		scanf("%d %d",&a,&b);
		for(i=0;i<top;i++){
			if(qu[i]>=a)
				break;
		}
		for(j=top-1;j>=0;j--){
			if(qu[j]<=b)
				break;
		}
		printf("Case #%d: %d\n",++cas,j-i+1);
	}
	return 0;
}
			

