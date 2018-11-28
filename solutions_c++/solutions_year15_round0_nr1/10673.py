#include<stdio.h>
#include<iostream>
#include<fstream>
#include<math.h>

using namespace std;

int main()
{
		int smax=0,s=0,arr[7]={-1},ans=0,sum=0,temp;
		int t=0,i=0,j=0,in=0;
		ifstream myfile;
		
		//myfile.open ("input.txt");
		cin>>t;
		for(i=1;i<=t;i++)
		{
		    smax=0;
		    s=0;
		    for(j=0;j<7;j++)
		    {
		        arr[j]=-1;
		    }
		    ans=0;
		    sum=0;
		    temp=0;
		    in=0;
			// extract digits
			cin>>smax;
			cin>>s;
			temp=s;
			for(j=smax,in=0;j>=1;j--,in++)
			{
				arr[in]=temp/pow(10,j);
				temp=temp%(int)pow(10,j);
			}
			arr[in]=temp;
			
			// digit extraction ends
			
			sum=0;
			for(j=0;j<=smax;j++)
			{
				if(arr[j]!=0)
				{
					if(sum<j)
					{
						ans+=j-sum;
						sum+=j-sum;
					}
					sum+=arr[j];
				}
			}
			cout<<"Case #"<<i<<": "<<ans<<"\n";
		}
		myfile.close();
		
    return 0;
}