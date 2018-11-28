/*
Because I'm happy to be sad
I want it all I want it bad
Oh oh, it's what I know

A vintage year for pop I hear
The middle of the end is near
Let's go oh, it's what I know

Torture me and torture me
It's forcin' me so torture me, please
Torture me with sorcery (all night long)
It's forcin' me so torture me, please (all night long)

All the leaves are turning brown
The wind is pushing me around
Let's go oh, it's what I know

Torture me and torture me
It's forcin' me so torture me, please
Torture me with sorcery (all night long, all night long)
It's forcin' me so torture me, please (all night long, all night long)

The will of God is standing still
Brazilian children get their fill, Let's go

Let's turn it up and dumb it down
The vision of your ultra sound, It's so

All the leaves are turning brown
The wind is pushing me around, Let's go

A vintage year for pop I hear
The middle of the end is near, It's so

Torture me and torture me(all night long, all night long)
It's forcin' me so torture me, please (all night long, all night long)
Torture me with sorcery (all night long, all night long)
It's forcin' me so torture me, please (all night long, all night long) (x2)
*/

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <algorithm>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <iostream>
#include <functional>


using namespace std;
 
#define ll long long
#define mp make_pair

int answer = 0;

const int MAXN = 3000010;

int a[MAXN];
int b[MAXN];

int main() 
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		double c, f, x;
		cin >> c >> f >> x;
		double q = 2.0;
		double answer = x / q;
		double qw = 0;
		while (true)
		{
			qw = qw + (c / q);
			q = q + f;
			if (qw + x / q <= answer)
			{
				answer = qw + (x / q);
			}
			else
			{
				break;
			}
		}
		cout << "Case #" << i + 1 << ": ";
		printf("%.7lf\n", answer);
	}
}