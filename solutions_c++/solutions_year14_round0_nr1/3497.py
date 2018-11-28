#include <iostream>
using namespace std;

int main()
{
	int t,c=1;
	cin>>t;
	while(t!=0)
	{
    	int A[4][4];
    	int B[4][4];
    	int N=16,n=4,a,b,i,j,count=0,ans;
    	cin>>a;
    	for(i=0;i<n;i++)
    	{
 		   for(j=0;j<n;j++)
 		   {
 		   	cin>>A[i][j];
 		   }
    	}
    	cin>>b;
    	for(i=0;i<n;i++)
    	{
 		   for(j=0;j<n;j++)
 		   {
 		   	cin>>B[i][j];
 		   }
    	}
    	for(i=0;i<n;i++)
    	{
 		   for(j=0;j<n;j++)
 		   {
 		   	if(A[a-1][i]==B[b-1][j])
 		   	{
 		   		ans=A[a-1][i];
 		   		count++;
 		   	}
 		   }
    	}
    	if(count==1)
    	{
    		cout<<"Case #"<<c<<": "<<ans<<endl;;
    	}
    	else if(count==0)
    	{
    		cout<<"Case #"<<c<<": "<<"Volunteer cheated!"<<endl;
    	}
    	else
    	{
    		cout<<"Case #"<<c<<": "<<"Bad magician!"<<endl;;
    	}
    	c++;
    	t--;
	}
}