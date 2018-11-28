#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>

using namespace std;

int main()
{

	ifstream cin("A-small-attempt2.in");
	ofstream cout("output.txt");

	long long t;
	cin >> t;

	for(long long cs = 1; cs <= t; cs++)
	{
		long long a,n;
		cin >> a >> n;

		vector<long long> vec;

		while(n--)
		{
			long long x;
			cin >> x;
			vec.push_back(x);
		}

		sort(vec.begin(),vec.end());

		long long cur_size = a;
		long long cnt = 0;

		for(long long i=0;i<vec.size();i++)
		{
			if(cur_size > vec[i])
			{
				cur_size += vec[i];
			}
			else
			{
				if(cur_size <= 1)
				{
					cnt += vec.size() - (i);
					break;
				}

				int tm = 0;

				while(cur_size <= vec[i])
				{
					cur_size += (cur_size-1);
					tm++;

				}

				cur_size += vec[i];

				if(vec.size() - i <= tm)
				{
					cnt += (vec.size() - i);
					break;
				}
				else
					cnt += tm;
			}
		}

		cout << "Case #" << cs << ": " << cnt << endl;

	}

}