#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<bool> visited(10);

bool is_visited()
{
	for(int i = 0; i < 10; ++i)
		if(!visited[i])
			return false;
	return true;
}

int main()
{
	int test_case;
	long n;
	cin >> test_case;
	for(int i = 1; i <= test_case; ++i)
	{
		cin >> n;
		if(n == 0)
		{
			cout << "Case #" << i << ": " << "INSOMNIA" << "\n";
		}
		else
		{
			for(int j = 0; j < 10; ++j)
				visited[j] = false;
			long long temp = n;
			long long counter = 1;
			while(!is_visited())
			{
				temp = counter * n;
				while(temp)
				{
					visited[temp%10] = true;
					temp /= 10; 
				}
				++counter;
			}
			cout << "Case #" << i << ": " << (counter - 1) * n << "\n";
		}
	}
}
