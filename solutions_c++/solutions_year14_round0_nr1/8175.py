#include<iostream>
#include<vector>
using namespace std;
vector<int> V;
int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("Magic_Trick.out","w",stdout);
	int T,R1,Arr1[4][4],R2,Arr2[4][4],A,B,C,D,Ind[4];
	cin>>T;
	for(int CASE=1 ; CASE<=T ; CASE++)
	{
		V.clear();
		cin>>R1;
		for(int i=0 ; i<4 ; i++)
		{
			for(int j=0 ; j<4 ; j++)
			{
				cin>>Arr1[i][j];
			}
		}
		A=Arr1[R1-1][0],B=Arr1[R1-1][1],C=Arr1[R1-1][2],D=Arr1[R1-1][3];
		cin>>R2;
		for(int i=0 ; i<4 ; i++)
		{
			for(int j=0 ; j<4 ; j++)
			{
				cin>>Arr2[i][j];
				if(i==R2-1 && (Arr2[i][j]==A || Arr2[i][j]==B || Arr2[i][j]==C || Arr2[i][j]==D ))
				{
					V.push_back(Arr2[i][j]);
				}
			}
		}
		cout<<"Case #"<<CASE<<": ";
		if(V.size()==1)
			cout<<V[0]<<endl;
		else if(V.size()==0)
			cout<<"Volunteer cheated!\n";
		else
			cout<<"Bad magician!\n";
	}
}