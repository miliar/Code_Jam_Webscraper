#include <iostream>
#include <string>

using namespace std;

string set[10] = {"ZERO", "TWO", "FOUR", "SIX", "EIGHT", "SEVEN", "FIVE", "NINE", "ONE", "THREE"};
int nums[10] = {0, 2, 4, 6, 8, 7, 5, 9, 1, 3};

int count(string a, int *c)
{
	
	int d[27];

	for(int j=0;j<26;j++)
		d[j] = 0;

	for(int i=0;i<a.size();i++)
		d[a[i]-'A']++;

	int min = 10000000;

	for(int i=0;i<a.size();i++)
	{
		int need = c[a[i]-'A'] / d[a[i]-'A'];
		if(need<min)
			min = need;
	}
	for(int i=0;i<a.size();i++)
		c[a[i]-'A']-=min;		
	return min;
}

int main()
{
	int t;
	cin >> t;
	for(int i=0;i<t;i++){
		
		string inp;
		int c[27];
		int d[10];

		for(int j=0;j<26;j++)
			c[j] = 0;

		cin >> inp;

		for(int j=0;j<inp.size();j++)
		{
			char ch = inp [j];
			c[ch-'A']++;
		}

		//for(int j=0;j<26;j++)
		//	cout << char(j+'A') << " : " << c[j] << endl;

		cout << "Case #" << i+1 << ": ";
		for(int j=0;j<10;j++)
			d[nums[j]] = count(set[j], c);
		for(int j=0;j<10;j++){
			for(int k=0;k<d[j];k++)
				cout << j;
		}
		cout << endl;
	}

	return 0;
}