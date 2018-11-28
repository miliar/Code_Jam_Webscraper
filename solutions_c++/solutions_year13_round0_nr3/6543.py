#include<iostream>
#include<stdio.h>
using namespace std;

int main()
{
	int t=1,cnt,val=0,l,a,b;
	int c[]={ 1, 4, 9, 121, 484};
	scanf("%d",&l);
	while(t<=l){
		cnt=0;
    scanf("%d%d",&a,&b);
	printf("Case #%d: ",t);
	for(int i=0;i<5;i++)
	{
		if(c[i]>=a && c[i]<=b)
		cnt++;
	}
	printf("%d\n",cnt);
     	t++;
    }
	
}
