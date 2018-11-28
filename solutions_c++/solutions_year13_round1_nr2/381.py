#include <iostream>
#include <fstream>
//#include <stdio.h>

using namespace std;

void qsort(int *a , int *b, int lo , int hi)
{
	int t;
	int l,h;
	l = lo; h = hi;
	int x;
	x = a[ (l+h)/2 ];
	do{
		while (a[l]>x) l++;
		while (a[h]<x) h--;
		if (l<=h)
		{
			t = a[l]; a[l] = a[h]; a[h] = t;
			t = b[l]; b[l] = b[h]; b[h] = t;
			l++; h--;
		}
	}while (l<=h);
	if (l<hi) {qsort(a , b, l,hi);};
	if (h>lo) {qsort(a , b, lo,h);};
}

const int NMax = 10005;
int v[NMax];
int e, r, n;

long long solve(int lo, int hi, int st, int fin)
{
	if (lo > hi)
		return 0;

	int pos = lo;
	for (int i = lo+1; i <= hi; i++)
		if (v[i] > v[pos])
			pos = i;
	
	long long pp = pos-lo;
	pp *= r;
	pp += st;
	int possib = st + (pos - lo)*r;
	if (pp > e)
		possib = e;

	pp = hi-pos;
	pp *= r;
	int now;
	if (fin > pp)
		now = possib - (fin - r*(hi-pos));
	else
		now = possib;

	long long temp = now;
	temp *= v[pos];
	return  temp + solve(lo, pos-1, st, possib-r) + solve(pos+1, hi, possib-now+r, fin);
}

int main()
{
	ifstream cin("input.txt");
	ofstream cout("output.txt");


	int testnum = 0;
	cin >> testnum;
	for (int testcase = 1; testcase <= testnum; testcase++)
	{
		cin >> e >> r >> n;
		for (int i = 1; i <= n; i++)
			cin >> v[i];

		long long res = solve(1, n, e, 0);

		cout << "Case #" << testcase << ": " << res << endl;
	}

	return 0;
}
