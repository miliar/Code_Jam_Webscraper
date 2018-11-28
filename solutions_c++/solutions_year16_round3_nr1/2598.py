#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <set>
#include <vector>
#include <string>

using namespace std;

char takeFromTop(set<pair<int, int> > &q, int &sum)
{
	pair<int, int> tmp = *q.begin();
	q.erase(tmp);
	tmp.first++;
	q.insert(tmp);
	--sum;
	return tmp.second + 'A';
}

void caseN (int n, int b)
{
	printf ("Case #%d: ", b);


	int sum = 0;
	set<pair<int, int> > q;
	for (int i = 0; i < n; ++i)
	{
		int tmp;
		scanf ("%d", &tmp);
		sum += tmp;
		q.insert(make_pair(-tmp, i));
	}
	while(sum != 0)
	{
		if (sum == 3)
		{
			cout << takeFromTop(q, sum);
		}
		else{
			for (int i = 0; i < 2; ++i)
				cout << takeFromTop(q, sum);
		}
		printf (" ");
	}
	printf ("\n");
}

int main (){
	freopen ("1.in", "r", stdin);
	freopen ("1.out", "w", stdout);

	int t;
	scanf ("%d", &t);
	for (int i = 0; i < t; ++i)
	{
		int n;
		scanf ("%d", &n);
		caseN(n, i + 1);
	}

	return 0;
}