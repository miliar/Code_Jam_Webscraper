#include <iostream>
using namespace std;

int main() 
{
	int t01[4][4],t02[4][4],num=0,t,row1,row2;
	cin>>t;
	for(int k=1;k<=t;k++)
	{
	
		cin>>row1;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			cin>>t01[i][j];
			
		}
		cin>>row2;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			cin>>t02[i][j];
			
		}
		int match=0;
		for(int i=0;i<4;i++)
		{
		for(int j=0;j<4;j++)
		{ 
   			if(t01[row1-1][i]==t02[row2-1][j])
   			{
   				match++;
   				num=t02[row2-1][j];
   				
   			}
		 }
		}
		 if(match==0)
		   cout<< "Case #"<<k<<": Volunteer cheated!";
		   else if(match==1)
		   cout<<"Case #"<<k<<": "<<num;
		   else
		   cout<<"Case #"<<k<<": Bad magician!";
		   cout<<endl;
	}
	
	return 0;
}