#include<iostream>
#include<algorithm>
#include<vector>
#include<stdio.h>

using namespace std;

int main()
{
	int t,c=1;
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	cin >> t;
	while(t)
	{
		int row,x;
		vector<int> cards;
		for(int k=0;k<2;k++)
		{
			cin >> row;
			for(int i=1;i<=4;i++)
			{
				for(int j=1;j<=4;j++)
				{
					cin >> x;
					if(i==row)
						cards.push_back(x);
				}
			}
		}
		int ans = -1;
		for(int i=0;i<cards.size();i++)
		{
			if(count(cards.begin(),cards.end(),cards[i])==2)
			{
				if(ans==-1)
					ans = cards[i];
				else if(ans!=cards[i])
				{
					ans = -2;
					break;
				}
			}
		}
		if(ans==-1)
			cout << "Case #" << c << ": Volunteer cheated!" << endl;
		else if(ans == -2)
			cout << "Case #" << c << ": Bad magician!" << endl;
		else
			cout << "Case #" << c << ": " << ans << endl;
		t--;
		c++;
	}
	return 0;
}