#include<iostream>
using namespace std;
int main()
{
	int t;cin>>t;
	for(int k=0;k<t;k++)
	{
		int r1,r2;
		int m1[4][4],m2[4][4];
		cin>>r1;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				cin>>m1[i][j];
		cin>>r2;
		int n=0,count=0;
		for(int i=0;i<4;i++)
                        for(int j=0;j<4;j++)
                                cin>>m2[i][j];
		for(int i=0;i<4;i++)
                {
		        for(int j=0;j<4;j++)
                        {
				if(m1[r1-1][i]==m2[r2-1][j])
				{
					++count;n=m1[r1-1][i];
				}
			}
		}
		if(count==1)
		cout<<"Case #"<<k+1<<": "<<n<<endl;
		else if(count>1)
		cout<<"Case #"<<k+1<<": "<<"Bad magician!"<<endl;
 		else if(count==0)
		cout<<"Case #"<<k+1<<": "<<"Volunteer cheated!"<<endl;
	}
}
       	
