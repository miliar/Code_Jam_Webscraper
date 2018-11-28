#pragma once
#include "taskBase.h"

long long int a[70];
bool initialized = false;

class TaskSolution : public TaskBase
{
public:
	TaskSolution(std::istream &is)
		: TaskBase(is)
	{
		if(!initialized)
		{
			std::ifstream in("numbers.txt");
			for(int i = 0; i < 70; i++)
			{
				long long int t;
				in >> t;
				in >> t;
				a[i] = t;
			}
			initialized = true;
		}
	}

	void readData()
	{
		cin >> x >> y;
	}

	void solve()
	{
		int res = 0;
		for(int i = 0; i < 50; i++)
		{
			if(a[i] >= x && a[i] <= y) res++;
		}
		cout << res;
	}
private:

	std::vector<std::string> vs;

	long long x, y;
};

