#include <bits/stdc++.h>
#define ll long long int
using namespace std;
int main()
{
	ll t,i,j,k,a,b,card1[6][6],card2[6][6];
	cin>>t;
	for(i=1; i<=t; i++)
	{
		cin>>a;
		for(j=1; j<=4; j++)
			for(k=1; k<=4; k++)
				cin>>card1[j][k];
		cin>>b;
		for(j=1; j<=4; j++)
			for(k=1; k<=4; k++)
				cin>>card2[j][k];
		int first=0,second=0;
		for(j=1; j<=4; j++)
		{
			for(k=1; k<=4; k++)
			{
				if(card1[a][j]==card2[b][k])
				{
					if(first==0)
						first=card1[a][j];
					else
					{
						second=card2[a][j];
						break;
					}
				}
			}
			if(second)
				break;
		}
		if(second)
			cout<<"Case #"<<i<<": Bad magician!\n";
		if(first&&!second)
			cout<<"Case #"<<i<<": "<<first<<"\n";
		if((!first)&&(!second))
			cout<<"Case #"<<i<<": Volunteer cheated!\n";
	}
	return 0;
}