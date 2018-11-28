#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	
	int t;
	cin>>t;
	int ar1[4][4],ar2[4][4],b,c;
	int m=1;
	while(t--)
	{
		cin>>b;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				cin>>ar1[i][j];
		cin>>c;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				cin>>ar2[i][j];
		int k=0,z=0;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				if(ar1[b-1][i]==ar2[c-1][j])
				{
					z=ar1[b-1][i];
				k++;
				}
			}
		}
		
		if(k==1)
		cout<<"Case #"<<m<<": "<<z<<endl;
		else if(k==0)
		cout<<"Case #"<<m<<": Volunteer cheated!"<<endl;
		else
		cout<<"Case #"<<m<<": Bad magician!"<<endl;
		m++;
	}
	return 0;
}
