#include <iostream>
using namespace std;

int main()
{
	int T,flag,t=1,pos;
	cin>>T;
	int m,n,x[4][4], y[4][4];
	while(t<=T)
	{
		flag = 0;
		cin>>m;
		for(int i=0; i<4; i++)
		for(int j=0; j<4; j++)
		{
			cin>>x[i][j];
		}
		cin>>n;
		for(int i=0; i<4; i++)
		for(int j=0; j<4; j++)
		{
			cin>>y[i][j];
		}
		for(int i=0; i<4; i++)
		for(int j=0; j<4; j++)
		{
			if((x[m-1][i]==y[n-1][j])&&(flag==0))
			{
				flag = 1;
				pos = i;
			}
			else if((x[m-1][i]==y[n-1][j])&&(flag==1))
			{
				cout<<"Case #"<<t<<": Bad magician!\n";
				goto end;
			}
		}
		if(flag==0)
		{
			cout<<"Case #"<<t<<": Volunteer cheated!\n";
		}
		else
		{
			cout<<"Case #"<<t<<": "<<x[m-1][pos]<<"\n";
		}
		
		end:
		t++;
	}

	return 0;
}
