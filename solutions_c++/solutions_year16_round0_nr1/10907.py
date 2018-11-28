#include <iostream>
#include <vector>
using namespace std;

bool checkrecord(vector<int> & r)
{
	int count = 0;
	for (int i = 0; i < r.size(); i++)
	{
		if (r[i] > 0) count++;
	}
	if (count == 10)
	{
		return true;
	}
	else
	{
		return false;
	}
}

void store(int num, vector<int> & record)
{
	while (num > 0)
	{
		int i = num % 10;
		record[i] ++;
		num = num / 10;
	}
	
}

void solve(int casenum)
{
	vector<int> record;
	record.assign(10, 0);
	cout << "Case #" << casenum << ": ";
	int N = 0;
	cin >> N;
	if (N == 0)
	{
		cout << "INSOMNIA" << endl;
	}
		
	else
	{
		for (int i = 0; i < 100; i++)
		{
			int K = (i + 1)*N;
			store(K, record);
			if (checkrecord(record))
			{
				cout << K << endl;
				return;
			}
		}
		cout << "INSOMNIA" << endl;
		
	}
}

int main()
{
	int testnum = 0;
	cin >> testnum;

	for (int i = 0; i < testnum; i++)
	{
		solve(i+1);
	}
	return 0;
}