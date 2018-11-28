#include<iostream>
using namespace std;
main()
{
	int t,j=0;
	cin>>t;
	while(t--)
	{ int s;
	  cin>>s;
	  
	  char *k;
	  k=new char [s+2];
	  int i;
	  cin>>k;
	  
	  int sum,ans=0;
	  sum=k[0]-48;
	  for(i=1;i<s+1;i++)
	  {
	  	if(sum>=i)
	  	{
	  		sum=sum+k[i]-48;
	  	}
	  	else
	  	{
	  		ans=ans+i-sum;
	  		sum=i+k[i]-48;
	  	}
	  }
	  j++;
	  cout<<"case #"<<j<<": "<<ans<<endl;;
	  
		
	}
}
