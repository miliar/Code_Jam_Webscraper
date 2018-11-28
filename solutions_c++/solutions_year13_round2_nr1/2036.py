#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

long Motes()
{
	long x, n;
	long a[100];
	cin >> x >> n;
	for(int i=0; i<n; i++)
	{
		long size;
		cin >> size;
		a[i] = size;
	}

	std::sort(a, a+n);
	int added[100];
	int adds = 0, deletes = 0;

	long cur = x;
	for(int i=0; i<n; i++)
	{
		if(cur > a[i])
		{
			added[i] = 0;
			cur += a[i];
		}
		else
		{
			long need = cur - 1;
			added[i] = 0;
			if(need == 0)
			{
				deletes++;
			}
			else
			{
				long temp = cur - 1;
				while(cur <= a[i])
				{
					added[i]++;
					cur += temp;
					adds++;
					temp = cur-1;
				}
				cur += a[i];
			}
		}
	}

	int temp = 0;
	int lastNode = n-1;
	for(int i=lastNode; i>=0; i--)
	{
		temp += added[i];
		if(temp > lastNode - i + 1)
		{
			adds -= temp;
			deletes += (lastNode-i+1);
			temp = 0;
			lastNode = i;
		}
	}

	return adds + deletes;
}

long main(long argc, char* argv[])
{
	long t;
	cin >> t;
	for(long i=0; i<t; i++)
	{
		long res = Motes();
		cout << "Case #" << i+1 << ": " << res << endl;
	}
}