//Email:kingshuk1000@gmail.com

//Just for fun :P

#include<iostream>

using namespace std;

int main()
{
	int i,j,k;

	freopen("A-small-attempt0.in", "rt", stdin);
	freopen("A-small.out","wt",stdout);
	int T;
	cin>>T;
	
	for(i=0;i<T;i++)
	{
		int r1,r2;
		int m1[4][4],m2[4][4];


		cin>>r1;
		r1=r1-1;
		for(j=0;j<4;j++)
			{for(k=0;k<4;k++)
			{
				cin>>m1[j][k];
				
			}
		
		}


		
		cin>>r2;
		r2=r2-1;
		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			{
				cin>>m2[j][k];
				
			}
			
		}

				
		int ans,cnt;
		
				ans=-1;
				cnt=0;
		for(j=0;j<4;j++)
			{
				
				for(k=0;k<4;k++)
			{
				
				if(m1[r1][j]==m2[r2][k])
				{
					ans=m1[r1][j];
					cnt++;
				}
			}
		}


			cout<<"Case #"<<i+1<<": ";
			if(cnt==1)
			{

				cout<<ans<<endl;
			}
			else if(cnt>1)
			{
				cout<<"Bad magician!"<<endl;
			}
			else
			{
				cout<<"Volunteer cheated!"<<endl;
			}

	}




}