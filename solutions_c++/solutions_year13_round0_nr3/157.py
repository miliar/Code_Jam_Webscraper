#include<iostream>
#include<string>
#include<map>
#include<vector>
#include<queue>
#include<stack>
#include<set>
#include<algorithm>
#include<sstream>
#include<iomanip>
#include<cstring>
#include<bitset>
#include<fstream>
#include<cmath>
#include<cassert>
#include <stdio.h>
#include<ctype.h>
using namespace std;
typedef long long LL;

string toStr(int n)
{
	string str;
	stringstream ss;
	ss << n;
	ss >> str;
	return str;
}

bool isPalindrome(string str)
{
	int i = 0;
	int j = str.size() - 1;
	while(i < j)
	{
		if(str[i] != str[j])
			return false;
		++i;
		--j;
	}
	return true;
}
string palinPlusOne(string n)
{
	int i = n.size() / 2 - 1, 
		j = n.size() / 2;
	if(n.size() % 2)
	{
		int mid = n.size() / 2;
		if(n[mid] < '9')
		{
			++n[mid];
			return n;
		}
		n[mid] = '0';
		i = mid - 1;
		j = mid + 1;
	}
	while(i >= 0)
	{
		if(n[i] == '9')
			n[i] = n[j] = '0';
		else
		{
			n[i] ++;
			n[j] ++;
			return n;
		}
		i --;
		j ++;
	}
	n[0] = '1';
	for(int i = 1; i < n.size(); ++i)
		n[i] = '0';
	n += '1';
	return n;
}
string add(string number1, string number2)
{
	string add = (number1.length() > number2.length()) ?  number1 : number2;
	char carry = '0';
	int differenceInLength = abs( (int) (number1.size() - number2.size()) );

	if(number1.size() > number2.size())
		number2.insert(0, differenceInLength, '0'); // put zeros from left

	else// if(number1.size() < number2.size())
		number1.insert(0, differenceInLength, '0');

	for(int i=number1.size()-1; i>=0; --i)
	{
		add[i] = ((carry-'0')+(number1[i]-'0')+(number2[i]-'0')) + '0';

		if(i != 0)
		{	
			if(add[i] > '9')
			{
				add[i] -= 10;
				carry = '1';
			}
			else
				carry = '0';
		}
	}
	if(add[0] > '9')
	{
		add[0]-= 10;
		add.insert(0,1,'1');
	}
	return add;
}

string multiply(string n1, string n2)
{
	if(n1.length() > n2.length()) 
		n1.swap(n2);

	string res = "0";
	for(int i=n1.length()-1; i>=0; --i)
	{
		string temp = n2;
		int currentDigit = n1[i]-'0';
		int carry = 0;

		for(int j=temp.length()-1; j>=0; --j)
		{
			temp[j] = ((temp[j]-'0') * currentDigit) + carry;

			if(temp[j] > 9)
			{
				carry = (temp[j]/10);
				temp[j] -= (carry*10);
			}
			else
				carry = 0;

			temp[j] += '0'; // back to string mood
		}

		if(carry > 0)
			temp.insert(0, 1, (carry+'0'));
		
		temp.append((n1.length()-i-1), '0'); // as like mult by 10, 100, 1000, 10000 and so on

		res = add(res, temp); // O(n)
	}

	while(res[0] == '0' && res.length()!=1) // erase leading zeros
		res.erase(0,1);

	return res;
}
int cmp(string n1, string n2)
{
	if(n1.size() != n2.size())
	{
		return (n1.size() < n2.size() ? -1 : 1);
	}
	for(int i = 0; i < n1.size(); ++i)
	{
		if(n1[i] < n2[i])
			return -1;
		else if(n1[i] > n2[i])
			return 1;
	}
	return 0;
}
#define END "10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
vector<string> all;
int N;
string s;
void rec(int i, int sum)
{
	if(i == (N / 2) + (N % 2))
	{
		string sms = multiply(s, s);
		all.push_back(multiply(s, s));
		return;
	}
	for(int j = 0; j <= 9; ++j)
	{
		if(!i && !j)
			continue;
		s[i] = s[N - i - 1] = j + '0';
		bool ad = (N % 2) && i == (N / 2);
		int curr = j * j * (1 + !ad);
		if(curr + sum <= 9)
			rec(i + 1, sum + curr);
		else
			break;
	}
}
string A, B;
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int i;
	for(i = 1; i <= 50; ++i)
	{
		N = i;
		s.resize(N);
		rec(0, 0);
	}
	int T;
	cin >> T;
	for(int ti = 1; ti <= T; ++ti)
	{
		cin >> A >> B;
		int s = -1, e = -1;
		int lo = 0;
		int hi = all.size() - 1;
		int mid;
		while(lo <= hi)
		{
			mid = (lo + hi) / 2;
			if(cmp(all[mid], A) == -1)
				lo = mid + 1;
			else
			{
				hi = mid - 1;
				s = mid;
			}
		}
		lo = 0;
		hi = all.size() - 1;
		while(lo <= hi)
		{
			mid = (lo + hi) / 2;
			if(cmp(all[mid], B) == 1)
				hi = mid - 1;
			else
			{
				lo = mid + 1;
				e = mid;
			}
		}
		int res;
		if(s == -1 || e == -1)
			res = 0;
		else
			res = e - s + 1;
		cout << "Case #" << ti << ": " << res << endl;
	}
}