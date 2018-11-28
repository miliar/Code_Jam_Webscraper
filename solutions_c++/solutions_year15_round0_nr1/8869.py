#include<iostream>
#include<sstream>
#include<string>
#include<string.h>
#include<cstring>
using namespace std;
#define ll long long int
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	string word;
	ll stand,size,testcases,counter;
	cin >> testcases;
	for (ll i = 1; i <= testcases; i++)
	{
		cin >> size >> word;
		stand = 0;
		counter = 0;
		size++;
		for (ll j = 0; j < size; j++)
		{
			if (stand < j && word[j] != '0')
			{
				counter += (j - stand);
				stand += (j - stand);
			}
			stand += (word[j]-'0');
		}
		cout << "Case #" << i << ": "<<counter<< endl;
	}
	return 0;
}