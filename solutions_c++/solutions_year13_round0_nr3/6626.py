#include <iostream>
#include<stdio.h>
using namespace std;

int main() {
	
int d[2000]={0};
d[1]=d[4]=d[9]=d[121]=d[484]=1;
int t,count,u,a,b;
cin>>t;
for(u=0;u<t;u++)
{
    count=0;
    cin>>a>>b;
    for(int i=a;i<=b;i++)
    {
        if(d[i]==1)
        count++;
    }
    printf("Case #%d: %d\n",u+1,count);
}        
	return 0;
}