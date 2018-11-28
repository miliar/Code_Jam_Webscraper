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

double a[MAXN];
double b[MAXN];

int a1[MAXN];
int b1[MAXN];

int main() 
{
    freopen("D-large.in", "r", stdin);
    freopen("D-large.out", "w", stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		for (int j = 0; j < 1100; j++)
		{
			b1[j] = 0;
		}
		int n;
		cin >> n;
		for (int j = 0; j < n; j++)
		{
			scanf("%lf", &a[j]);
		}
		for (int j = 0; j < n; j++)
		{
			scanf("%lf", &b[j]);
		}
		int answer1 = 0;
		sort(a, a + n);
		sort(b, b + n);
		int z = n - 1;
		int index = n;
		for (int j = 0; j < n; j++)
		{
			if (a[n - 1] > b[z])
			{
				index = j;
				break;
			}
			z--;
		}
		for (int j = n - 1; j >= index; j--)
		{
			if (b[z] > a[j])
			{
				j = j + 1;
				index = index + 1;
				z--;
				continue;
			}
			answer1++;
			z--;
		}
		int answer2 = 0;
		for (int j = 0; j < n; j++)
		{
			int c = 0;
			for (int z = 0; z < n; z++)
			{
				if (b[z] > a[j] && b1[z] != 1)
				{
					b1[z] = 1;
					c = 1;
					break;
				}
			}
			if (c == 0)
			{
				answer2++;
				for (int z = 0; z < n; z++)
				{
					if (b1[z] != 1)
					{
						b1[z] = 1;
						break;
					}
				}
			}
		}
		for (int j = 0; j < 1100; j++)
		{
			b1[j] = 0;
		}
		int answer3 = 0;
		for (int j = n - 1; j >= 0; j--)
		{
			int c = 0;
			for (int z = 0; z < n; z++)
			{
				if (b[z] > a[j] && b1[z] != 1)
				{
					b1[z] = 1;
					c = 1;
					break;
				}
			}
			if (c == 0)
			{
				answer3++;
				for (int z = 0; z < n; z++)
				{
					if (b1[z] != 1)
					{
						b1[z] = 1;
						break;
					}
				}
			}
		}
		cout << "Case #" << i + 1 << ": " << answer1 << " " << max(answer3, answer2) << endl;
	}
}