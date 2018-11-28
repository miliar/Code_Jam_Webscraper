#include<iostream>
#include<queue>
#include<map>
#include<cstring>
#include<utility>
#include<vector>
#include<climits>
#include<iomanip>
#include<set>
#include<algorithm>
#include<string>
#include<cmath>
#include<math.h>
#include<cstdlib>
#include<stack>
#include<cstdio>
#include<stdio.h>
using namespace std;
int t, motes, Armin, arr[1000001];
int res(int index, int operations, int cur)
{
	if(index == motes)
		return operations;
	else if(cur > arr[index])
		return res(index + 1, operations, cur + arr[index]);
	else if(cur != 1)
		return min(res(index + 1, operations + 1, cur), res(index, operations + 1, 2 * cur - 1));
	else
		return res(index + 1, operations + 1, cur);

}

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> t;
	for(int i = 1; i <= t; i++)
	{
		cin >> Armin >> motes;
		for(int j = 0; j < motes; j++)
		{
			cin >> arr[j];
		}
		sort(arr, arr + motes);
		cout << "Case #" << i << ": " << res(0, 0, Armin) << endl;
	
	}
	
	
	return 0;
}








