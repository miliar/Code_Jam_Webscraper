#include <iostream>
using namespace std;

int main() 
{
	int T,s1,s2,c,s;
	int d1[4],d2[4],d3[12];
	cin>>T;
	for (int i=1;i<=T;i++)
	{
		c=0;
		s=0;
		cout<<"Case #";
		cout<<i<<": ";
		cin>>s1;
		if(s1 == 1)
		{
		for (int j=0;j<4;j++)
		{
			cin>>d1[j];
		}
		for (int k=0;k<12;k++)
		{
			cin>>d3[k];
		}
		}
		if(s1 == 2)
		{
		for (int j=0;j<4;j++)
		{
			cin>>d3[j];
		}
		for (int k=0;k<4;k++)
		{
			cin>>d1[k];
		}
		for (int j=0;j<8;j++)
		{
			cin>>d3[j];
		}
		}
		if(s1 == 3)
		{
		for (int j=0;j<8;j++)
		{
			cin>>d3[j];
		}
		for (int k=0;k<4;k++)
		{
			cin>>d1[k];
		}
		for (int j=0;j<4;j++)
		{
			cin>>d3[j];
		}
		}
		if(s1 == 4)
		{
		for (int j=0;j<12;j++)
		{
			cin>>d3[j];
		}
		for (int k=0;k<4;k++)
		{
			cin>>d1[k];
		}
		}
		cin>>s2;
		if(s2 == 1)
		{
		for (int j=0;j<4;j++)
		{
			cin>>d2[j];
		}
		for (int k=0;k<12;k++)
		{
			cin>>d3[k];
		}
		}
		if(s2 == 2)
		{
		for (int j=0;j<4;j++)
		{
			cin>>d3[j];
		}
		for (int k=0;k<4;k++)
		{
			cin>>d2[k];
		}
		for (int j=0;j<8;j++)
		{
			cin>>d3[j];
		}
		}
		if(s2 == 3)
		{
		for (int j=0;j<8;j++)
		{
			cin>>d3[j];
		}
		for (int k=0;k<4;k++)
		{
			cin>>d2[k];
		}
		for (int j=0;j<4;j++)
		{
			cin>>d3[j];
		}
		}
		if(s2 == 4)
		{
		for (int j=0;j<12;j++)
		{
			cin>>d3[j];
		}
		for (int k=0;k<4;k++)
		{
			cin>>d2[k];
		}
		}
		for (int l=0;l<4;l++)
		{
			for (int u=0;u<4;u++)
			{
				if (d1[l] == d2[u])
				{
					c++;
					s = d1[l];
				}
			}
		}
		if (c == 1)
		{
			cout<<s<<endl;
		}
		else if (c > 1)
		{
			cout<<"Bad magician!"<<endl;
		}
		else if (c == 0)
		{
			cout<<"Volunteer cheated!"<<endl;
		}
		
	}
	return 0;
}