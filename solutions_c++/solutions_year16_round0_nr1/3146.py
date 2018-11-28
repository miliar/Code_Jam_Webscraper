#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<sstream>
#include<functional>
#include<numeric>

using namespace std;

int main()
{
	int cases;
	cin >> cases;

	for(int i=1; i<=cases; i++)
	{
		long long n;
		cin >> n;

		vector<int> seen(10, 0);

		long long at = n;
		for(int j=0; j<=1000000; j++)
		{
			stringstream parse;;
			string temp;
			parse << at;
			parse >> temp;

			for(size_t k=0; k<temp.size(); k++)
			{
				seen[temp[k] - '0'] = 1;
			}


			if(accumulate(seen.begin(), seen.end(), 0) == 10)
			{
				break;
			}
			at += n;
		}
		if(accumulate(seen.begin(), seen.end(), 0) == 10)
		{
			cout << "Case #" << i << ": " << at << endl;
		}
		else
		{
			cout << "Case #" << i << ": INSOMNIA" << endl;;

		}

	}

	return 0;
}
