#include <iostream>
#include <algorithm>
#include <queue>
#include <fstream>
#include <map>
#include <string>
#include <vector>

#define mp make_pair
#define mt make_tuple
#define fi first
#define se second
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).rend()
#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define for1(i, n) for (int i = 1; i <= (int)(n); ++i)
#define ford(i, n) for (int i = (int)(n) - 1; i >= 0; --i)
#define fore(i, a, b) for (int i = (int)(a); i <= (int)(b); ++i)

using namespace std;

typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<pii> vpi;
typedef vector<vi> vvi;
typedef long long i64;
typedef vector<i64> vi64;
typedef vector<vi64> vvi64;
typedef pair<i64, i64> pi64;
typedef double ld;

int main()
{
	ifstream inputFile;
	inputFile.open("A-large.in");
	//inputFile.open("Test.txt");
	ofstream outputFile;
	outputFile.open("result.txt");
	int T;
	inputFile >> T;
	string f;
	getline(inputFile, f);
	for (int t = 1; t <= T; t++)
	{
		string s;
		getline(inputFile, s);
		int n = s.size();
		vector<char> v;
 		forn(i, n)
		{
			if (i == 0)
			{
				v.push_back(s[i]);
				continue;
			}
			vector<char>::iterator it;

			if (s[i] >= v[0])
				v.insert(v.begin(),s[i]);
			else
				v.push_back(s[i]);

			
		}

		cout << "Case #" << t << ": " ;
		outputFile << "Case #" << t << ": " ;
		forn(i, n)
		{
			cout << v[i];
			outputFile << v[i] ;
		
		}
		cout << endl;
		outputFile << endl;
		v.clear();

	}

}