#include <bits/stdc++.h>
using namespace std;
#define int long long

int d, cakes[1262];

void pain()	{
	cin >> d;
	int maximumPresent = -1, assertedMaximum, minTime = 262000000, tempTime = 0;
	for(int i=0; i<d; i++)	{
		cin >> cakes[i];
		maximumPresent = max(maximumPresent, cakes[i]);
	}
	for(assertedMaximum = 1; assertedMaximum <= maximumPresent; assertedMaximum++)	{
		for(int i=0; i<d; i++)	{
			if(cakes[i] > assertedMaximum)	{
				tempTime += (cakes[i] + assertedMaximum - 1) / assertedMaximum - 1;
			}
		}
		minTime = min(minTime, assertedMaximum + tempTime);
		tempTime = 0;
	}
	cout << minTime << "\n";
}

#undef int
int main()	{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	string input = "input-qual-B.txt";
	string output = "output-qual-B.txt";
	freopen(input.c_str(), "r", stdin);
	freopen(output.c_str(), "w", stdout);
	int tt; cin >> tt;
	for(int iii=1; iii<=tt; iii++)	{
		cout << "Case #" << iii << ": ";
		pain();
	}
}
