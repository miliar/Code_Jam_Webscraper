#include<iostream>
using namespace std;
int main()
{
	int t,a[4][4],b[4][4],i,r1,r2,l,j,d=1,k;
	cin>>t;
	while(t--)
	{
		l=0;
		cin>>r1;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
			     cin>>a[i][j];
	        }
	    }
	    cin>>r2;
	    for(i=0;i<4;i++)
	    {
	    	for(j=0;j<4;j++)
             cin>>b[i][j];	    	
	    }
	    for(i=0;i<4;i++)
	      {
	      	for(j=0;j<4;j++)
	      	{
	      	
	      	   if(a[r1-1][i]==b[r2-1][j])
	      	   {
	      	     k=a[r1-1][i];
	      	     l++;
	      	   }
	        }
	      }
	      if(l==1)
	      {
	      	cout<<"Case #"<<d<<": "<<k<<"\n";
	      }
	      if(l>1)
	      cout<<"Case #"<<d<<": "<<"Bad magician!\n";
	      if(l==0)
	      cout<<"Case #"<<d<<": "<<"Volunteer cheated!\n";
	      d++;
	      	
	}
	
}
