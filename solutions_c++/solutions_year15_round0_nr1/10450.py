#include <iostream>
#include<stdio.h>
using namespace std;

int main() {
    int s,i,t,j,sum,b;
    char a[7];
    scanf("%d",&t);
    for(j=1;j<=t;j++)
    {
        scanf("%d\t %s",&s,&a);
      //  cout<<s;
        
        sum=0;
       for(i=0;i<=s;i++)
        {
           // cout<<a[i];
            if(a[i]==48)
            {
               // sum++;
                //cout<<sum;
            }
        }
        
      //  if(a[0]==48);
       // sum++;
       b=0;
        for(i=0;i<=s;i++)
        {
            if(a[i]!=48)
            {
              sum=i;
              b=sum+a[i]-48;
              break;
            }    
        }
        for(i=sum+1;i<=s;i++)
        {
            if(a[i]!=48)
            {
                if(b<i)
                {
                    sum=sum+i-b;
                    b=b+sum+a[i]-48;
                }
                else
                {
                    b=b+a[i]-48;
                }
            }
        }
       printf("Case #%d: %d\n",j,sum);
     //  cout<<endl;
    }
	// your code goes here
	return 0;
}

