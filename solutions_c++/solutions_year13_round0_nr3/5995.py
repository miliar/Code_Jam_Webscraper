#include <iostream>
#include <algorithm>
#include <string>
#include <set>
#include <vector>
#include <queue>
#include <fstream>
#include <sstream>
#include <map>
#include <list>
#include <cmath>
#include <bitset>
#include <stack>
#include <stdio.h>
#include <cstring>
#include <ctime>
#include <ctype.h>
#include <utility>
#include <stdlib.h>
#include <stdio.h>
#include <cstdio>
using namespace std;
 
#define mod 1000000007
#define ll long long
#define INF 1000000000
#define PI 3.1415926

bool ispal[10000001];
ll numpals[10000001];

bool isPalin (ll a)
{
	string s = "";

	while (a != 0)
	{
		s = char((a % 10) + '0') + s;
		a /= 10;
	}

	for (int i = 0; i < s.size()/2; i++)
		if (s[i] != s[s.size()-1-i])
			return false;

	return true;
}

int main (void)
{

    ifstream cin("C-small-attempt0 (1).in");
	ofstream cout("out.txt");

    int t;
	cin >> t;

	memset(numpals, 0, sizeof(numpals));
	numpals[0] = 0;

	for (ll i = 1; i <= 1000; i++)
	{
		numpals[i] = numpals[i-1];
		if (isPalin(i) && isPalin(i*i))
			numpals[i]++;
	}
	
	for (int i = 0; i < t; i++)
	{
		ll a, b;
		cin >> a >> b;

		ll p = a;
		a = int(sqrt(double(a)));
		b = int(sqrt(double(b)));

		if (a * a == p)
			a--;

		cout << "Case #" << i+1 << ": " <<numpals[b] - numpals[a] << endl;
	}

	//while (true) {}

}