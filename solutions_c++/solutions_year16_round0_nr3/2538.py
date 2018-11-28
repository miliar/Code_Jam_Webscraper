#include<iostream>
#include<vector>
#include<numeric>
#include<math.h>

using namespace std;

long long lessprime(long long inputNum)
{
	if (inputNum <= 3)
		return 0;
	if (inputNum % 2 == 0)
		return 2;
	long long sqrtNum = sqrt(inputNum);
	for (long long i = 3; i <= sqrtNum; i += 2)
	{
		if (inputNum % i == 0)
			return i;
	}
	return 0;
}

int main()
{
	int T;
	cin >> T; // T is 1.
	cout << "Case #" << T << ": " <<  endl;
	int N, J;

	cin >> N >> J;
	unsigned int numCvr = 0;
	
	numCvr |= 1;
	numCvr |= (1 << (N - 1));
	
	while (J > 0)
	{
		vector<long long> res_list;
		for (int j = 2; j <= 10; j++)
		{
			long long tmpVal = 1;
			long long base = j;
			for (int k = 1; k < N; k++)
			{
				tmpVal += ((numCvr >> k) & 1) * base;
				base *= j;
			}
			//cout << "numCvr : " << numCvr << " " << "j : " << j << "tmpVal : " << tmpVal << endl;
			long long lspr;
			if ((lspr = lessprime(tmpVal)) == 0)
			{
				//cout << endl << endl;
				break;
			}		
			else
			{
				res_list.push_back(lspr);
				if (10 == j)
				{
					for (int i = N - 1; i >= 0; i--)
					{
						cout << ((numCvr >> i) & 1);
					}
					cout << " ";
					//cout << endl << tmpVal << endl;
					for (int k = 0; k < res_list.size(); k++)
						cout << res_list[k] << " ";
					cout << endl;
					J--;
				}
			}
		}
		numCvr += 2;
	}
}