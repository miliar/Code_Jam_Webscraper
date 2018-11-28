#include<iostream>
#include<algorithm>
#include<math.h>
#include<string.h>
#include<stack>
#include<queue>
#include<stdio.h>
using namespace std;
int main()
{
    int t,ctr,p,smax,sum,i;
    
    cin>>t;
    for(p=1;p<=t;p++)
    {
    	cin>>smax;
        char str[smax+1]; 

		cin>>str;
    	ctr=0;
    	sum=0;
    	for(i=0;i<=smax;i++)
    	{
    		sum=sum+str[i]-'0';
    		if(sum == 0)
    		   ctr++;
    		else
			   sum--;   
    	}
    	cout<<"Case #"<<p<<": "<<ctr<<endl;
    }
	return 0;
}


