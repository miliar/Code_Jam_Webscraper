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

int main() 
{
	int n_cases;
	long long r = 0, t = 0;
	
	read(n_cases);

	long long n = 0;
	int case_no = 1;
	while ( case_no <= n_cases)
	{
		cin >> r >> t;

		long double b = 2 * r - 1;
		long double d = 1 + 8 * t/(b*b);
		float re = (-1 + sqrt(d)) * b/ 4;

		n = t;
		cout << "Case #" << case_no << ": " << (long) re << endl;
		case_no++;
	}

	// system("PAUSE");
	return 0;
}
