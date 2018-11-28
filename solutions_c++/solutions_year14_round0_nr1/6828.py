#include <iostream>
using namespace std;

int main() {
	int a,b,i,j,k,t,x[4][4],y[4][4],cnt,m;
	cin>>t;
	for(k=1;k<=t;k++)
	{
		cnt=0;
		cin>>a;
		a--;
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				cin>>x[i][j];
		cin>>b;
		b--;
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				cin>>y[i][j];
				
	for(i=0;i<4;i++)
		for(j=0;j<4;j++)
			if(x[a][i]==y[b][j])
			{
			cnt++;
			m=x[a][i];
			}
	if(cnt==0)
	{
		cout<<"Case #"<<k<<": "<<"Volunteer cheated!"<<endl;
	}
	else if(cnt==1)
	{
		cout<<"Case #"<<k<<": "<<m<<endl;
	}
	else
	{
		cout<<"Case #"<<k<<": "<<"Bad magician!"<<endl;
	}
			
	}
	
	return 0;
}
