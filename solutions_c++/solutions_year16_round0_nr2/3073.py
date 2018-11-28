#include <iostream>
#include <cstring>
#include <stdio.h>
#include <algorithm>
#include <cmath>
#include <map>
#include <vector>
#include <set>
#include <string>
using namespace std;
/*the first answer*/
/*
int main()
{
	freopen("A-small-attempt2.in", "r", stdin);
	freopen("result.txt", "w", stdout);
	int test_case;
	cin >> test_case;
	int index = 0;
	while (test_case--)
	{
		cout << "Case #" << ++index << ": ";
		int value;
		cin >> value;
		if (value == 0)
		{
			cout << "INSOMNIA" << endl;
			continue;
		}
		string digit = to_string(value);
		set<char> s;

		for (int i = 0; i < digit.size(); ++i)
		{
			s.insert(digit[i]);
		}
		if (s.size() == 10) cout << value << endl;
		for (int i = 2;; ++i)
		{
			int next = value*i;
			digit = to_string(next);
			for (int j = 0; j < digit.size(); ++j)
			{
				s.insert(digit[j]);
			}
			if (s.size() == 10)
			{
				cout << next << endl;
				break;
			}
		}

	}

}*/

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("resultbl.txt", "w", stdout);
	int test_case;
	cin >> test_case;
	int index = 0;
	while (test_case--)
	{
		cout << "Case #" << ++index << ": ";
		string s;
		cin >> s;
		s.push_back('+');
		int len = s.size();
		int i = 0;
		int j = i + 1;
		int result = 0;
		while (j < len)
		{
			if (s[i] != s[j])
			{
				result++;
			}
			i++;
			j++;
		}
		cout << result << endl;

	}

}
/*
int main()
{
	freopen("D-small-attempt1.in", "r", stdin);
	freopen("result.txt", "w", stdout);
	int test_case;
	cin >> test_case;
	int index = 0;
	while (test_case--)
	{
		cout << "Case #" << ++index << ": ";
		
		int k, c, s;
		cin >> k >> c >> s;
		long long len = pow(k,c-1) ;
		if (len == 0)
		{
			cout << 1;
		}
		for (int i = 0; i < s&&len!=0; ++i)
		{
			cout << i*len +1<<" ";
		}
		
		cout << endl;

	}

}
string printbinary(long long val)
{
	string s;
	long long base = 1;
	for (int i = 32; i >= 0; i--)
	{
		if (val & (base << i))
			s.push_back('1');
		else
			s.push_back('0');
	}
	return s;
}
bool is_prime(long long val,long &divisor)
{
	
	long long value = sqrt(val);
	long i = 2;
	while (i <= value)
	{
		if (val%i == 0)
		{
			divisor = i;
			return false;
			
		}
		i++;
	}
	return true;
}

long long bi_to_other(string s, int oper)
{
	long long sum = 0;
	switch (oper)
	{

	case 2:
		for (int i = 0; i < s.size(); ++i)
		{
			if (s[i] == '1')
				sum += pow(2, s.size() - i - 1);
		}
		return sum;
		break;
		case 3:
			for (int i = 0; i < s.size(); ++i)
			{
				if (s[i] == '1')
				sum += pow(3, s.size() - i - 1);
			}
			return sum;
			break;
		case 4:
			for (int i = 0; i < s.size(); ++i)
			{
				if (s[i] == '1')
				sum += pow(4, s.size() - i - 1);
			}
			return sum;
			break;
		case 5:
			for (int i = 0; i < s.size(); ++i)
			{
				if (s[i] == '1')
				sum += pow(5, s.size() - i - 1);
			}
			return sum;
			break;
		case 6:
			for (int i = 0; i < s.size(); ++i)
			{
				if (s[i] == '1')
				sum += pow(6, s.size() - i - 1);
			}
			return sum;
			break;
		case 7:
			for (int i = 0; i < s.size(); ++i)
			{
				if (s[i] == '1')
				sum += pow(7, s.size() - i - 1);
			}
			return sum;
			break;
		case 8:
			for (int i = 0; i < s.size(); ++i)
			{
				if (s[i] == '1')
				sum += pow(8, s.size() - i - 1);
			}
			return sum;
			break;
		case 9:
			for (int i = 0; i < s.size(); ++i)
			{
				if (s[i] == '1')
				sum += pow(9, s.size() - i - 1);
			}
			return sum;
			break;

		case 10:
			for (int i = 0; i < s.size(); ++i)
			{
				if (s[i] == '1')
					sum += pow(10, s.size() - i - 1);
			}
			return sum;
			break;
	}
}
int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("result1.txt", "w", stdout);
	int test_case;
	cin >> test_case;
	int index = 0;
	while (test_case--)
	{
		cout << "Case #" << ++index << ": " << endl;
		int n, m;
		cin >> n >> m;
		long long up_bound = pow(2, n)-1;
		long long down_bound = pow(2, n-1) + 1;
	
		for (long long i = down_bound; i <= up_bound; ++i)
		{
			
			vector<long> result;
			bool outofloop = false;
			long divisor = 0;
			string bit = printbinary(i);
			if (bit[bit.size() - 1] == '0')
			{
				continue;
			}
			for (int j = 2; j <= 10; ++j)
			{
				long long temp = bi_to_other(bit, j);
				if (is_prime(temp,divisor))
				{
					break;
					outofloop = true;
				}
				else
				{
					
					result.push_back(divisor);
				}
			}
			if (outofloop)
			{
			break;
			}
			if (result.size() == 9)
			{
				m--;
				bool flag = false;
				for (int i = 0; i < bit.size(); ++i)
				{
					if (bit[i] == '1')
						flag = true;
					if (flag)
					{
						cout << bit[i];
					}
				}
				cout << " ";
				
				
				for (int i = 0; i < result.size(); ++i)
				{
					
				
					cout << result[i] << " ";
				}
	
				cout << endl;
			}
			if (m == 0)
				break;



		}
	

	}
}*/