#include"stdafx.h"

#include<bits/stdc++.h>
using namespace std;

#define ll long long
#define mod2 1000000007
string str;
int freq[30];

int reset(string st,int len)
{
	for (char ch : st)
	{
		freq[ch - 'A'] -=len;
	}
	return len;
}

int arr[15];
int main()
{
	int t, k;
	freopen("alll.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	cin >> t;
	k = 0;
	while (t--)
	{
		k++;
		memset(freq, 0, sizeof(freq));

		memset(arr, 0, sizeof(arr));
		cin >> str;
		int i, j,ans=0;

		for (char ch : str)
			freq[ch - 'A']++;

		if (freq['Z' - 'A'])		
		{
			arr[0]=reset("ERO", freq['Z' - 'A']);
			freq['Z' - 'A'] = 0;
		}
		if (freq['W' - 'A'])
		{
			arr[2] += reset("TO", freq['W' - 'A']);
			freq['W' - 'A'] = 0;
		}
		if (freq['X' - 'A'])
		{
			arr[6] += reset("SI", freq['X' - 'A']);
			freq['X' - 'A'] = 0;
		}
		if (freq['U' - 'A'])
		{
			arr[4] += reset("FOR", freq['U' - 'A']);
			freq['U' - 'A'] = 0;
		}
		if (freq['F' - 'A'])
		{
			arr[5] += reset("IVE", freq['F' - 'A']);
			freq['F' - 'A'] = 0;
		}
		if (freq['V' - 'A'])
		{
			arr[7] += reset("SEEN", freq['V' - 'A']);
			freq['V' - 'A'] = 0;
		}

		if (freq['G' - 'A'])
		{
			arr[8] += reset("EIHT", freq['G' - 'A']);
			freq['G' - 'A'] = 0;
		}


		if (freq['T' - 'A'])
		{
			arr[3] += reset("HREE", freq['T' - 'A']);
			freq['T' - 'A'] = 0;
		}
		if (freq['O' - 'A'])
		{
			arr[1] += reset("NE", freq['O' - 'A']);
			freq['O' - 'A'] = 0;
		}
		if (freq['N' - 'A'])
		{
			arr[9] += reset("INE", freq['N' - 'A'])/2;
			freq['N' - 'A'] = 0;
		}

		cout << "Case #" << k<<": ";
		for (i = 0; i < 10; i++)
		{
			while (arr[i])
			{
				cout << i;
				arr[i]--;
			}

		}
		cout << "\n";

	}

	
	return 0;
}
