#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

int main() {
       
    long long int t,n,i,j,tempn,newn;
    int a[10]={0},count=1,d,rem;
    cin>>t;

    while(t--)
    {
    	cin>>n;
    	d=0;
    	
    	for(i=0;i<10;i++)
    		a[i]=0;

    	
    	if(n==0)
    		cout<<"Case #"<<count++<<": INSOMNIA"<<endl;

    	else
    	{
    		j=1;
    		while(d!=10)
    		{
    			newn=j*n;
    			j++;
    			tempn=newn;
    			while(tempn)
    			{
    				rem=tempn%10;
    				tempn=tempn/10;
    				if(a[rem]==0)
    				{
    					a[rem]=1;
    					d++;
    				}
    				
    			}
    		}
    		cout<<"Case #"<<count++<<": "<<newn<<endl;
    		
    	}

    }

    return 0;
}
