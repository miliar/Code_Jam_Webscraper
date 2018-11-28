//////////////////////////////////////////////
//Author: Adrian Seitan: seitan.adi@gmail.com
//////////////////////////////////////////////

#include<bits/stdc++.h>

using namespace std;



string solveThis(int val)
{
	string res = "";
	int myarr[10] = {0};
	for (int i = 1; i < 100; i++)
	{
		long long int mult = (long long)i * (long long)val;
		long long mult2 = mult;
		while (mult != 0)
		{ char ch = mult % 10; 
		mult = mult / 10;
		myarr[ch] = 1; }

		int j = 0;
		for (; j < 10; j++) if (myarr[j] == 0){ break; }
		if (j == 10)
		{
			res += to_string(mult2);
			return res;
		}
	}
	res += "INSOMNIA";
	return res;
}

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);

	int cases, writtenCase = 1;
	cin >> cases;
	while (--cases >= 0)
	{
		int N;
		cin >> N;
		cout << "Case #" << writtenCase++ << ": " << solveThis(N) << endl;
	}

	
	return 1;
}
