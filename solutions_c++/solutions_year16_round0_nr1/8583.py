#include <iostream>
#include<stdio.h>
using namespace std;

int main() {
    freopen("a1.in","r",stdin);
    freopen("output1.out","w",stdout);
	int a;	
	int b;
	cin>>b;
	
	int j=0;
	while(j<b)//for(int j=0;j<b;j++)
	{   long long int count=0,temp1,temp2;
		long long int p;
		int arr[]={0,1,2,3,4,5,6,7,8,9};
		cin>>p;
		if(p==0)
		{
			cout<<"Case #"<<j+1<<": INSOMNIA"<<endl;
		}
		else
		{  int k=1;
		    while(1)
		    {   
		        temp1=p*k;
		        temp2=temp1;
		        k++;
		        while(temp1>0)
		        {
		            a=temp1%10;
		            if(arr[a]==a)
		            {
		                arr[a]=-1;
		                count++;
		            
		            }
		            temp1=temp1/10;
		        }
		        if(count==10)
		        break;
		        //cout<<"j:"<<j<<"\tk:"<<k<<"\tcount:"<<count<<"\ttemp1"<<temp1<<"\ttemp2:"<<temp2<<endl;
		    }
		    cout<<"Case #"<<j+1<<": "<<temp2<<endl;
		}
	    j++;
	    
	}
	// your code goes here
	return 0;
}
