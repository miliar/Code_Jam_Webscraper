#include<iostream>
using namespace std;
int main()
{
	
	int t,n1,n2;
	int arr1[4][4];
	int arr2[4][4];
	int flag=0;
	cin>>t;//total test cases
	int ar[t];
	int same;
	for(int i=0;i<t;i++)
	{
		cin>>n1;
		for(int j=0;j<4;j++)
		{
		  for(int k=0;k<4;k++)
		  {
		  	cin>>arr1[j][k];
		  	//scanf("%d",&arr1[j][k]);
		  }
	    }
	    cin>>n2;
		for(int j=0;j<4;j++)
		{
		  for(int k=0;k<4;k++)
		  {
		  	cin>>arr2[j][k];
		  	//scanf("%d",&arr2[j][k]);
		  }
	    }
	    for(int j=0;j<4;j++)
	    {
	    	for(int k=0;k<4;k++)
	    	{
	    		if(arr1[n1-1][j]==arr2[n2-1][k])
	    		{
	    			flag++;
	    			same=arr1[n1-1][j];
	    		}
	    		if(flag==2)
	    		break;
	    		
	    	}
	    	if(flag==2)
	    	break;
	    }
	  if(flag==0)
	  ar[i]=-2;
	  else if(flag==1)
	  ar[i]=same;
	  else if(flag==2)
	  ar[i]=-3; 
	  flag=0;  
	}
	for(int i=0;i<t;i++)
	{
		if(ar[i]==-3)
		cout<<"Case #"<<i+1<<": Bad magician!\n";
		else if(ar[i]==-2)
		cout<<"Case #"<<i+1<<": Volunteer cheated!\n";
		else
		cout<<"Case #"<<i+1<<": "<<ar[i]<<"\n";
	}
}