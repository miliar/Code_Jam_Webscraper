#include <iostream>
#include <list>
#include <algorithm>

using namespace std;

bool cmp(const double &first, const double &second)
{
	return first > second;
}

void printList(const list<double> &l)
{
	for(list<double>::const_iterator it = l.begin(); it != l.end(); it++)
	{
		cout << *it << " ";
	}
	cout << endl;
}

void ps(list<double> k, list<double> n)
{
	cout << endl;
	cout << "Ken: ";
	printList(k);
	cout << "Naomi: ";
	printList(n);
	cout << endl;
}

int war(list<double> ken, list<double> naomi)
{
	list<double>::iterator kit = ken.begin();
	list<double>::iterator nit = naomi.begin();
	int count = 0;

	// for each element naomi has
	for(; nit != naomi.end(); nit++)
	{
		bool found = false;

		// find the smallest element in ken s.t. k > n
		for(; kit != ken.end(); kit++)
		{
			if(*kit > *nit)
			{
				// if found, use it.
				ken.erase(kit);
				kit = ken.begin();
				found = true;
				break;
			}
		}

		// if none of ken's element is > n, naomi gets a point
		// ken would use the lowest element
		if(!found) 
		{
			ken.pop_front();
			kit = ken.begin();
			count++;
		}

	}

	return count;
}

// ken is sorted, naomi is sorted in rev;
int deceitwar(list<double> ken, list<double> naomi)
{
	int count = 0;
	while(!naomi.empty())
	{
		double nmin = naomi.back();
		double kmin = ken.front();
		if(nmin < kmin)
		{
			naomi.pop_back();
			ken.pop_back();
		}
		else
		{
			count++;
			naomi.pop_back();
			ken.pop_front();
		}
	}

	return count;
}

int main()
{
	int nCases;
	cin >> nCases;
	for(int t = 1; t <= nCases; t++)
	{
		int n;
		cin >> n;
		list<double> ken;
		list<double> naomi;
		for(int i = 0; i < n ; i++)
		{
			double na;
			cin >> na;
			naomi.push_back(na);
		}

		for(int i = 0; i < n; i++)
		{
			double k;
			cin >> k;
			ken.push_back(k);
		}

		ken.sort();
		naomi.sort(cmp);

		//ps(ken, naomi);

		int w = war(ken, naomi);
		int d = deceitwar(ken, naomi);

		cout << "Case #" << t << ": " << d << " " << w << endl;
	}
}