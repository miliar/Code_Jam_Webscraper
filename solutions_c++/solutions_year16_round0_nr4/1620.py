#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int t;
	cin >> t;
	for (int i=0; i<t; i++)
	{
		int k,c,s;
		cin >> k >> c >> s;
		printf ("Case #%d:",i+1);
		for (int j=1; j<=s; j++)
			printf (" %d", j);
		printf ("\n");
	}
}
