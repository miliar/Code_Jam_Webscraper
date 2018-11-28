#include<iostream>
using namespace std;

int main()
{
	//freopen("A-small-attempt0.in","r",stdin);
	//freopen("trick.txt","w",stdout);
	int t;
	cin>>t;
	for(int tt=1;tt<=t;++tt)
	{
		int r1,r2,m1[4][4],m2[4][4];
		cin>>r1;
		--r1;
		for(int i=0;i<4;++i)
			for(int j=0;j<4;++j)
				cin>>m1[i][j];
		cin>>r2;
		--r2;
		for(int i=0;i<4;++i)
			for(int j=0;j<4;++j)
				cin>>m2[i][j];
				
		int count=0,index;
		for(int i=0;i<4;++i)
		{
			for(int j=0;j<4;++j)
			{
				if(m1[r1][i]==m2[r2][j])
				{
					index=i;
					++count;
					break;
				}
			}
		}
		if(count==0)
			cout<<"Case #"<<tt<<": Volunteer cheated!\n";
		else if(count==1)
			cout<<"Case #"<<tt<<": "<<m1[r1][index]<<endl;
		else
			cout<<"Case #"<<tt<<": Bad magician!\n";
	}
	return 0;
}
