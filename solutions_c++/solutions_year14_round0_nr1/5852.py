#include <iostream>

#include <algorithm>
#include <string>
#include <cstring>
#include <vector>
#include <map>
#include <set>
#include <cmath>
#include <limits>

using namespace std;

#define BAD "Bad magician!"
#define CHEAT "Volunteer cheated!"

int T;

void print_set(set<int> s)
{
	set<int>::iterator it;
	for (it=s.begin(); it!=s.end(); ++it)
		std::cout << " " << *it;
	cout << endl;;

}

void solve(set<int> s1, set<int> s2)
{
	
	set<int> res;
	set_intersection(s1.begin(), s1.end(), s2.begin(), s2.end(), inserter(res, res.begin()));

	/*print_set(s1);
	print_set(s2);
	print_set(res);*/
	
	if(res.empty())
		cout << CHEAT << endl;
	else if(res.size() > 1)
		cout << BAD << endl;
	else
		cout << *(res.begin()) << endl;
}

int main()
{
	cin >> T;
	int r1, r2;
	int tmp;
	
	for(int i=0; i < T; i++)
	{
		set<int> s1;
		set<int> s2;
		cin >> r1;
		for(int j=0; j < 4; j++)
		{
			for(int k=0; k < 4; k++)
			{
				cin >> tmp;
				if(j==r1-1)
					s1.insert(tmp);
			}
		}

		cin >> r2;
		for(int j=0; j < 4; j++)
		{
			for(int k=0; k < 4; k++)
			{
				cin >> tmp;
				if(j==r2-1)
					s2.insert(tmp);
			}
		}

		
		cout << "Case #" << i+1 << ": ";
		solve(s1, s2);
	}
	return 0;
}
