#if 1
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <functional>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;

FILE* pF;

FILE* pAnsF;

void reset();

int  N;

int C;
int a[27];
int h[27];
int main()
{
	freopen_s(&pF, "Text.txt", "r", stdin);

	freopen_s(&pAnsF, "OA.txt", "w", stdout);

	cin >> C;
	
	for (int c = 1; c <= C; c++)
	{
		cin >> N;
		int cnt = 0;
		int t = 0;
		for (int i = 1; i <= N; i++)
		{
			cin >> a[i];
			t += a[i];
			h[i] = 2 * a[i] - 1;
		}
		cout << "Case #" << c << ": ";
		for (int j = 1; j <= t; j++)
		{
			int m = 0;
			int index = 0;
			int i = 0;
			for (i = 1; i <= N; i++)
			{
				if (m < h[i])
				{
					m = h[i];
					index = i;
				}
			}
			char ch = char(65 + index - 1);
			cout << ch;		
			
			if (j % 2 == 0)
			{
				if ( j != t - 1 )
					cout << " ";
			}			
			if ((t % 2 != 0 && j == t - 2))
			{
				cout << " ";
			} 
			else
			{

			}
			

			a[index]--;
			h[index] = 2 * a[index] - 1;
		}
		cout << endl;
		reset();		
	}


	return 0;
}
void reset()
{
	for (int i = 1; i <= N; i++)
	{
		a[i] = 0;
		h[i] = 0;
	}
}
#endif