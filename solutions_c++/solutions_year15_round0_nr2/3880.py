#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>
#include <string>
#include <map>
#include <set>
using namespace std;

map<map<int, int>, int> cash;

int z(map<int, int> a){
	if (cash.count(a) != 0)
		return cash[a];

	if (a.empty()){
		return cash[a] = 0;
	}							  
	map<int, int> c = a;
	int ans = a.rbegin()->first;
	for (map<int, int>::iterator it = a.begin(); it != a.end(); it++){

		int d = it->first;
		int cnt = it->second;
		if (d <= 1) continue;
		c.erase(d);

		int one = 0;
		int two = d;
		for (int i = 0; i < d; i++){
			one++;
			two--;
			if (one < 1 || two < 1) continue;
			c[one] += cnt;
			c[two] += cnt;
			ans = min(ans, cnt + z(c));
			c[one] -= cnt;
			c[two] -= cnt;
			if (c[one] <= 0) c.erase(one);
			if (c[two] <= 0) c.erase(two);
		}
		c[d] = cnt;
	}
	return cash[a] = ans;
}



int  main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	cin >> t;
	for (int q = 1; q <= t; q++)
	{
		int n;
		map <int, int> a;
		scanf("%d", &n);
		for (int i = 0; i < n; i++)
		{
			int temp;
			scanf("%d", &temp);
			a[temp]++;
		}
		
		cout << "Case #" << q << ": " << z(a) << endl;
	}
	return 0;
}