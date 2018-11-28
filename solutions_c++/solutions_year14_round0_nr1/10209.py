#include<iostream>
using namespace std;
int main()
{
	
	int t,k=1;
	cin>>t;
	while(k<=t)
	{
		int a[4][4],b[4][4];
		int q1,q2,j,i;
		cin>>q1;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			cin>>a[i][j];
		}
		cin>>q2;
			for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			cin>>b[i][j];
		}
		int flag=0,l=0;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
			if(a[q1-1][i]==b[q2-1][j])
				{
				flag++;
				if(flag==1)
				l=a[q1-1][i];
				break;
				}
			}
			
		}
		    if(flag==1)
		    cout<<"Case #"<<k<<":"<<" "<<l<<"\n";
		    else if(flag>1)
           cout<<"Case #"<<k<<":"<<" Bad magician!"<<"\n";
           else if(flag==0)
           cout<<"Case #"<<k<<":"<<" Volunteer cheated!"<<"\n";
           k++;
	}
	return 0;
	
}