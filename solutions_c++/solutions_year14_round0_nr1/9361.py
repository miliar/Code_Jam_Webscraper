#include <iostream>

using namespace std;

int main(void)
{
	int T;
	cin >> T;
	for(int i=1; i<=T; i++)
	{	
		int r;
		int arr[17]={0};
		cin >> r;
		int temp;
		for(int j=1; j<5; j++)
		{
			for(int k=0; k<4; k++)
			{
				cin >> temp;
				if(r==j)
				{
					arr[temp]=1;
				}
			}

		}
		int r2;
		cin >> r2;
		//int arr2[17]={0};
		int ans;
		int count=0;
		for(int j=1; j<5; j++)
		{
			for(int k=0; k<4; k++)
			{
				cin >> temp;
				if(r2==j)
				{
					if(arr[temp]==1)
					{
						count++;
						ans=temp;

					}
					
				}
			}

		}
		if(count==0)
		{

			cout << "Case #" << i << ": Volunteer cheated!" << endl;
		}
		else if(count==1)
		{
			cout << "Case #" << i << ": " << ans << endl;

		}
		else
		{
			cout << "Case #" << i << ": Bad magician!" << endl;

		}

	}



	return 0;
}