#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <bitset>
#include <deque>
#include <utility>
#include <sstream>

#define clear(a) memset(a, 0, sizeof(a))
#define initNeg(a) memset(a, -1, sizeof(a))
#define INF 1000000000
#define FOR(i, a, b) for(int i=int(a); i<=int(b); i++)
#define REP(i, b) for(int i=0; i<=int(b); i++)
#define p2(b) (1 << (b))

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

template <typename T> string toString(T n){ostringstream ss; ss << n; return ss.str();}
template <typename T> T toNum(const string &Text){istringstream ss(Text); T result; return ss >> result ? result : 0;}

int main()
{

	int TC;
	cin >> TC;
	FOR(T, 1, TC)
	{

		int N, M;
		cin >> N >> M;

		int arr[N][M];

		REP(i, N-1)
			REP(j, M-1)
				cin >> arr[i][j];

		bool allgood = true;
		REP(row, N-1)
		{
			REP(column, M-1)
			{
				if(allgood)
				{
					bool goodR = true;
					REP(i, N-1)
					{	
						if(goodR)
						{
							if(arr[i][column] > arr[row][column])
								goodR = false;
						}
					}	


					bool goodC = true;
					REP(i, M-1)
					{
						if(goodC)
						{
							if(arr[row][i] > arr[row][column])
								goodC = false;
						}
					}

					if(!goodR && !goodC)
						allgood = false;
				}
			}

		}

		cout << "Case #" << T << ": " << (allgood ? "YES" : "NO") << endl; 
	}


}