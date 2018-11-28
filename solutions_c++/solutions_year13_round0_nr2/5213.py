#include<cstdlib>
#include <iostream>

using namespace std;

int main()
{
	int n_case;
	cin>>n_case;
	int mat[100][100];
	int max_righe[100];
	int max_col[100];
	for(int i=0;i<n_case;i++)
	{
		int rig,col;
		cin>>rig;
		cin>>col;
		
		int aus=-1;
		for(int j=0;j<rig;j++)
		{
			aus=-1;
			for(int k=0;k<col;k++)
			{
				cin>>mat[j][k];
				if(mat[j][k]>aus)
				{
					aus=mat[j][k];
				}
			}
			max_righe[j]=aus;
		}
				
		for(int j=0;j<col;j++)
		{
			aus=-1;
			for(int k=0;k<rig;k++)
			{
				if(mat[k][j]>aus)
				{
					aus=mat[k][j];
				}
			}
			max_col[j]=aus;
		}
		
		bool ris=true;
		for(int j=0;j<rig;j++)
		{
			for(int k=0;k<col;k++)
			{
				ris=ris && (mat[j][k]==max_righe[j] || mat[j][k]==max_col[k]);
			}
		}
		
		cout<<"Case #"<<i+1<<": ";
		if(ris)
		{
			cout<<"YES\n";;
		}
		else
		{
			cout<<"NO\n";
		}
	}
}
