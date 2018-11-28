#include <list>
#include <iostream>
using namespace std;

void print_args(){}

template <typename T, typename... Args>
void print_args(const T & val, Args... args)
{
	cout << val << " ";
	print_args(args...);
}

template <typename... Args>
void print_case(int test_case, Args... args)
{
	cout << "Case #" << test_case << ": ";
	print_args(args...);
	cout << endl;
}

pair<list<int>::iterator,int> smallest(list<int> & lst)
{
	list<int>::iterator best = lst.begin();
	int b_dist = 0, dist = 0;
	for(auto it = lst.begin(); it != lst.end(); it++)
	{
		if( (*it) < (*best) )
		{
			best = it;
			b_dist = dist;
		}
		dist++;
	}
	return make_pair(best, b_dist);
}

int main()
{
	int num_cases;
	cin >> num_cases;
	for(int c = 0; c < num_cases; c++)
	{
		int num_ints;
		cin >> num_ints;
		list<int> ints;
		for(int n = 0; n < num_ints; n++)
		{
			int tmp;
			cin >> tmp;
			ints.push_back(tmp);
		}

		int ans = 0;
		for(int n = 0; n < num_ints; n++)
		{
			auto p = smallest(ints);
			int dist = p.second;
			ints.erase(p.first);
			ans += min(dist, (int)ints.size()-dist);
		}
		print_case(c+1, ans);
	}
	return 0;
}
