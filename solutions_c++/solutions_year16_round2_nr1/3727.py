
#include <iostream>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
using namespace std;

bool a[2007];

int main(){
	FILE *f1, *f2;
	freopen_s(&f1, "in.txt", "r+", stdin);
	freopen_s(&f2, "out.txt", "w+", stdout);
	string s;
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++)
	{
		for (int i = 0; i < 2000; i++)
		{
			a[i] = false;
		}
		vector<int>ans;
		cin >> s;
		for (int j = 0; j < s.length(); j++)
		{
			if (!a[j])
			{
				if (s[j] == 'X')
				{
					a[j] = true;
					bool ts = false, ti = false;
					for (int k = 0; k < s.length(); k++)
					{
						if (!a[k])
						{

							if (!ts&& s[k] == 'S')
							{
								a[k] = true;
								ts = true;
							}
							else if (!ti&& s[k] == 'I')
							{
								a[k] = true;
								ti = true;
							}
							if (ti&&ts)
							{
								break;
							}
						}
					}
					ans.push_back(6);

				}
				else if (s[j] == 'G')
				{
					a[j] = true;
					bool te = false, ti = false, th = false, tt = false;
					for (int k = 0; k < s.length(); k++)
					{
						if (!a[k])
						{
							if (!te&&s[k] == 'E')
							{
								a[k] = true;
								te = true;
							}
							else if (!th&&s[k] == 'H')
							{
								a[k] = true;
								th = true;
							}
							else if (!ti&&s[k] == 'I')
							{
								a[k] = true;
								ti = true;
							}
							else if (!tt&&s[k] == 'T')
							{
								a[k] = true;
								tt = true;
							}
							if (te&&tt&&ti&&th)
							{
								break;
							}
						}
					}
					ans.push_back(8);
				}
				else if (s[j] == 'U')
				{
					a[j] = true;
					bool tf = false, to = false, tr = false;
					for (int k = 0; k < s.length(); k++)
					{
						if (!a[k])
						{
							if (!tf&&s[k] == 'F')
							{
								a[k] = true;
								tf = true;
							}
							else if (!to&&s[k] == 'O')
							{
								a[k] = true;
								to = true;
							}
							else if (!tr&&s[k] == 'R')
							{
								a[k] = true;
								tr = true;
							}
							if (tr&&tf&&to)
							{
								break;
							}
						}
					}
					ans.push_back(4);
				}
				else if (s[j] == 'Z')
				{
					a[j] = true;
					bool te = false, tr = false, to = false;
					for (int k = 0; k <= s.length(); k++)
					{
						if (!a[k])
						{
							if (!te&&s[k] == 'E')
							{
								a[k] = true;
								te = true;
							}
							else if (!tr&&s[k] == 'R')
							{
								a[k] = true;
								tr = true;
							}
							else if (!to&&s[k] == 'O')
							{
								a[k] = true;
								to = true;
							}
							if (te&&tr&&to)
							{
								break;
							}
						}
					}
					ans.push_back(0);

				}
			}
		}
		for (int j = 0; j < s.length(); j++)
		{
			if (!a[j])
			{
				if (s[j] == 'S')
				{
					a[j] = true;
					int te = 0;
					bool tv = false, tn = false;
					for (int k = 0; k < s.length(); k++)
					{
						if (!a[k])
						{
							if (te < 2 && s[k] == 'E')
							{
								te++;
								a[k] = true;
							}
							else if (!tv&&s[k] == 'V')
							{
								tv = true;
								a[k] = true;
							}
							else if (!tn&&s[k] == 'N')
							{
								tn = true;
								a[k] = true;
							}
							if (te == 2 && tv&&tn)
							{
								break;
							}
						}
					}
					ans.push_back(7);
				}
				else if (s[j] == 'F')
				{
					a[j] = true;
					bool ti = false, tv = false, te = false;
					for (int k = 0; k < s.length(); k++)
					{
						if (!a[k])
						{

							if (!ti&&s[k] == 'I')
							{
								a[k] = true;
								ti = true;
							}
							else if (!tv&&s[k] == 'V')
							{
								a[k] = true;
								tv = true;
							}
							else if (!te&&s[k] == 'E')
							{
								a[k] = true;
								te = true;
							}
							if (ti&&tv&&te)
							{
								break;
							}
						}
					}
					ans.push_back(5);

				}
			}
		}
		for (int j = 0; j < s.length(); j++)
		{
			if (!a[j])
			{
				if (s[j] == 'I')
				{
					a[j] = true;
					int tn = 0;
					bool te = false;
					for (int k = 0; k < s.length(); k++)
					{
						if (!a[k])
						{
							if (tn < 2 && s[k] == 'N')
							{
								tn++;
								a[k] = true;
							}
							else if (!te&&s[k] == 'E')
							{
								te = true;
								a[k] = true;
							}
							if (tn == 2 && te)
							{
								break;
							}
						}
					}
					ans.push_back(9);
				}
			}
		}
		for (int j = 0; j < s.length(); j++)
		{
			if (!a[j])
			{
				if (s[j] == 'N')
				{
					a[j] = true;
					bool to = false, te = false;
					for (int k = 0; k < s.length(); k++)
					{
						if (!a[k])
						{
							if (!to&&s[k] == 'O')
							{
								to = true;
								a[k] = true;
							}
							else if (!te&&s[k] == 'E')
							{
								te = true;
								a[k] = true;
							}
							if (to&&te)
							{
								break;
							}
						}
					}
					ans.push_back(1);

				}
				else if (s[j] == 'W')
				{
					a[j] = true;
					bool tt = false, to = false;
					for (int k = 0; k < s.length(); k++)
					{
						if (!a[k])
						{
							if (!tt&&s[k] == 'T')
							{
								tt = true;
								a[k] = true;
							}
							else if (!to&&s[k] == 'O')
							{
								to = true;
								a[k] = true;
							}
							if (tt&&to)
							{
								break;
							}
						}
					}
					ans.push_back(2);

				}
			}
		}
		int kl = 0;
		for (int j = 0; j < s.length(); j++)
		{
			if (!a[j])
			{
				kl++;
				if (kl == 4)
				{
					kl = 0;
					ans.push_back(3);
				}
			}
		}
		sort(ans.begin(), ans.end());
		cout << "Case #" << i << ": ";
		for (int j = 0; j < ans.size(); j++)
		{
			cout << ans[j];
		}
		cout << endl;
	}
	return 0;
}

