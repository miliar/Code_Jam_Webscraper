#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cctype>
#include <utility>

#include <cmath>
#include <iostream>
#include <fstream>

#include <string>
#include <vector>
#include <queue>
#include <map>
#include <algorithm>
#include <set>
#include <sstream>
#include <stack>
using namespace std;

#define MEM(a, b) memset(a, (b), sizeof(a))
#define CLR(a) memset(a, 0, sizeof(a))
#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define MIN(a, b) ((a) < (b) ? (a) : (b))
#define ABS(X) ( (X) > 0 ? (X) : ( -(X) ) )
#define S(X) ( (X) * (X) )
#define SZ(V) (int )V.size()
#define FORN(i, n) for(i = 0; i < n; i++)
#define FORAB(i, a, b) for(i = a; i <= b; i++)
#define ALL(V) V.begin(), V.end()

typedef pair<int,int> PII;
typedef pair<double, double> PDD;
typedef pair<int, long long> PILL;
typedef vector<int> VI;
typedef vector<PII > VP;


#define IN freopen("A-large.in", "r", stdin);
#define OUT freopen("outLarge.txt", "w", stdout);

#define MAX_SIZE 200010


int T, Sm;

int main()
{
	IN
	OUT
	int t, i, clapping, req;
	string S;
	while(cin >> T) {
		FORAB(t, 1, T) {
			cin >> Sm;
			cin >> S;

			int Si;
			clapping = S[0]-'0';
			req = 0;

			FORAB(i, 1, Sm) {
				Si = S[i]-'0';
				if(Si>0 && i > clapping) {
					req += i - clapping;
					clapping += i - clapping;
				}

				clapping += Si;
			}

			cout << "Case #" << t << ": " << req << endl;
		}
	}

	return 0;
}
