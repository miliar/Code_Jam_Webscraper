#include<iostream>
using namespace std;
int main()
{
	int t,k=0;
	cin>>t;
	while(k++!=t)
	{
		int i,j,first,second,c=0,a[4][4],b[4][4],y=0;
		cin>>first;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				cin>>a[i][j];
			}
		}
		cin>>second;
                for(i=0;i<4;i++)
                {
                        for(j=0;j<4;j++)
                        {
                                cin>>b[i][j];
                        }
                }
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				if(a[first-1][i]==b[second-1][j])
				{
					c++;
					y=a[first-1][i];
				}
			}
		}
		if(c==0)
			cout<<"Case #"<<k<<": Volunteer cheated!"<<endl;
		else if (c==1)
			cout<<"Case #"<<k<<": "<<y<<endl;
		else
			cout<<"Case #"<<k<<": Bad magician!"<<endl;
	}
	return 0;
}
