#include <iostream>
#include <string>
#include <cmath>
#include <vector>
#include <sstream>
using namespace std;

typedef unsigned long long ull;

bool isPalindrome(ull n)
{
	string s;
	while (n)
	{
		int i = n%10;
		s.push_back('0'+i);
		n /= 10;
	}

	int i = 0;
	int j = s.length()-1;
	while (i<j)
	{
		if (s[i] == s[j])
		{
			++i;
			--j;
		}
		else
			break;
	}

	if (i < j) return false;

	return true;
}

int digits(ull n)
{
	int c = 0;
	while (n)
	{
		++c;
		n /= 10;
	}

	return c;
}

void gen(string n, int digits, vector<ull>& vi)
{
	if (digits < n.length()/2)
	{
		int len = n.length();
		string nn = n;
		for (int i = len-1; i >= 0; --i)
			nn += nn[i];

		stringstream ss(nn);
		ull v;
		ss>>v;
		vi.push_back(v);
		return;
	}

	for (int i = 0; i < 10; ++i)
	{
		n.push_back('0' + i);
		gen(n, digits-1, vi);
		n.pop_back();
	}
}

void generate_palindrome(int digits, vector<ull>& vi)
{
	string s;
	for (int i = 1; i < 10; ++i)
	{
		s += '0'+i;
		gen(s, digits-1, vi);
	}
}

int main()
{
	int T;
	cin>>T;

	for (int i = 0; i < T; ++i)
	{
		ull A,B;
		cin>>A>>B;

		ull low = sqrt(A+0.1)-1;
		ull high = sqrt(B+0.1)+1;

		ull ret = 0;
		for (ull k = low; k <= high; ++k)
		{
			{
				if (isPalindrome(k))
				{
					ull square = k*k;
					if (isPalindrome(square) && square <= B && square >= A)
						++ret;

					if (square > B) break;
				}
			}
		}

		cout<<"Case #"<<i+1<<": "<<ret<<endl;
	}
}