// ConsoleApplication1.cpp : Defines the entry point for the console application.
//

#include "stdio.h"
#include "conio.h"
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <sstream>
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
#define SZ(x) (int)(x.size())
#define F0(i,n) for(int i=0;i<n;i++)
#define RF0(i,n) for(int i=n-1;i>=0;i--)
#define F1(i,n) for(int i=1;i<=n;i++)
#define RF1(i,n) for(int i=n;i>=1;i--)
const int MOD = 1000002013;
const double pi = atan(1.0)*4.0;
const double eps = 1e-8;
ll ucln(ll x, ll y) { return y ? ucln(y, x%y) : x; }
ll bcnn(ll x, ll y) { return (x*y) / ucln(x, y); }
bool prime(ll n) { for (ll i = 2, size = sqrt(n); i <= size; i++) if (n%i == 0) return false;	return true; }
int bc(int n) { return n ? bc((n - 1)&n) + 1 : 0; }
/*
int get_line_intersection(float p0_x, float p0_y, float p1_x, float p1_y,
	float p2_x, float p2_y, float p3_x, float p3_y, float *i_x = NULL, float *i_y = NULL)
{
	float s1_x, s1_y, s2_x, s2_y;
	s1_x = p1_x - p0_x;     s1_y = p1_y - p0_y;
	s2_x = p3_x - p2_x;     s2_y = p3_y - p2_y;

	float s, t;
	s = (-s1_y * (p0_x - p2_x) + s1_x * (p0_y - p2_y)) / (-s2_x * s1_y + s1_x * s2_y);
	t = (s2_x * (p0_y - p2_y) - s2_y * (p0_x - p2_x)) / (-s2_x * s1_y + s1_x * s2_y);

	if (s >= 0 && s <= 1 && t >= 0 && t <= 1)
	{
		// Collision detected
		if (i_x != NULL)
			*i_x = p0_x + (t * s1_x);
		if (i_y != NULL)
			*i_y = p0_y + (t * s1_y);
		return 1;
	}

	return 0; // No collision
}
*/
bool f;
int n, p[1000];
int t, ret, x;

bool check(int p[], int n) {
	int total = 0;
	F0(i, n)	total += p[i];
	F0(i, n) {
		if (p[i] * 1.0 / total > 0.5) {
			return false;
		}
	}
	return true;
}

int main() {

	//freopen("test.in", "r", stdin);
	//freopen("test.out", "w", stdout);

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	//freopen("A-large-practice.in", "r", stdin);
	//freopen("A-large-practice.out", "w", stdout);
	

	cin >> t;

	//t = 1; // test
	
	F0(i, t) {
		cin >> n;

		ret = 0;
		F0(j, n) {
			cin >> p[j];
			ret += p[j];
			//cout << p[j] << " ";
		}
		//cout << endl;
		cout << "Case #" << i + 1 << ": ";

		while (ret > 0) {
			int _max1 = -1;
			int _max2 = -1;
			F0(j, n) {
				if (_max1 < 0 || p[_max1] < p[j])	_max1 = j;
			}
			F0(j, n) {
				if ((j != _max1) && (_max2 < 0 || p[_max2] < p[j]))	_max2 = j;
			}
			//cout << endl << "ret = " << ret << " -- _max1 = " << _max1 << "    _max2 = " << _max2 << " ";
			if ((p[_max1] > 1 && p[_max2] > 1) || (p[_max1] + p[_max2] == ret)) {
				p[_max1]--;
				p[_max2]--;
				ret -= 2;
				cout << (char)(_max1 + 'A') << (char)(_max2 + 'A') << " ";
			}
			else if (p[_max1] > 0) {
				if (p[_max1] == 2 && p[_max2] == 1) {
					p[_max1]--;
					ret -= 1;
					cout << (char)(_max1 + 'A');
				}
				p[_max1]--;
				ret -= 1;
				cout << (char)(_max1 + 'A') << " ";
			}
		}

		cout << endl;
	}
	

	getch();
	return 0;
}
