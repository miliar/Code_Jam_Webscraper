#include <iostream>
#include <cstdio>
using namespace std;


char str[1005]="";
int main() {
	int T,i,j,N,count=0,sum=0;
	scanf("%d",&T);
	while(T--)
	{
	    sum=0;
	    int val=0;
	    count++;
	    scanf("%d %s\n",&N,str);
	    sum=(str[0]-'0');
	    for(i=1;i<=N;i++)
	    {
	       	
	        if(sum<i)
	        {
	            val++;
	            sum++;
	        }
	        sum+=(str[i]-'0');
	    }
	    printf("Case #%d: %d\n",count,val);
	}
	return 0;
}