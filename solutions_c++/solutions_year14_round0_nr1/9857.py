#include <iostream>
using namespace std;

int main() {
		int i,j,a[4][4],b[4][4],count,t,m,r1,r2,no;
	cin>>t;
	for(m=1;m<=t;m++)
	{ count=0;
		cin>>r1;
		for(i=0;i<4;i++)
		for(j=0;j<4;j++)
		cin>>a[i][j];
		cin>>r2;
		for(i=0;i<4;i++)
		for(j=0;j<4;j++)
		cin>>b[i][j];
		for(i=0;i<4;i++)
		for(j=0;j<4;j++)
		{
			if(a[r1-1][i]==b[r2-1][j]) { count++; no=a[r1-1][i];}
		}
		if(count==1) cout<<"Case #"<<m<<": "<<no<<endl;
		else if(count>1)  cout<<"Case #"<<m<<": "<<"Bad magician!"<<endl;
		else if(count==0) cout<<"Case #"<<m<<": "<<"Volunteer cheated!"<<endl;
	}
	return 0;
}