#include <iostream>
#include <cmath>
#include <fstream>
using namespace std;

int Digits(_int64 a)
{
	int digits = 0;
	while(a)
	{
		a /= 10;
		digits++;
	}
	return digits;
}

bool IsPalindrome(_int64 a)
{
	_int64 rev = 0;
	int i = Digits(a) - 1;
	_int64 copy = a;
	while(a)
	{
		int mod = a % 10;
		rev += mod * pow(10, i);
		a /= 10;
		i--;
	}
	if(copy == rev)
		return true;
	return false;
}

bool IsSquare(const _int64 &a)
{
	int s = sqrt(a);
	if(s * s == a)
		return true;
	return false;
}

int main()
{
	ifstream in("1.in");
	ofstream out("1.out");
	int n;
	in >> n;
	for(int num = 0; num < n; num++)
	{
		_int64 a, b;
		in >> a >> b;
		_int64 count = 0;
		for(_int64 i = a; i <= b; i++)
		{
			if(IsSquare(i) && IsPalindrome(i))
			{
				if(IsPalindrome(sqrt(i)))
					count++;
			}			
		}
		out << "Case #" << num + 1 << ": " << count << endl;
	}
}