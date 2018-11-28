#include<iostream>
#include<cstdio>
#include<fstream>
using namespace std;
int main()
{
									//	freopen ("A-small-attempt0.in","r",stdin);
									//	freopen ("output.txt","w",stdout);

	int t,a,b;
	int arr1[6][6],arr2[6][6];

	 cin>>t;
	for(int tt=1;tt<=t;tt++)
	{
		int ans=0,index=0;

		cin>>a;
		for(int i=1;i<=4;i++)
				for(int j=1;j<=4;j++)
						cin>>arr1[i][j];

		cin>>b;
		for(int i=1;i<=4;i++)
				for(int j=1;j<=4;j++)
						cin>>arr2[i][j];
						
	//	cout<<a<<"  a and b "<<b<<endl;

		for(int i=1;i<=4;i++)
		{
			int num=arr1[a][i];
		//	cout<<num<<endl;
				for(int j=1;j<=4;j++)
				{

				   if(num==arr2[b][j])
    	  		             ans++;
				   if(ans==1 and num==arr2[b][j])
				   			 index=j;
				}
        }
      //  cout<<"index "<<index<<endl;
        
		cout<<"Case #"<<tt<<": ";
		if(ans==1)
				  cout<<arr2[b][index]<<endl;
		else if(ans==0)
				  cout<<"Volunteer cheated!"<<endl;
		else
				  cout<<"Bad magician!"<<endl;
        
        
	}
}
