#include<iostream>
using namespace std;
int main()
{
	freopen("A-small-attempt1.in","r",stdin);
	freopen("A.out","w",stdout);
	int a[4][4],b[4][4],i,j,fir,sec,t;
	cin>>t;
	int cas=0;
	while(t--)
	{
		cin>>fir;
		fir--;	
		cas++;
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
			{
				cin>>a[i][j];
			}
		cin>>sec;
		sec--;
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
			{
				cin>>b[i][j];
			}
		int cnt=0;
		for(i=0;i<4;i++)
		for(j=0;j<4;j++)
		{
			if(a[fir][i]==b[sec][j])
			{
				cnt++;
				//b[sec][j]=-1;
			}		
		}
		//cout<<cnt<<endl;
		if(cnt==1)
		for(i=0;i<4;i++)
		for(j=0;j<4;j++)
		{
			if(a[fir][i]==b[sec][j])
			{
				cout<<"Case #"<<cas<<": "<<a[fir][i]<<endl;
			    break;
			}
		
		}
		else if(cnt>1)
		cout<<"Case #"<<cas<<": "<<"Bad magician!"<<endl;
		else
		cout<<"Case #"<<cas<<": "<<"Volunteer cheated!"<<endl;		
	}
	return 0;
}
