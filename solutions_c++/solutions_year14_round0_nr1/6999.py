#include<iostream>
#include<vector>


using namespace std;

	int grid1 [4][4];
	int grid2 [4][4];
	vector <int> answer ;

void read(int array [4][4])
{
	for(int m=0;m<4;m++)
	{
		for(int n=0;n<4;n++)
		{
				cin>>array[m][n];
		}
	}
}

void detect(int x, int y)
{
	int v=0;
	int i,j,k;
	x=x-1;
	y=y-1;
	for(i=0;i<4;i++)
	{
		for(j=0;j<4;j++)
		{
			if(grid1[x][i]==grid2[y][j])
			{
				v++;
				k=grid1[x][i];
			}
		}
	}

	if(v==1)
	{cout<<k<<endl;}
	else if(v==0)
	{cout<<"Volunteer cheated!"<<endl;}
	else
	{cout<<"Bad magician!"<<endl;}

}

int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("solution.out","w",stdout);
	int t,a1,a2;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		cin>>a1;
		read(grid1);
		cin>>a2;
		read(grid2);
		cout<<"Case #"<<i<<": ";
		detect(a1,a2);
		
	}

	return 0;
}