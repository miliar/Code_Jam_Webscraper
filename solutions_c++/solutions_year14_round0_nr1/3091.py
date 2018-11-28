#include<iostream>
using namespace std;
int main()
{
	int T;
	cin>>T;
	int no=1;
	while(T--)
	{
		int a,b;
		cin>>a;
		bool an[17]={0};
		int ans=0;
		for(int i=1;i<=4;i++)
		{
			int temp;
			if(i!=a){
				for(int j=0;j<4;j++)cin>>temp;
			}else{
				for(int j=0;j<4;j++)
				{
					cin>>temp;
					an[temp]=true;
				}
			}
		}
		cin>>b;
		for(int i=1;i<=4;i++)
		{
			int temp;
			if(i!=b){
				for(int j=0;j<4;j++)cin>>temp;
			}else{
				for(int j=0;j<4;j++)
				{
					cin>>temp;
					if(an[temp]==true)
					{
						if(ans==0)
							ans=temp;
						else
							ans=-1;
					}
				}
			}
		}
		cout<<"Case #"<<no<<": ";
		if(ans>0)	
			cout<<ans<<endl;
		else if(ans==0)
			cout<<"Volunteer cheated!\n";
		else
			cout<<"Bad magician!\n";
		no++;
	}
}

