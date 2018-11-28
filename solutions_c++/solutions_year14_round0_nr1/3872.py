#include<iostream>
#include<fstream>
using namespace std;

int main()
{
	freopen("A-small-attempt0.in","r",stdin); 
	freopen("Problem_a_output.txt","w",stdout);
	
	int t,a[4][4],b[4],x,i,j,k,l,c[4],q1,q2;
	cin>>t;
	for(x=0;x<t;x++)
	{
		
		cin>>q1;
		
		
		
		for(i=0;i<4;i++)
		   {
		   		for(j=0;j<4;j++)
		   		 {
		   		 	cin>>a[i][j];
		   		 	if(i==q1-1)
		   		 	c[j]=a[i][j];
		   		 }
		   }
		   
		   
		cin>>q2;
		
		  	for(i=0;i<4;i++)
		   {
		   		for(j=0;j<4;j++)
		   		 cin>>a[i][j];
		   }
		   
	
		   
		   
		   k=0;
		   	for(j=0;j<4;j++)
		   		 	{
		   		     for(l=0;l<4;l++)
						{
							if(a[q2-1][j]==c[l])
							 b[k++]=c[l];
						}	
		   
		            }
		   cout<<"Case #"<<x+1<<": ";
		   
		   if(k>1)
		   cout<<"Bad Magician!";
		   else if(k==0)
		   cout<<"Volunteer cheated!";
		   else if(k==1)
		   cout<<b[0];
		   cout<<endl;
		   
		   
		
		
		
	}
 
}
