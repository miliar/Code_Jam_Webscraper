#include <iostream>
using namespace std;

int main()
{
	long long int r , t , T , sum , count , nsum , nsum1;
	cin >> T;
	for(long long int i = 0 ; i < T ; i++)
	{
		cin >> r;
		cin >> t;
		sum = 2 * r + 1;
		nsum = 2 * r + 1;
		count = 0;
		for(long long int j = 0 ; sum <= t ; j++)
		{
			nsum = nsum + 4;
			sum = sum + nsum;
			count++;
		}
		cout << "Case #" << i+1 << ": " << count << endl;
	}
	return 0;
}
