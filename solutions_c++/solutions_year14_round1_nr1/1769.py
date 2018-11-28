#include<iostream>
#include<string>
#include <algorithm>
using namespace std;
int n, l;
string xor(const string &a,const string &b)
{
	string tmp;
	int i;
	for (i = 0; i < l; i++)
	{
		if (a[i] == b[i])
			tmp=tmp+ '0';
		else
			tmp=tmp+ '1';
	}
	return tmp;
}
int jishu(const string &a)
{
	int t = 0;
	for (int i = 0; i < l; i++)
	{
		if (a[i] == '1')
			t++;
	}
	return t;
}
int main()
{
	int T;
	errno_t err1;
	FILE *f;
	err1 = freopen_s(&f, "A-small-attempt1 (1).in", "r", stdin);
	errno_t err2;
	FILE *f2;
	err2 = freopen_s(&f2, "3.txt", "w", stdout);
	cin >> T;
	int min = 400;
	for (int i = 0; i < T; i++)
	{
		min = 400;
		cin >> n >> l;
		string A[200];
		string B[200];
		for (int i = 0; i < n; i++)
		{
			cin >> A[i];
		}
		for (int j = 0; j < n; j++)
		{
			cin >> B[j];
		}
	//	sort(A, A + n);
		sort(B, B + n);
		string jieguo;
		string tmp[200] = {};
		int mark = 0;
		for (int i = 0; i < n; i++)
		{
			jieguo = xor(A[0], B[i]);
			for (int j = 0; j < n; j++)
			{
				tmp[j] = xor(A[j],jieguo);
			}
			sort(tmp, tmp + n);
			int tt = 0;
			for (int j = 0; j < n; j++)
			{
				if (tmp[j] != B[j])
				{
					tt = 1;
					break;
				}
			}
			if (tt == 0)
			{
				int sum = jishu(jieguo);
				mark = 1;
				if (min > sum)
					min = sum;
			}

		}
		if (mark == 1)
			cout << "Case #" << i + 1 << ": " << min << endl;
		else
			cout << "Case #" << i + 1 << ": " << "NOT POSSIBLE"<<endl;
	}
	return 0;
}