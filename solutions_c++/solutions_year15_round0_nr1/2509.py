#include <iostream>
#include<string.h>
using namespace std;
int main()
 {
 	freopen ("aa.in", "r", stdin);
   freopen ("output.txt", "w", stdout);
	long long int t,i,j,n,v=0,ans,temp,count;;
	char a[10000]; 
	scanf("%lld",&t);
	while(t--)
	{
	    ans=0;v++; count=0;
	    scanf("%lld %s",&n,&a);   
		 count=a[0]-48; 
	    for( i=1;i<strlen(a);i++)
        {
           
            if(count>=i)
            {
               count=count+(a[i]-48);
            }
            else {
                ans=ans+i-count;
                count=i+(a[i]-48);
 
            }
 
        }
	    printf("Case #%lld: %lld\n",v,ans);
	}
	
	return 0;
}
