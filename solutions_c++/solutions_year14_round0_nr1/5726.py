#include<iostream>
using namespace std;
int main()
{
	int t,k;
	cin>>t;
    for(k=1;k<=t;k++)	
	{
		int m,n,arr1[4][4],arr2[4][4],count=0,result;
		cin>>m;
		for(int i=0;i<4;i++)
		 for(int j=0;j<4;j++)
		{
			cin>>arr1[i][j];
		}
		
		cin>>n;
		for(int i=0;i<4;i++)
		 for(int j=0;j<4;j++)
		{
			cin>>arr2[i][j];
		}
		
		for(int i=0;i<4;i++)
		 for(int j=0;j<4;j++)
		{
		   if(arr1[m-1][i]==arr2[n-1][j])
		   {
   				count++;   	
				result=arr1[m-1][i];	
   		   }
		}

		 if(count==1)
		   {
   		 		      cout<<"Case #"<<k<<" : "<<result<<endl;
	       }
		
		else if(count==0)
		   {
   		 		      cout<<"Case #"<<k<<" : "<<"Volunteer cheated!"<<endl;
	       }
		
		else if(count>1)
		   {
   		 		      cout<<"Case #"<<k<<" : "<<"Bad magician!"<<endl;
	       }
		
	
	}
return 0;		
}