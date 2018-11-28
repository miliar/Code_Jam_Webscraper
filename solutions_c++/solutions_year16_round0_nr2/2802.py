#include <bits/stdc++.h>

using namespace std;

typedef pair<int, int> ii;
typedef pair<ii, string> is;

/*bool operator<(const is& a, const is& b)
{
	if (a.first.first < b.first.first)
		return true;
	else if (a.first.first == b.first.first)
		if (a.second.size() < b.second.size())
			return true;
	return false;
}

class ObjCompare {
public:
    bool operator()(const is a, const is b)
    {
       if (a.first.first < b.first.first)
			return true;
		else if (a.first.first == b.first.first)
			if (a.second.size() < b.second.size())
				return true;
		return false;
    }
};*/

string removeTrailingPlus(string s)
{
	while(s.size() > 0 && s.back() == '+')
		s.pop_back();
	return s;
}

string compute(string s, int offset)
{
	string n = "";
	for(int i=0; i <= offset; i++)
		n += (s[offset-i] == '+')? '-' : '+';
	for(int i=offset+1; i < s.size(); i++)
		n += s[i];
	return n;
}

/*bool isOk(string s)
{
	for(auto &c : s)
		if (c == '-')
			return false;
	return true;
}*/

priority_queue<is> pq;
set<string> s_str;

int main()
{
	int T;
	string current;

	scanf("%d\n", &T);

	for(int tc=1; tc <= T; tc++)
	{
		pq = priority_queue<is>();
		s_str = set<string>();

		printf("Case #%d: ", tc);
		getline(cin, current);

		//printf("%s / ", current.c_str());
		current = removeTrailingPlus(current);
		//printf("%s", current.c_str());

		if (current.size() == 0)
		{
			printf("0\n");
			continue;
		}

		for(int i=0; i < current.size(); i++)
			pq.push( {{-1, i}, compute(current, i)} );

		while(true)
		{
			is curr = pq.top(); pq.pop();

			s_str.insert(curr.second);

			//printf("\n  > current element: score %d, prev %d, %s / ", -curr.first.first, curr.first.second, curr.second.c_str());

			curr.second = removeTrailingPlus(curr.second);
			//printf("%s", curr.second.c_str());
			if (curr.second.size() == 0)
			{
				printf("%d\n", -curr.first.first);
				break;
			}

			for(int i=0; i < curr.second.size(); i++)
			{
				if (i == curr.first.second)
					continue;
				string c_str = compute(curr.second, i);
				if (s_str.find(c_str) != s_str.end())
					continue;
				pq.push( {{curr.first.first-1, i}, compute(curr.second, i)} );
			}

		}
	}

	return EXIT_SUCCESS;
}