#include <iostream>
#include <stdlib.h>
using namespace std;

struct Set
{
public:
	double *arr1;
	double *arr2;
	double *brr2;
	double *brr1;
	int size;
	int war1, war2;

	void start(int a)
	{
		size = a;
		arr1 = new double[a];
		arr2 = new double[a];
		brr1 = new double[a];
		brr2 = new double[a];
		war2 = 0; war1 = 0;
	}

	void war()
	{
		int ap = 0;
		int bp = 0;
		while(ap < size)
		{
			if(arr1[ap] < brr1[bp])
			{
				ap++;
			}
			else
			{
				war1++;
				ap++; bp++;
			}
		}

		ap = 0;
		bp = 0;

		while(bp < size)
		{
			if(arr2[ap] < brr2[bp])
			{
				bp++;
				ap++;
			}
			else
			{
				bp++;
				war2++;
			}
		}
	}

};

// int compare (const void *a, const void *b)
// {
// 	if(a < b)
// 		return -1;
// 	else if(b < a)
// 		return 1;
// 	else
// 		return 0;

// }


int compare(const void *a,const void *b) {
double *x = (double *) a;
double *y = (double *) b;
// return *x – *y; // this is WRONG…
if (*x < *y) return -1;
else if (*x > *y) return 1;
return 0;
}

int main()
{
	int cases;
	int a;
	cin >> cases;

	Set *set;
	set = new Set[cases];
	for (int i = 0; i < cases; ++i)
	{
		cin >> a;
		set[i].start(a);
		for (int j = 0; j < a; ++j)
		{
			cin >> set[i].arr1[j];
		}
		for (int k = 0; k < a; ++k)
		{
			cin >> set[i].brr1[k];
		}
	}


	for (int i = 0; i < cases; ++i)
	{
		qsort (set[i].arr1, set[i].size, sizeof(double), compare);
		qsort (set[i].brr1, set[i].size , sizeof(double), compare);
		set[i].arr2 = set[i].arr1;
		set[i].brr2 = set[i].brr1;
	}

	for (int i = 0; i < cases; ++i)
	{
		set[i].war();
		cout << "Case #" << i+1 << ": " << set[i].war1 << " " << set[i].war2 << endl;
	}

	

	return 0;
}