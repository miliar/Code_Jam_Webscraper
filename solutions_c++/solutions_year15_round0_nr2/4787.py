#include <stdio.h>
#include <string.h>
#include <iostream>
#include <string>
#include <algorithm>
#include <set>
#include <map>
using namespace std;

int p[1010], n;
map <vector <int>, int> m;

int sol (vector <int> v){
	if (v.size() == 0)
		return 0;

	/*for (int i=0;i<v.size();i++)
		printf ("%d ", v[i]);
	printf ("\n");*/
		

	sort (v.begin(), v.end());

	if (m.find (v) != m.end())
		return m[v];

	int ret = 1<<30;

	vector <int> nv;

	for (size_t i=0;i<v.size();i++){
		if (v[i] > 1)
			nv.push_back(v[i]-1);
	}
	ret = min (ret, sol (nv) + 1);

	nv.clear();
	for (size_t i=0;i<v.size();i++)
		nv.push_back(v[i]);

	nv.push_back(0);

	for (size_t i=0;i<v.size();i++){
		for (int j=1;j<v[i];j++){
			nv[i] -= j;
			nv.back() = j;
			ret = min (ret, sol (nv)+1);
			nv[i] += j;
		}
	}

	return m[v] = ret;
}

int main (){
	
	freopen ("input.txt", "r", stdin);
	freopen ("output2.txt", "w", stdout);
	
	int t;
	scanf ("%d", &t);

	for (int tc = 1;tc<=t;tc++){

		scanf ("%d", &n);

		for (int i=0;i<n;i++)
			scanf ("%d", &p[i]);

		sort (p, p+n);
		reverse (p, p+n);

		vector <int> init;
		for (int i=0;i<n;i++)
			init.push_back(p[i]);

		printf ("Case #%d: %d\n", tc, sol(init));
	}
	return 0;
}
