#include<iostream>
#include<string>
#define ll long long
#pragma warning ( disable : 4996)
using namespace std;


bool digits[10];
char paras[20];


bool checkdigits()
{
	for (int i = 0; i < 10; i++)
	{
		if (digits[i] == false)
		{
			return false;
		}
	}
	return true;
}
int main()
{
	freopen("output.txt", "w", stdout);
	freopen("input.txt", "r", stdin);
	ll T;
	ll para;
	ll temp;
	cin >> T;
	for (ll i = 0; i < T; i++)
	{
		//init
		temp = 0;
		memset(digits, false, 10);
		memset(paras, 11, 20);
		//init end
		cin >> para;
		if (para == 0)
		{
			cout << "Case #" << i + 1 << ": " << "INSOMNIA" << endl;
			continue;
		}
		while (true)
		{
			temp += para;
			sprintf(paras, "%d", temp);
			int para_len = strlen(paras);
			for (int k = 0; k < para_len; k++)
			{
				digits[paras[k] - '0'] = true;
			}
			if (checkdigits())
			{
				cout << "Case #" << i + 1 << ": " << temp << endl;
				break;
			}
			
		}

	}

}