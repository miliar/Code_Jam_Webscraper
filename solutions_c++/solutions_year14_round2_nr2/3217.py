#include <iostream>
#include <fstream>

using namespace std;


int *bin(int a)
{
	int * t = new int[11], n = 0, trm;

	while (a > 0)
	{
		if (a % 2 == 0)
		{
			t[n++] = 0;
		}
		else
			t[n++] = 1;

		a /= 2;
	}

	t[n] = -1;

	return t;
}


int inter(int *a, int *b)
{
	int nA = 0, nB = 0, *t, num = 0;

	for (; a[nA] != -1; nA++);
	for (; b[nB] != -1; nB++);

	if (nA >= nB)
	{
		t = new int[nA + 1];

		for (int i = 0; i < nA; i++)
		{
			if (nB > i)
			{
				if (a[i] == b[i])
					t[i] = a[i];
				else if (a[i] == 0 || b[i] == 0)
					t[i] = 0;

			}
			else
				t[i] = 0;

		}


		t[nA] = -1;

		float j = 0;
		for (int i = 0; i < nA; i++, j++)
		{
			num += t[i] * pow(2.0, j);
		}

		return num;
	}
	else
	{
		t = new int[nB];

		for (int i = 0; i < nB; i++)
		{
			if (nA > i)
			{
				if (a[i] == b[i])
					t[i] = a[i];
				else if (a[i] == 0 || b[i] == 0)
					t[i] = 0;

			}
			else
				t[i] = 0;

		}

		t[nB] = -1;

		float j = 0;
		for (int i = 0; i < nB; i++, j++)
		{
			num += t[i] * pow(2.0, i);
		}

		
		return num;
	}

}



int main()
{
	ifstream inf("B-small-attempt2.in");
	ofstream onf("ms.txt");
	int i, j, size, m, n, a, b, k, ni = 1, count = 0;

	inf >> size;


	while (size >= ni)
	{
		inf >> a >> b >> k;
		int *at, *bt;
		count = 0;

		for (i = 0; i < a; i++)
		{
			for (j = 0; j < b; j++)
			{
				at = bin(i);
				bt = bin(j);
				m = inter(at, bt);
				delete at;
				delete bt;

				if (m < k)
					count++;
			}

		}

		onf << "Case #" << ni << ": " << count << endl;

		ni++;
	}



	return 0;
}