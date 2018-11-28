#include <iostream>
#include<vector>
using namespace std;

int main() {
	int t,l;
	cin>>t;
	l=t;
	while(t--)
	{
		int i,j,a[4][4],b[4][4],m,n;
		vector <int> o;
		cin>>m;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				cin>>a[i][j];
			}
		}
		cin>>n;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				cin>>b[i][j];
			}
		}
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				if(a[m-1][i]==b[n-1][j])
				o.push_back(a[m-1][i]);
			}
		}
		cout<<"Case #"<<l-t<<": ";
		if(o.size()==1)
		cout<<o[0]<<endl;
		else if(o.size()==0)
		cout<<"Volunteer cheated!"<<endl;
		else
		cout<<"Bad magician!"<<endl;
	}
	return 0;
}