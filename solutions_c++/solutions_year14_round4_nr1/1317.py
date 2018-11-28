#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <iomanip>
#include <map>
#include <queue>
#include <ctime>
#include <cmath>

using namespace std;

#define forn(I,N) for (int I=0; I<N; I++)
#define fornd(I,N) for (int I=N-1; I>=0; I--)
#define forab(I,A,B) for (int I=A; I<=B; I++)
#define forabd(I,A,B) for (int I=B; I>=A; I--)
#define FOREACH(I,A) for (__typeof__(A)::iterator I=A.begin(); I<A.end(); I++)
#define pb push_back
#define mp make_pair

typedef long long int ll;

int main() {
	int T;
	cin >> T;
	
	forn (i, T)
	{
		int X, S;
		cin >> X >> S;
		
		vector <int> disc(X);
		forn (j, X)
			cin >> disc[j];
		sort(disc.begin(), disc.end());
		
		int ct = 0;
		vector <int> taken(X);
		forn(j, X) if (!taken[j])
		{
			taken[j] = 1;
			fornd (k, X)
			{
				if (!taken[k] && disc[j] + disc[k] <= S)
				{
					taken[k] = 1;
					break;
				}
			}
			ct++;
		}
		cout << "Case #" << i+1 << ": " << ct << endl;
	}
	
	return 0;
}