#include <stdio.h>
#include <string.h>
#include <queue>
#include <map>
#include <algorithm>
#include <iostream>
using namespace std;

map <pair <pair<int, int>, int>, int> mp;

int r, c, n;

int cnt (int b){
	int ret = 0;
	while (b){
		ret += b%2;
		b /=2;
	}
	return ret;
}

int nbg (int b){
	int last = 0;
	int ret = 0;

	while (b){
		if (b%2 && last)
			ret++;
		last = b%2;
		b /= 2;
	}
	return ret;
}

int sol (int y, int b, int l){
	if (y == r)
		return l?1<<30:0;

	pair <pair<int,int>, int> p;
	p.first.first = y;
	p.first.second = b;
	p.second = l;

	if (mp.find(p) != mp.end())
		return mp[p];

	int ret = 1<<30;

	for (int i=0;i<(1<<c);i++){
		int k = cnt(i);
		if (k > l)
			continue;
		ret = min (ret, sol (y+1, i, l-k) + nbg(i) + cnt(i&b));
	}

	return mp[p] = ret;
}

int main (){
	
	freopen ("b_input.txt", "r", stdin);
	freopen ("b_output.txt","w",stdout);
	
	int t;
	scanf ("%d", &t);

	for (int tc=1;tc<=t;tc++){
		
		scanf ("%d %d %d", &r, &c, &n);

		if (r<c)
			swap(r, c);

		mp.clear();
		int ret = sol (0, 0, n);

		printf ("Case #%d: %d\n", tc, ret);
	}
	return 0;
}
