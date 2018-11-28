#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
using namespace std;

int Tn;
int row1, row2;
set<int> s1;

int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small.out","w",stdout);

	int i,j;

	cin >> Tn;
	for (int T=1;T<=Tn;T++)
	{
		s1.clear();

		int count = 0;
		int ans;
		int tmp;
		cin >> row1;
		for (i=1;i<=4;i++)
			for (j=1;j<=4;j++)
			{
				cin >> tmp;
				if (i==row1)
					s1.insert(tmp);
			}
		cin >> row2;
		for (i=1;i<=4;i++)
			for (j=1;j<=4;j++)
			{
				cin >> tmp;
				if (i==row2)				
					if (s1.find(tmp)!=s1.end())
					{
						count++;
						ans = tmp;
					}
			}

		cout << "Case #" << T << ": ";
		if (count == 0)
			cout << "Volunteer cheated!" << endl;
		else if (count > 1)
			cout << "Bad magician!" << endl;
		else
			cout << ans << endl;
	}
}