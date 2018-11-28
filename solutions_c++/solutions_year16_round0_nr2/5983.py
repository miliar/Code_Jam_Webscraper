#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int puzzle_flip_invert(int *a,int n)
{
	int i1, m, i, j;
	char b;
	for (m = 0; ; m++)
	{
		if (a[0] == 1)
		{
			for (i1 = 0; (i1 < n - 1) && (a[i1 + 1] == 1); i1++);
				if (i1 == n - 1)
					break;
		}
		else
			for (i1 = n - 1; (i1 >= 0) && (a[i1] == 1); i1--, n--);
		for (i = 0, j = i1; i <= j; i++, j--)
		{
			b = 1 - a[i]; a[i] = 1 - a[j]; a[j] = b;
		}
	}
	return m;
}

int main() {
	ofstream fout ("test.out");
	ifstream fin ("test.in");
	int cases = 0;
	fin >> cases;
	for(int i = 1; i <= cases; i++){
		string a;
		fin >> a;
		int d[10] = {0};
		int counter = 0;
		for(char c : a) {
			if(c == '-')
				d[counter] = 0;
			else
				d[counter] = 1;
			counter++;
		}
		fout << "Case #" << i << ": " << puzzle_flip_invert(d, counter) << endl;
	}
	return 0;
}