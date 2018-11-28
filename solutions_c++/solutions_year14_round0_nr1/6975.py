#include<iostream>

using namespace std;

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.in","w",stdout);
	int T;
	cin>>T;
	for(int t=1;t<=T;++t)
	{
		int r1,r2;
		int a[4][4],b[4][4],c[4],idx;
		cin>>r1;
		for(int i=0;i<4;++i)
			for(int j=0;j<4;++j)
				cin>>a[i][j];
		cin>>r2;
		for(int i=0;i<4;++i)
			for(int j=0;j<4;++j)
				cin>>b[i][j];
		for(int i=0;i<4;++i)
			c[i]=a[r1-1][i];
		int count=0,y;
		for(int j=0;j<4;++j){
			for(int i=0;i<4;++i)
				if(c[j]==b[r2-1][i]){
					count++;
					y=c[j];
					break;
				}
		}
		cout<<"Case #"<<t<<": ";
		if(count==1)	cout<<y<<endl;
		else if(count>1)	cout<<"Bad magician!"<<endl;
		else	cout<<"Volunteer cheated!"<<endl;
	}
	return 0;
}