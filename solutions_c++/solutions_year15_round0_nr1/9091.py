#include <iostream>
#include<stdio.h>
using namespace std;

int main() {
	int t,i,n,s[1001],stood,extra,e1,f,k;
	char str[1001];
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{   stood=0;extra=0;e1=0;
	    scanf("%d %s",&n,str);
	    printf("Case #%d: ",i);
	    stood=str[0]-'0';
	    if(n==0)
	    {
	        printf("0\n");
	        continue;
	    }
	    for(k=1;k<=n;k++)
	    {   extra=0;
	        if(k<=stood) 
	        {
	            stood+=(str[k]-'0');
	        }
	        else
	        {   if(str[k]!='0')
	            extra+=(k-stood);
	            stood+=str[k]-'0';
	            stood+=extra;
	            e1+=extra;
	        }
	    }
	    printf("%d\n",e1);
	    
	    
	}
	return 0;
}
