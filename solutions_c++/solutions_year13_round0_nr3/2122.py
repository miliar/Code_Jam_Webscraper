#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

typedef vector<int> bigint;

string tostring(const bigint& a)
{
	string ans;
	for (int i = a.size() - 1; i >= 0; i--)
		ans += (char)(a[i] + '0');
	return ans;
}

bool exceed(const bigint& a, const bigint& b)
{
	if (a.size() != b.size())
		return a.size() > b.size();
	for (int i = a.size() - 1; i >= 0; i--)
		if (a[i] != b[i])
			return a[i] > b[i];
	return false;
}

bool palindrome(const bigint& a)
{
//	cerr << "checking " << tostring(a) << endl;;
	for (int i = 0; i < a.size() - 1 - i; i++)
		if (a[i] != a[a.size() - 1 - i])
			return false;
	return true;
}

bigint dec(const bigint& a)
{
	bigint ans = a;
	ans[0]--;
	for (int i = 0; i < ans.size(); i++)
	{
		if (ans[i] >= 0)
			break;
		ans[i] += 10;
		ans[i+1]--;
	}
	while (ans.size() && !ans.back())
		ans.pop_back();
	return ans;
}

bigint operator *(const bigint& a, const bigint& b)
{
	if (!a.size() || !b.size())
		return bigint();

	bigint ans(a.size() + b.size() - 1);
	for (int i = 0; i < a.size(); i++)
		for (int j = 0; j < b.size(); j++)
			ans[i + j] += a[i] * b[j];
	for (int i = 0; i < ans.size(); i++)
		if (ans[i] >= 10)
		{
			if (i == ans.size() - 1)
				ans.push_back(0);
			ans[i+1] += ans[i] / 10;
			ans[i] %= 10;
		}
//	cerr << tostring(a) << " x " << tostring(b) << " = " << tostring(ans) << endl;
	return ans;
}

int toint(const bigint &a)
{
	int ans = 0;
	for (int i = a.size() - 1; i >= 0; i--)
		ans = ans * 10 + a[i];
	return ans;
}

int get_count(bigint N)
{
	int ans = 0;
	if (N.size() <= 4)
	{
		int n = toint(N);
		if (n >= 1)
			ans++;
		if (n >= 4)
			ans++;
		if (n >= 9)
			ans++;
		if (n >= 121)
			ans++;
		if (n >= 484)
			ans++;
		return ans;
	}
	
	ans += 5;
	for (int l = 2; ; l++)
	{
		// len = 2l - 1, starting with 1
		for (int mid = 0; mid < (1 << (l-2)); mid++)
			for (int tail = 0; tail < 3; tail++)
			{
				bigint cur(l * 2 - 1);
				cur[0] = 1;
				for (int i = 1, s = mid; s; i++)
				{
					cur[i] = s & 1;
					s >>= 1;
				}
				cur[l - 1] = tail;
				for (int i = l; i < cur.size(); i++)
					cur[i] = cur[l * 2 - 2 - i];
					
				bigint sqr = cur * cur;
				if (exceed(sqr, N))
					return ans;
				if (palindrome(sqr))
					ans++;
			}
			
		// len = 2l - 1, starting with 2
		for (int tail = 0; tail < 2; tail++)
		{
			bigint cur(l * 2 - 1);
			cur[0] = cur[l * 2 - 2] = 2;
			cur[l - 1] = tail;
			bigint sqr = cur * cur;
			if (exceed(sqr, N))
				return ans;
			if (palindrome(sqr))
				ans++;	
		}
		
		// len = 2l, starting with 1
		for (int mid = 0; mid < (1 << (l-1)); mid++)
		{
			bigint cur(l * 2);
			cur[0] = 1;
			for (int i = 1, s = mid; s; i++)
			{
				cur[i] = s & 1;
				s >>= 1;
			}
			for (int i = l; i < cur.size(); i++)
				cur[i] = cur[l * 2 - 1 - i];
				
			bigint sqr = cur * cur;
			if (exceed(sqr, N))
				return ans;
			if (palindrome(sqr))
				ans++;
		}
		
		// len = 2l, starting with 2
		bigint cur(l * 2);
		cur[0] = cur[l * 2 - 1] = 2;
		bigint sqr = cur * cur;
		if (exceed(sqr, N))
			return ans;
		if (palindrome(sqr))
			ans++;
	}	
}

int main()
{
	int caseN;
	cin >> caseN;
	for (int caseI = 1; caseI <= caseN; caseI++)
	{
		string a, b;
		cin >> a >> b;
		bigint A, B;
		for (int i = 0; i < a.size(); i++)
			A.push_back(*(a.rbegin() + i) - '0');
		for (int i = 0; i < b.size(); i++)
			B.push_back(*(b.rbegin() + i) - '0');
		cout << "Case #" << caseI << ": " << get_count(B) - get_count(dec(A)) << endl;
	}
	return 0;
}
