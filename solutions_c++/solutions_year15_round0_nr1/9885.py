#include <iostream>
#include<stdio.h>
#include<string.h>
using namespace std;

int main() {
	int t,n;
	char str[100001];
	cin>>t;
	int j=1,i;
	while(j<=t)
	{
	    int count=0,sum=0;
	    scanf("%d%s",&n,str);
	    for(i=0;i<n+1;i++)
	    {
	       if(sum<i)
	       {
	       count++;
	       sum++;
	       }
	       sum=sum+(str[i]-'0');
	    }
	    printf("Case #%d: %d\n",j,count);
	    j++;
	  }
	}

