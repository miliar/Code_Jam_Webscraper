#include <iostream>
#include <iomanip>
#include <cstdlib>

#include<assert.h>

using namespace std;

inline int read(int &x){
	x = 0; // reset x;
	int sign, ch = getchar();
	while ((ch < '0' || ch > '9') && ch != '-' && ch != EOF) ch = getchar();
	if (ch=='-') sign = -1, ch = getchar();
	else sign = 1;
	do x = (x << 3) + (x << 1) + ch - '0';
	while((ch=getchar())>='0' && ch<='9');
	x *= sign;
	return 1;
}

inline void swap(int& a, int& b)
{
	int temp = a; a = b; b = temp;
}

int cmp(const void *v1, const void *v2)
{
	const int i1 = *(const int *)v1;
	const int i2 = *(const int *)v2;

	return i1 < i2 ? -1 : ( i1 > i2 );
}

inline int modValue(const int n)
{
	return n >= 0? n : -n;
}

enum { NOPATH, RIGHT, DOWN, BOTH };

const int MAXDIM = 100;
int main() 
{
	int n_cases;
	int nrows = 0, ncols = 0;
	
	read(n_cases);
	int L[MAXDIM][MAXDIM];
	int dat[MAXDIM][MAXDIM];
	int maxrows[MAXDIM], maxcols[MAXDIM];

	int i, j;
	int case_no = 1;
	while ( case_no <= n_cases)
	{
		read(nrows); read(ncols);
		for (i = 0; i < MAXDIM; i++)
		{
			maxrows[i] = 0; maxcols[i] = 0;
		}
		for ( i = 0; i < nrows; i++)
		{
			for (j = 0; j < ncols; j++)
			{
				read(L[i][j]);

				if (L[i][j] > maxrows[i]) maxrows[i] = L[i][j];
				if (L[i][j] > maxcols[j]) maxcols[j] = L[i][j];
			}
		}

		bool answer = true;
		for (i = 0; i < nrows; i++)
		{
			for (j = 0; j < ncols; j++)
			{
				if(L[i][j] == maxrows[i] && L[i][j] == maxcols[j])
				{
					dat[i][j] = BOTH;
				}
				else if(L[i][j] == maxrows[i])
				{
					dat[i][j] = RIGHT;
				}
				else if(L[i][j] == maxcols[j])
				{
					dat[i][j] = DOWN;
				}
				else
				{
					dat[i][j] = NOPATH;
					answer = false;
					break;
				}
			}
			if (!answer) break;
		}

		cout << "Case #" << case_no << ": " << (answer? "YES" : "NO" )<< endl;
		case_no++;
	}

	// system("PAUSE");
	return 0;
}
