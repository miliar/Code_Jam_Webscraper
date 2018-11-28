#include<iostream>
using namespace std;
int n,m;
int Grass[128][128];
bool Check()
{
	for (int i=0;i<n;++i)
	for (int j=0;j<m;++j)
	{
		bool flag1=true,flag2=true;
		for (int k=0;k<m;++k)
		if (Grass[i][k] > Grass[i][j]) flag1=false;
		for (int k=0;k<n;++k)
		if (Grass[k][j] > Grass[i][j]) flag2=false;
		if ( (!flag1) && (!flag2) ) return false;
		
	}
	return true;
}
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("ans-B-Large.txt","w",stdout);
	int CaseN;
	cin>>CaseN;
	for (int i=1;i<=CaseN;++i)
	{
		cin>>n>>m;
		for (int j=0;j<n;++j)
		for (int k=0;k<m;++k)
		cin>>Grass[j][k];
		if (Check())
		{
			cout<<"Case #"<<i<<": YES\n";
		} else
			cout<<"Case #"<<i<<": NO\n";
	}
	return 0;
}
