#define _USE_MATH_DEFINES 
#define _CRT_SECURE_NO_DEPRECATE 
#include <iostream> 
#include <cstdio> 
#include <cstdlib> 
#include <vector> 
#include <sstream> 
#include <string> 
#include <map> 
#include <set> 
#include <algorithm> 
#include <cmath> 
#include <cstring> 
#include <queue>
using namespace std; 
#pragma comment(linker, "/STACK:256000000") 
#define mp make_pair 
#define pb push_back 
#define all(C) (C).begin(), (C).end() 
#define sz(C) (int)(C).size() 
#define PRIME 1103 
#define PRIME1 31415 
typedef long long int64; 
typedef unsigned long long uint64; 
typedef pair<int, int> pii; 
typedef vector<int> vi; 
typedef vector<vector<int> > vvi; 
//------------------------------------------------------------ 
const int N = 317;
int l, x;
int mat[4][4] = 
{
	{1, 2, 3, 4},
	{2, -1, 4, -3},
	{3, -4, -1, 2}, 
	{4, 3, -2, -1}
};
int mas[150000];
int d[2][2][5][5];
int q = 0;
string solve()
{
	string st;
	cin >> l >> x;
	cin >> st;
	q = 0;
	memset(d, 0, sizeof d);
	for(int i = 0; i < l; ++i)
	{
		if (st[i] == 'i')
			mas[i] = 2;
		if (st[i] == 'j')
			mas[i] = 3;
		if (st[i] == 'k')
			mas[i] = 4;
	}
	
	int n = 0;
	//if (x < 12)
	//{
		for(int i = 1; i < x; ++i)
			for(int j = 0; j < l; ++j)
				mas[i * l + j] = mas[j];
		n = l * x;
/*	}
	else
	{
		for(int i = 1; i < 12 + x % 4; ++i)
			for(int j = 0; j < l; ++j)
				mas[i * l + j] = mas[j];
		n = (12 + x % 4) * l;
	}*/
	d[0][0][0][0] = 1;
	for(int i = 0; i < n; ++i)
	{
		for(int j = 0; j < 4; ++j)
			for(int k = 0; k < 3; ++k)
			{
				d[q ^ 1][0][j][k] = 0;
				d[q ^ 1][1][j][k] = 0;
			}
		
		for(int j = 0; j < 4; ++j)
			for(int k = 0; k < 3; ++k)
			{
				if (d[q][0][j][k])
				{
					int t = mat[j][mas[i] - 1];
					
					int b = t < 0;
					//cerr << i << ' ' << t << ' ' << b << ' ' << k << endl;
					d[q ^ 1][b][abs(t) - 1][k] = 1;
					if (abs(t) == k + 2)
						d[q ^ 1][b][0][k + 1] = 1;
				}
				if (d[q][1][j][k])
				{
					int t = mat[j][mas[i] - 1];
					int b = t > 0;
					d[q ^ 1][b][abs(t) - 1][k] = 1;
					if (abs(t) == k + 2)
						d[q ^ 1][b][0][k + 1] = 1;
				}
			}
		q ^= 1;
		
	}
	
	if (d[q][0][3][2] == 1)
		return "YES";
	else
		return "NO";
//pos[i] = sign * mat[mas[i] - 1][abs(pos[i + 1]) - 1];
	
}

int main() 
{
#ifdef WIN32
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
	int t;
	cin >> t;
	for(int i = 0; i < t; ++i)
	{
		if (solve() == "YES")
			printf("Case #%d: YES\n", i + 1);
		else
			printf("Case #%d: NO\n", i + 1);
	}
}