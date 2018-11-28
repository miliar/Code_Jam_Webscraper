#include <iostream>
using namespace std;
int main()
{
	int t,i,possible=0,j,n,m,k,T;
	int a[101][101];
	cin>>t;
	T=t;
	while(t--)
	{
		cout<<"Case #"<<T-t<<": ";
		cin>>n>>m;
		possible=1;
		for(i=0;i<n;i++)
		{
			for(j=0;j<m;j++)
			{
				cin>>a[i][j];
			}
		}


		for(i=0;i<n;i++)
		{
			for(j=0;j<m;j++)
			{
				
				
				
					//cout<<i<<" "<<j<<endl;
					for(k=0;k<n;k++)
					{
						if(a[i][j]<a[k][j])
							break;
					}
					//cout<<k<<endl;
					if(k!=(n))
					{
						for(k=0;k<m;k++)
						{
							if(a[i][j]<a[i][k])
								break;
						}
						if(k!=m)
						{
							possible=0;
							break;
						}
					}
				

			}
		}	
		if(possible)
		{
			cout<<"YES"<<endl;
		}
		else
			cout<<"NO"<<endl;
	}
	return 0;
}
 
