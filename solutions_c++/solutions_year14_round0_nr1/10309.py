#include<iostream>
#include<map>
using namespace std;

int main()
{
	int T,A,B,A1[4][4],B1[4][4],val,count,i,j,cas=1;
	map<int,int> M;
	cin>>T;
	while(T--)
	{
		count=0;
		cin>>A;A-=1;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				cin>>A1[i][j];
			}
		}
		cin>>B;B-=1;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				cin>>B1[i][j];
			}
		}
		for(i=0;i<4;i++)
		{
			M[A1[A][i]]=1;
		}
		for(i=0;i<4;i++)
		{
			if(M.find(B1[B][i])!=M.end())
			{
				count++;
				val=B1[B][i];
			}
		}
		if(count==0)cout<<"Case #"<<cas<<": Volunteer cheated!\n";
		else if(count==1)cout<<"Case #"<<cas<<": "<<val<<"\n";
		else cout<<"Case #"<<cas<<": Bad magician!\n";
		M.clear();cas++;
	}
}
