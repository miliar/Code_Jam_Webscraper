#include <iostream>
using namespace std;

int main()
{
	int t;
	cin>>t;
	for(int i=1; i<=t; i++)
	{
		int r1,r2;
		int a[5][5], b[5][5];
		cin >> r1;
		for(int j=1; j<5; j++)
		{
			for(int k=1; k<5; k++)
			{
				cin >> a[j][k];
			}
		}
		cin >> r2;
		for(int j=1; j<5; j++)
		{
			for(int k=1; k<5; k++)
			{
				cin >> b[j][k];
			}
		}
		int cnt=0;
		int number;
		for(int j=1; j<5; j++)
		{
			for(int k=1; k<5; k++)
			{
				if(a[r1][j]==b[r2][k]){
					 cnt++;
					 number = a[r1][j];
				 }
			}
		}
		if(cnt==0) cout << "Case #" << i <<": Volunteer cheated!\n";
		else if(cnt==1) cout << "Case #" << i << ": " << number << endl;
		else cout << "Case #" << i <<": Bad magician!\n";

	};
}
