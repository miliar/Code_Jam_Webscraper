#include <iostream>
#include <iomanip>
#include <stdio.h>

using namespace std;
int main()
{
	int t,sh,str[1001],i,j,counter=0,out[100],sum=0;
	char num;
	cin>>t;

	for(i=0;i<t;i++)
		{
			cin>>sh;
			sum=0;
			counter=0;
			
			for(j=1;j<=sh+1;j++)
		 	{
		 		cin>>num;
		 		str[j-1]=num-48;
		 		
		 		sum+=str[j-1];
		 		
				if(j>sum)
					{
						counter++;
						sum++;
					}
				
		 	}
			out[i]=counter;
		}

	for(i=0;i<t;i++)	
		cout<<"Case #"<<i+1<<": "<<out[i]<<endl;
	return 0;
}