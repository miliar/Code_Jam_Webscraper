#include<iostream>
#include<vector>
using namespace std;
int main()
{
	freopen("A-small-attempt2.in","r",stdin);
	freopen("out.in","w",stdout);
	int cas=0;
	int t;
	cin>>t;
	while(t--)
	{

		cas++;
		int p;
		cin>>p;
		vector<vector<int>>v(4,vector<int>(4));

		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				cin>>v[i][j];

		vector<int>v2(4);

		for(int i=0;i<4;i++)
			v2[i]=v[p-1][i];

		v.clear();
		v.resize(4,vector<int>(4));
		cin>>p;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				cin>>v[i][j];

		vector<int>v3(4);

		for(int i=0;i<4;i++)
			v3[i]=v[p-1][i];


		int count=0;
		int posV2;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				if(v2[i]==v3[j])
				{count++;posV2=i;}

				if(count==1)
					cout<<"Case #"<<cas<<": "<<v2[posV2]<<endl;
				else
					if(count==0)
						cout<<"Case #"<<cas<<": "<<"Volunteer cheated!"<<endl;
					else
						cout<<"Case #"<<cas<<": "<<"Bad magician!"<<endl;


				//v.clear();v2.clear();v3.clear();
	}



}