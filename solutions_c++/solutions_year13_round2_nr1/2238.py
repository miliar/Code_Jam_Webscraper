#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <string>
using namespace std;

int size[101];
int a, n;
int ans;

int go(int total, int start, int end)
{
	if(start == end)
	{
		if(total > size[start])
			return 0;
		else
			return 1;
	}
	if(total > size[start])
	{
		return go(total+size[start], start+1, end);
	}
	else if(total > 1)
		return min(go(total+total-1, start, end), go(total, start, end-1)) + 1;
	else
		return go(total, start, end-1) + 1;
}

int main()
{
	//freopen("input.txt", "r", stdin);
	//freopen("C-large-1.in", "r", stdin);
	//freopen("A.txt", "w", stdout);
	int T;
	cin>>T;
	for(int t=0; t<T; t++)
	{
		
		cin>>a>>n;
		ans = 0;
		for(int i=0; i<n; i++)
		{
			cin>>size[i];
		}
		sort(size, size+n);
		ans = go(a, 0, n-1);
		printf("Case #%d: %d\n", t+1, ans);
	}
	fclose(stdout);
	fclose(stdin);
	return 0;
}

