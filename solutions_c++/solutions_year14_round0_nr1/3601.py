#include<bits/stdc++.h>

using namespace std;

int main(void)
{
	int t;
	cin >> t;
	for(int T=1;T<=t;T++)
	{
		int arr[4][4];
		int brr[4][4];
		int r1,r2;
		cin >> r1;
		r1-=1;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cin>>arr[i][j];
			}
		}
		cin >> r2;
		r2-=1;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cin >> brr[i][j];
			}
		}
		int count = 0;
		int x = -1;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				if(arr[r1][i] == brr[r2][j])
				{
					x = arr[r1][i];
					count++;
				}
			}
		}
		
		cout << "Case #" << T << ": "; 
		
		if(count == 1)
		{
			cout << x << endl;
		}
		else if(count > 1)
		{
			cout << "Bad magician!" << endl;
		}
		else if(count == 0)
		{
			cout << "Volunteer cheated!" << endl;
		}
	}
}
	
