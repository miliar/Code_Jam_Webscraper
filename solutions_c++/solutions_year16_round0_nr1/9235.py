#include <iostream>
using namespace std;

int main()
{
	int i, j, k, T, N, currentNum;
	int nums[10];
	bool check;
	
	cin >> T;
	for(i = 0; i < T; ++i)
	{
		cin >> N;
		
		if(N != 0)
		{
			for(j = 0; j < 10; ++j)
				nums[j] = 0;
			
			for(j = 1; j > 0; ++j)
			{
				check = 1;
				currentNum = j*N;
				while(currentNum > 0)
				{
					nums[currentNum % 10] = 1;
					currentNum = currentNum/10;
				}
				for(k = 0; k < 10; ++k)
				{
					if(nums[k] == 0)
					{
						check = 0;
					}
				}
				if (check == 1)
					break;
			}
			cout << "Case #" << i + 1 << ": " << j*N << endl;
		}
		else
			cout << "Case #" << i + 1 << ": " << "INSOMNIA" << endl;
	}
}
