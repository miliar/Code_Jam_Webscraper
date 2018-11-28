#include<iostream>
#include<algorithm>
#include<list>
using namespace std;

bool greater(double a1, double a2)
{
	return a1 > a2;
}

int main()
{
	int N;
	cin >> N;
	for (int i = 0; i < N; ++i)
	{
		int nums;
		cin >> nums;
		list<double> naomi, ken;
		double tmp;
		for (int j = 0; j < nums; ++j)
		{
			cin >> tmp;
			naomi.push_back(tmp);
		}
		for (int j = 0; j < nums; ++j)
		{
			cin >> tmp;
			ken.push_back(tmp);
		}
		//sort(naomi.begin(), naomi.end());
		naomi.sort();
		//sort(ken.begin(), ken.end());
		ken.sort();
		list<double> op_ken(ken);
		int de_cnt = 0, op_cnt = 0;
		for (list<double>::const_iterator iter = naomi.begin(); iter != naomi.end(); ++iter)
		{
			list<double>::const_iterator kenBeg = ken.begin();
			if (*iter > *kenBeg)		// bigger than some elements of ken
			{
				++de_cnt;
				ken.pop_front();
			}
			else 						// smaller than any element of ken	
			{
				ken.pop_back();
			}
			if (op_ken.size() == 0)
				continue;

			list<double>::iterator iter2 = op_ken.begin();
 			for (; iter2 != op_ken.end(); ++iter2)
			{
				if (*iter2 > *iter)
					break;
			}
			if (iter2 != op_ken.end())
			{
				op_ken.erase(iter2);
			}
			else 
			{
				op_cnt = op_ken.size();
				op_ken.clear();
			}
		}
				
		cout << "Case #" << i+1 << ": " << de_cnt << " " << op_cnt << endl;
	}
	return 0;
}
