#include<stdio.h>
#include<iostream>
using namespace std;
int main()
{
	int T;
	int card[5][5];
	int i,j;
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A.out","w",stdout);
	cin>>T;
	int t;
	for(t = 1;t <= T; t ++)
	{
		int ans;
		int row1;
		int row2;
		cin >> row1;
		int card1[5];
		int card2[5];
		for(i = 1;i <= 4;i ++)
		{
			for(j = 1;j <= 4;j ++)
			{
				cin>>card[i][j];
				if(i == row1)
				{
					card1[j] = card[i][j];
				}
			}
		}
		cin >> row2;
		int count = 0;
		for(i = 1;i <= 4;i ++)
		{
			for(j = 1;j <= 4;j ++)
			{
				cin>>card[i][j];
				if(i == row2)
				{
					card2[j] = card[i][j];
				}
			}
		}
		for(i = 1;i <= 4;i ++)
		{
			for(j = 1;j <= 4;j ++)
			{
				if(card1[i] == card2[j])
				{
					count ++;
					ans = card1[i];
				}
			}
		}
		if(count == 1)
		{
			cout<<"Case #"<<t<<": "<<ans<<endl;
		}
		else if(count >= 2)
		{
			cout<<"Case #"<<t<<": Bad magician!"<<endl;
		}
		else if(count == 0)
		{
			cout<<"Case #"<<t<<": Volunteer cheated!"<<endl;
		}
	}
	return 0;
}