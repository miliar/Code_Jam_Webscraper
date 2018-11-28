#include "iostream"
using namespace std;

int mp1[4][4];
int mp2[4][4];


int T;
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	
	
	cin>>T;
	for(int t=1;t<=T;t++)
	{
		int ans=0;
		int sa=0;
		int r1=0,r2=0;
		cin>>r1;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				cin>>mp1[i][j];
		cin>>r2;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				cin>>mp2[i][j];
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
			{
				if(mp1[r1-1][i]==mp2[r2-1][j])
				{
					ans=mp1[r1-1][i];
					sa++;
				}
			}
			
		cout<<"Case #"<<t<<": ";
		if(sa == 0) cout<<"Volunteer cheated!"<<endl;
		else if(sa==1) cout<<ans<<endl;
		else cout<<"Bad magician!"<<endl;
	}
	return 0;
}