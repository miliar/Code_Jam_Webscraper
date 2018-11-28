#pragma once
#include "taskBase.h"
#include <vector>
using namespace std;

class TaskSolution : public TaskBase
{
public:
	TaskSolution(std::istream &is)
		: TaskBase(is)
	{

	}

	void readData()
	{
		cin >> e >> r >> n;
		v.resize(n);
		for(int i = 0; i < n; i++)
		{
			cin >> v[i];
		}
	}

	void f(int d, int E, int g)
	{
		if(d == n)
		{
			res = max(res, g);
			return;
		}
		for(int i = 0; i <= E; i++)
		{
			f(d + 1, min(E - i + r, e), g + i * v[d]);
		}
	}

	void solve()
	{
		res = 0;
		f(0, e, 0);
		cout << res;
	}
private:
	int e, r, n;
	int res;
	vector<int> v;
};
