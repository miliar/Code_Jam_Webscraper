#include<iostream>
#include<fstream>

using namespace std;

int main(){
	freopen("output.txt","w",stdout);
	freopen("input.txt","r",stdin);

	int t;
	cin>>t;
	for(int k=1;k<=t;k++){
		cout<<"Case #"<<k<<": ";
		int mat[4][4]={};
		int r1;
		cin>>r1;
		bool a[17]={};
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				cin>>mat[i][j];
				if((i+1)==r1)
					a[mat[i][j]]=true;
			}
		}
		int r2;
		int ctr=0;
		int ans;
		cin>>r2;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				cin>>mat[i][j];
				if((i+1)==r2)
					if(	a[mat[i][j]])
					{
						ans=mat[i][j];
						ctr++;
					}
			}
		}

		if(ctr==0)
			cout<<"Volunteer cheated!\n";
		else if(ctr==1)
			cout<<ans<<"\n";
		else
			cout<<"Bad magician!\n";
	}

	//system("pause");
}