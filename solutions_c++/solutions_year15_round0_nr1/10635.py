#include <iostream>
#include<stdio.h>
using namespace std;

int main() {
	int t,j;
	cin>>t;
	for(j=1;j<=t;j++)
	{
	       int n,i,sum=0,ans=0;
	       cin>>n;
	       char str[n+5];
	       scanf("%s",&str);
	       for(i=0;str[i]!='\0';i++)
            {
                int temp=(int)str[i]-48;
               // cout<<temp<<endl;
                sum+=temp;
                if((i+1-sum)>0)
                    {
                        ans+=(i+1-sum);
                        sum+=(i+1-sum);
                    }
            }	       
	        cout<<"Case #"<<j<<": "<<ans<<endl;
	}
}
