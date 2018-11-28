#include<iostream>
#include<stdio.h>
#include<stdlib.h>

using namespace std;
int main()
{
    int t,a,b,l;
    scanf("%d",&t);
    for(int i=1;i<=t;i++) {
        int total=0;
    	scanf("%d %d %d",&a,&b,&l);
        if(l!=0) {
            total+=(a+b)-1;
    	for(int j=1;j<a;j++)
    	for(int k=1;k<b;k++)
    	if((j&k)<l)
    	total++;
        }
    	printf("Case #%d: %d\n",i,total);
    }
}
