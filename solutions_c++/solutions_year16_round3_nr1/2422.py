#include <iostream>
#include <queue>

using namespace std;

struct party
{
	int count;
	char id;
	
	party() {}
	party(char id_, int count_) : id(id_), count(count_) {}
	
	bool operator<(const party& rhs) const
	{
		return count < rhs.count;
	}
};

party topmost(priority_queue<party>& ordering)
{
	party p = ordering.top();
	ordering.pop();
	return p;
}

void evacuate(priority_queue<party>& ordering, party& p, int& total)
{
	total--;
	p.count--;
	cout << p.id;
	if (p.count)
		ordering.push(p);
}

int main()
{
	int cases;
	cin >> cases;
	for (int c = 1; c <= cases; c++)
	{
		cout << "Case #" << c << ":";
		
		int n, k, p, total;
		priority_queue<party> ordering;
		
		cin >> n;
		total = 0;
		for (k = 0; k < n; k++)
		{
			cin >> p;
			total += p;
			ordering.push(party(k + 'A', p));
		}
		
		while (total > 3)
		{
			if (ordering.top().count > total / 2)
			{
				cout << "FAILURE" << endl;
				return 0;
			}
			cout << " ";
			
			party u = topmost(ordering);
			if (!ordering.empty() && ordering.top().count == u.count)
			{
				party v = topmost(ordering);
				evacuate(ordering, v, total);
			}
			evacuate(ordering, u, total);
		}
		if (total == 3)
		{
			party x = topmost(ordering);
			cout << " ";
			evacuate(ordering, x, total);
		}
		party y = topmost(ordering);
		party z = topmost(ordering);
		
		cout << " ";
		evacuate(ordering, y, total);
		evacuate(ordering, z, total);
		cout << endl;
	}
	return 0;
}
