#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t,x;
	cin >> t;
	int row1,row2;
	int a[4], b[4];
	for(int k=1;k<=t;k++)
	{
		cin >> row1;
		for(int i=1;i<=4;i++)
		{
			if(i==row1)
			{
				cin >> a[0];
				cin >> a[1];
				cin >> a[2];
				cin >> a[3];
			}else
			{
				cin >> x;
				cin >> x;
				cin >> x;
				cin >> x;
			}
		}
		cin >> row2;
		for(int i=1;i<=4;i++)
		{
			if(i==row2)
			{
				cin >> b[0];
				cin >> b[1];
				cin >> b[2];
				cin >> b[3];
			}else
			{
				cin >> x;
				cin >> x;
				cin >> x;
				cin >> x;
			}
		}
		int c=0;
		int match = 0;
		for(int i=1; i<=4;i++)
		{
			for(int j=1;j<=4; j++)
			{
				if (a[i-1]==b[j-1])
				{
					match = a[i-1];
					c++;
					break;
				}
			}
		}
		if (c==0)
		cout << "Case #" << k << ": Volunteer cheated!\n";
		if(c==1)
		cout << "Case #" << k << ": " << match << "\n";
		if(c>1)
		cout << "Case #" << k << ": Bad magician!\n";
	}
	return 0;
}
