#include <iostream>
#include <cstdlib>
#include <cstdio>

using namespace std;

int main()
{
	freopen("A-small-attempt4.in","r",stdin);
	freopen("out.out","w",stdout);
	int t, ans;
	cin>>t;
	int mat[4][4];
	int v1[4];
	 int v2[4];
	for(int i = 0 ; i < t; i++)
	{
		int count = 0,aux;
		cin>>ans;
		for(int j = 0 ; j < 4; j++)
		{
			for(int k = 0 ; k < 4; k++)
				cin>>mat[j][k];		
		}
		for(int j = 0 ; j < 4 ;j++)
			v1[j]=mat[ans-1][j];
		cin>>ans;
		for(int j = 0 ; j < 4; j++)
		{
			for(int k = 0 ; k < 4; k++)
				cin>>mat[j][k];		
		}
		for(int j = 0 ; j < 4 ;j++)
			v2[j]=mat[ans-1][j];
		
		for(int j = 0 ; j < 4 ;j++)
		{
			for(int k = 0 ; k < 4; k++)
			{
				if(v1[j] == v2[k])
				{
					aux = v1[j];
					count++;
				}
			}

				
		}
		
		if(count==1)
			cout<<"Case #"<<i+1<<": "<<aux<<endl;
		else if(count<1)
			cout<<"Case #"<<i+1<<": "<<"Volunteer cheated!"<<endl;
		else if(count>1)
			cout<<"Case #"<<i+1<<": "<<"Bad magician!"<<endl;
		
	}
	
	
	
	return 0 ; 
}
