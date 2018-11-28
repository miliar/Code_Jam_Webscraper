#include <iostream>

using namespace std;

int main()
{
	int tc;
	int tm;
	int n;
	int chk[17];
	int cnt;
	int idx;
	cin>>tc;
	for(int k=1;k<=tc;k++)
	{
		cin>>n;
		cnt=0;
		for(int i = 1;i<=16;i++)
			chk[i]=0;
		for(int i=1;i<=4;i++)
		{
			for(int j = 1;j<=4;j++)
			{
				cin>>tm;
				if(i==n) chk[tm]=1;
			}
		}

		cin>>n;
		for(int i=1;i<=4;i++)
		{
			for(int j = 1;j<=4;j++)
			{
				cin>>tm;
				if(i==n) chk[tm]+=2;
			}
		}

		for(int i = 1; i <=16;i++)
		{
			if(chk[i]==3){
				cnt++;
				idx=i;
			}
		}
		
		cout<<"Case #"<<k<<": ";
		if(cnt==0) cout<<"Volunteer cheated!"<<endl;
		else if(cnt==1) cout<<idx<<endl;
		else cout<<"Bad magician!"<<endl;
	}
	return 0;
}