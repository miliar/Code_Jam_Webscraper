#include <cstdio>
#include <cstring>
#include <deque>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

#define MAX 10000000

#define PRINT(x) copy(x.begin(), x.end(), ostream_iterator<int>(cout)); cout << endl
#define DEBUG(s, x) cout << s << ": " << x << endl;

// There is an infitnite amount of diners, so you can always put pancakes 
// somewhere.

// You never need to put pancakes onto someone elses plate then.

int minutes(deque<int> q, int limit)
{
	if (q.back() <= 2)
		return q.back();
	if (limit == 0)
		return MAX;

	deque<int> normal(q);
	for (int i = 0; i < normal.size(); i++)
		normal[i] -= 1;
	while (normal.front() == 0)
		normal.pop_front();

	int m = minutes(normal, limit - 1);

	int max = q.back();
	for (int j = 1; j <= max / 2; j++) {
		deque<int> special(q);
		int max = special.back();
		special.pop_back();
		special.push_back(j);
		special.push_back(max - j);
		sort(special.begin(), special.end());

		m = min(m, minutes(special, limit - 1));
	}

	return m + 1;
}

int main()
{
	int N; 
	scanf("%d", &N);

	for (int n = 1; n <= N; n++) {
		int d = 0; 
		scanf("%d", &d);

		int p[d];
		for (int i = 0; i < d; i++) 
			scanf("%d", &p[i]);

		deque<int> q;
		for (int i = 0; i < d; i++)
			q.push_back(p[i]);
		sort(q.begin(), q.end());

		int m = minutes(q, q.back());
		
		printf("Case #%d: %d\n", n, m);
	}

	return 0;
}