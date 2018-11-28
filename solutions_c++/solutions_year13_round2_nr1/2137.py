#include <iostream>
#include <cstdio>
#include <climits>
using namespace std;

#define MIN2(a, b) (a)<=(b)?(a):(b)

void Merge(int *a, int l, int m, int r)
{
	int s1 = m - l + 1;
	int s2 = r - m;
	int a1[s1+1];
	int a2[s2+1];

	a1[s1] = INT_MAX;
	for (int s=0; s<s1; s++)
		a1[s] = a[l+s];

	a2[s2] = INT_MAX;
	for (int s=0; s<s2; s++)
		a2[s] = a[m+1+s];

	int c1=0, c2=0;
	for (int i=l; i<=r; i++)
	{
		if (a1[c1] <= a2[c2])
			a[i] = a1[c1++];
		else
			a[i] = a2[c2++];
	}
}

void Sort(int *a, int l, int r)
{
	if (l >= r)
		return;
	int m = (l+r)/2;
	Sort(a, l, m);
	Sort(a, m+1, r);
	Merge(a, l, m, r);
}

int MinCost(int A, int *motes, int l, int r)
{
	if (l > r)
		return 0;

	if (motes[l] < A)
		return MinCost(A+motes[l], motes, l+1, r);

	if (A == 1)
		return 1 + MinCost(A, motes, l+1, r);

	int sol1 = 1 + MinCost(A+A-1, motes, l, r);
	int sol2 = 1 + MinCost(A, motes, l+1, r);

	return MIN2(sol1, sol2);
}

int main(int argc, char *argv[])
{
	freopen(argv[1], "r", stdin);
	freopen(argv[2], "w", stdout);

	int T;
	cin >> T;
	for (int t=0; t<T; t++)
	{
		int A, N;
		cin >> A >> N;
		int motes[N];
		for (int n=0; n<N; n++)
			cin >> motes[n];

		Sort(motes, 0, N-1);
		
		int cost = MinCost(A, motes, 0, N-1);
		cout << "Case #" << t+1 << ": " << cost << endl;
	}

	return 0;
}
	
