#include <iostream>
using namespace std;
int main()
{
    int c[4][4],c1[4][4],c2[4],c3[4];
	int a1,a2,t,k=0,ans;
cin>>t;
	int T=t;
	while(t--)
	{
		k=0;
	cin>>a1;
		for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
	cin>>c[i][j];
	cin>>a2;;
		for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
		cin>>c1[i][j];
	
		for(int i=0;i<4;i++)
			c2[i]=c[a1-1][i];
		for(int i=0;i<4;i++)
			c3[i]=c1[a2-1][i];
		for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
		{
			if(c3[i]==c2[j])
			{
				k++;
				ans=c3[i];
			}
		}
		if(k>1)
			cout<<"Case #"<<T-t<<": Bad magician!"<<endl;
		else if(k==1)
			cout<<"Case #"<<T-t<<": "<<ans<<endl;
		else
			cout<<"Case #"<<T-t<<": Volunteer cheated!"<<endl;
	}
}