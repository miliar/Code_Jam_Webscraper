#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <complex>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <complex>
#include <stdio.h>
#include <cstdlib>
#include <memory.h>
#include <ctime>

const double pi = 3.1415926535897932384626433832795;
const int INF = 2000000000;
double E=1e-9;

#define sz size()
#define pb push_back
#define ALL(a) (a).begin(), (a).end()
#define MEMS(a,b) memset(a,b,sizeof(a))
#define sqr(a) ((a)*(a))
#define MAX(a,b) ((a>=b)?a:b)
#define MIN(a,b) ((a<=b)?a:b)
#define ABS(a) ((a<0)?-(a):a)
#define FOR(i,a,b) for (int i=(a);i<(b);++i)
#define VVI vector < vector <int> >
#define LL long long
LL gcd(LL a, LL b){if (a==0) return b;return gcd(b%a,a);}
LL lcm (LL a, LL b) {return a / gcd (a, b) * b;}

using namespace std;

int main()
{
	//freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);
	char game[4][4];
	int T;

	cin >> T;
	FOR(i, 0, T)
	{
		FOR(j, 0, 4)
			FOR(k, 0, 4)
				cin >> game[j][k];

		int cntDots = 0;
		string res = "";
		bool isThereT;
		int cntX, cntO;
		FOR(j, 0, 4)
		{			
			isThereT = 0;
			cntX = cntO = 0;

			FOR(k, 0, 4)
				if(game[j][k] == 'X')
					cntX ++;
				else if(game[j][k] == 'O')
					cntO ++;
				else if(game[j][k] == 'T')
					isThereT = 1;
				else cntDots ++;

			if(cntX == 4 || (cntX == 3 && isThereT))
			{
				res = "X won";
				break;
			}if(cntO == 4 || (cntO == 3 && isThereT)) 
			{
				res = "O won";				
				break;
			}

			isThereT = 0;
			cntX = cntO = 0;
			FOR(k, 0, 4)
				if(game[k][j] == 'X')
					cntX ++;
				else if(game[k][j] == 'O')
					cntO ++;
				else if(game[k][j] == 'T')
					isThereT = 1;
				else cntDots ++;

			if(cntX == 4 || (cntX == 3 && isThereT))
			{
				res = "X won";
				break;
			}if(cntO == 4 || (cntO == 3 && isThereT)) 
			{
				res = "O won";				
				break;
			}
		}


		isThereT = 0;
		cntX = cntO = 0;
		FOR(k, 0, 4)
			if(game[k][k] == 'X')
				cntX ++;
			else if(game[k][k] == 'O')
				cntO ++;
			else if(game[k][k] == 'T')
				isThereT = 1;

		if(cntX == 4 || (cntX == 3 && isThereT))
			res = "X won";
		if(cntO == 4 || (cntO == 3 && isThereT))
			res = "O won";		
		
		isThereT = 0;
		cntX = cntO = 0;
		FOR(k, 0, 4)
			if(game[k][3 - k] == 'X')
				cntX ++;
			else if(game[k][3 - k] == 'O')
				cntO ++;
			else if(game[k][3 - k] == 'T')
				isThereT = 1;

		if(cntX == 4 || (cntX == 3 && isThereT))
			res = "X won";
		if(cntO == 4 || (cntO == 3 && isThereT))
			res = "O won";	


		if(res == ""){
			if(cntDots == 0)
				res = "Draw";
			else res = "Game has not completed";
		}

		cout << "Case #" << i + 1 << ": " << res << endl;
	}

	return 0;
}