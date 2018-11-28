// codejam.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

#define ALL(x) (x).begin(), (x).end()

typedef vector<int> vi;
typedef vector<vector<int> > vvi;

vvi first(4, vi(4)), second(4, vi(4));

int main(int argc, char * argv[])
{
#ifndef ONLINE_JUDGE
	freopen("../A-small-attempt0.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif

	int tc;
	cin >> tc;
	for(int tt=1;  tt<=tc; tt++)
	{
		int a1;
		cin >> a1;
		a1--;
		for(int i=0;i<4;i++)
			for(int j=0; j<4;j++)
				cin >> first[i][j];

		int a2;
		cin >> a2;
		a2--;
		for(int i=0;i<4;i++)
			for(int j=0; j<4;j++)
				cin >> second[i][j];

		sort(ALL(first[a1]));
		sort(ALL(second[a2]));
		int arr[4];
		auto end = set_intersection(ALL(first[a1]), ALL(second[a2]), arr);
		if(end - arr == 0)
			printf("Case #%d: Volunteer cheated!\n", tt);
		else if(end - arr == 1)
			printf("Case #%d: %d\n", tt, arr[0]);
		else
			printf("Case #%d: Bad magician!\n", tt);

	}
	return 0;
}

