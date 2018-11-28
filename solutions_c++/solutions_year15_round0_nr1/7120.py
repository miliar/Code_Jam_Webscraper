// Google Code Jam 2015
// Problem A. Standing Ovation
// Borui Lin (Boris)
// boruilin224@gmail.com

#include <iostream>
using namespace std;

int main()
{
	int n,i,j,max,total,ans;
	char ch;
	cin >> n;
	for (i=0; i<n; i++)
	{
		cin >> max;
		total=0;
		ans=0;
		ch=getchar();
		for (j=0; j<=max; j++)
		{
			ch=getchar();
			while (ch<'0' || ch>'9') ch=getchar();
			if (total>=j) total+=ch-48;
			else if (ch>'0')
			{
				ans+=j-total;
				total+=j-total+ch-48;
			}
		}
		cout << "Case #" << i+1 << ": " << ans << endl;
	}
	return 0;
}