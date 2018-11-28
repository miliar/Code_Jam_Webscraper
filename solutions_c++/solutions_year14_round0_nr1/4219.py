#include <iostream>
using namespace std;
int main()
{
	int T;
	cin >> T;
	for(int i=1; i<=T; i++)
	{
		
		int arr[4][4];
		int r;
		cin >> r;
		r--;
		for(int j = 0; j<4; j++)
			for(int k = 0; k<4; k++)
			{
				cin >> arr[j][k];
			}
		int arr2[4][4];
		int r2;
		cin >> r2;
		r2--;
		for(int j = 0; j<4; j++)
			for(int k = 0; k<4; k++)
			{
				cin >> arr2[j][k];
			}
		int candidate = 0;
		int cancount = 0;
		for(int j = 0; j<4; j++)
		{
			bool match = false;
			for(int k = 0; k<4; k++)
			{
				//cout << arr2[r2][k] << " " << arr[r][j]<<endl;
				if(arr2[r2][k] == arr[r][j])
				{
					cancount ++;
					candidate = k;
				}
			}
		}
		
		if(cancount == 0) cout<<"Case #"<<i<<": Volunteer cheated!"<<endl;
		if(cancount > 1) cout<<"Case #"<<i<<": Bad magician!"<<endl;
		if(cancount == 1) cout<<"Case #"<<i<<": "<<arr2[r2][candidate]<<endl;
	}
}
