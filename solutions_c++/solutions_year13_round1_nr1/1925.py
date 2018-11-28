#include <iostream>
#include <sstream>
#include <string>
#include <queue>
#include <functional> // For less<> greater<>
#include <algorithm>

using namespace std;

typedef long long ull;

ull last = -3;

void Solve(ull r, ull t)
{
	ull first_r = r;
	ull kalan = t;
	int sayi = 0;
	while (kalan > 0)
	{
		ull fark = 2*first_r + last + 4;
		if (kalan >= fark)
		{
			kalan = kalan - fark;
			sayi++;
			r += 2;
			last = last + 4;
		}
		else
			break;
	}

	cout << sayi;
}

int main()
{
	int case_count;
	cin >> case_count;

	for (int i = 0; i < case_count; i++)
	{
		// Do whatever you want here
		ull r, t;
		cin >> r >> t;

		// Call Solve function with your parameters
		cout << "Case #" << i + 1 << ": ";
		last = -3;
		Solve(r, t);
		cout << endl;
	}

	getchar();
	return EXIT_SUCCESS;
}