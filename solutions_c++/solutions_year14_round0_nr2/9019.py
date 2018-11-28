#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <string>
#include <string.h>
#include <vector>
#include <set>
#include <map>
#include <queue>

using namespace std;

#define ll long long
#define ld long double
#define ull unsigned long long
#define pb push_back
#define mp make_pair
#define y0 isdnfviu
#define y1 asinhiv
#define fst first
#define snd second
#define count sdifnsugh

bool used[111];
int t;
ld x,c,f;

int main()
{
	freopen("input.in","r",stdin);
	freopen("output.txt","w",stdout);
	cin >> t;
	for(int k=1; k<=t; k++)
	{
		cin >> c >> f >> x;
		ld kol=2.0;
		ld time=0;
		while(true)
		{
			ld cc=c*(kol+f), xx=x*kol;
			ld first=x*kol*(kol+f),sec=kol*(cc+xx);
			if (first<=sec)
			{
				time+=x/kol;
				break;
			}
			time+=c/kol;
			kol+=f;
		}
		cout.precision(8);
		cout << "Case #" << k << ": ";	
		cout << fixed << time << "\n";
	}
	cin >> t;
	return 0;
}
