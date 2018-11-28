#include <iostream>
using namespace std;
int x[5][5],y[5][5];
bool tt[17];
int main()
{
	int t,a,b;
	cin>>t;
	for (int i=0;i<t;++i)
	{
		for (int j=1;j<17;++j)
			tt[j]=false;
		cin>>a;
		for (int j=1;j<5;++j)
			for (int k=1;k<5;++k)
				cin>>x[j][k];
		for (int k=1;k<5;++k)
			tt[x[a][k]]=true;
		bool ttt=false,ttt2=false;
		int xx=0;
		cin>>b;
		for (int j=1;j<5;++j)
			for (int k=1;k<5;++k)
				cin>>y[j][k];
		for (int k=1;k<5;k++)
			if (tt[y[b][k]])
			{
				if (!ttt)
				{
					ttt=true;
					xx=y[b][k];
				}
					else ttt2=true;
			}
		cout<<"case #"<<i+1<<": ";
		if (ttt)
		{
			if (ttt2)
				cout<<"Bad magician!"<<endl;
				else cout<<xx<<endl;
		}
		else cout<<"Volunteer cheated!"<<endl;
	}
} 
