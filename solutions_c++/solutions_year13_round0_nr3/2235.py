#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <vector>

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

bool check_palindrome(long long num)
{
	long long n = num;
	long long rev = 0;
	while (num > 0)
	{
		long long dig = num % 10;
		rev = rev * 10 + dig;
		num = num / 10;
	}
	return n == rev;
}

vector<long long> fns_nos;

int findall()
{
	long long n;
	for(long long i = 1; i <= 10000000; i++)
	{
		n = i * i;

		if (check_palindrome(i) && check_palindrome(n)) 
		{
			fns_nos.push_back(n);
			// cout << n << endl;
		}
	}
	// cout << "Size: " << fns_nos.size() << endl;
	
	return 0;
}

int fns2(long long ll, long long ul)
{
	int count = 0;
	for ( unsigned int i = 0; i < fns_nos.size(); i++)
	{
		if (ll <= fns_nos[i] && fns_nos[i] <= ul)
		{
			count++; //  cout << fns_nos[i] << " ";
		}
	}
	return count;
}


int fns1(long long ll, long long ul)
{
	long long sq_ll = (long long) sqrt(ll);
	long long sq_ul = (long long) sqrt(ul);
	
	if (sq_ll * sq_ll < ll) ++sq_ll;

	long long n;
	int count = 0;
	
	for(long long i = sq_ll; i <= sq_ul; i++)
	{
		n = i * i;

		if (check_palindrome(i) && check_palindrome(n)) 
		{
			count++; // cout << n << " ";
		}
	}
	return count;
}

int main() 
{
	int n_cases = 0;
	read(n_cases);

	findall();

	int case_no = 1;
	long long ll, ul;
	while ( case_no <= n_cases)
	{
		cin >> (ll) >> (ul);

		cout << "Case #" << case_no << ": " << fns2(ll, ul)<< endl;
		case_no++;
	}

	// system("PAUSE");
	return 0;
}
