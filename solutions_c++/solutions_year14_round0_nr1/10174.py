#include<iostream>
#include<map>
#include<vector>
using namespace std;
int main()
{
	int t,i,m,n,j,pos=0;
	cin>>t;
	while(t--)
	{
		cin>>m;
		m--;
		pos++;
		vector<vector<int> >mat,v;
		mat.resize(4);
		v.resize(4);
		for(i=0;i<4;i++)
		{
			mat[i].resize(4);
			v[i].resize(4);
		}
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				cin>>mat[i][j];
		cin>>n;
		n--;
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				cin>>v[i][j];
		map<int,int>mp;
		for(i=0;i<4;i++)
			mp[mat[m][i]]=1;
		int count=0,val;
		for(i=0;i<4;i++)
			if(mp.find(v[n][i]) != mp.end())
			{
				count++;
				val=v[n][i];
			}
		if(count==1)
			cout<<"Case #"<<pos<<": "<<val<<endl;
		else if(!count)
			cout<<"Case #"<<pos<<": "<<"Volunteer cheated!\n";
		else
			cout<<"Case #"<<pos<<": "<<"Bad magician!\n";
	}
	return 0;
}
