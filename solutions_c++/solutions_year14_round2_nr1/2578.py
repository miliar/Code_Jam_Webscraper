#include <cstdio>
#include <iostream>
#include <string>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

typedef long long LL;
typedef long double LD;
typedef vector<int> VI;
typedef vector<string> VS;
typedef pair<int,int> PII;
#define FOR(k,a,b) for(typeof(a) k=(a); k <= (b); ++k)
#define REP(k,a) for(int k=0; k < (a); ++k)
#define REPD(k,a) for(int k=(a)-1; k >= 0; --k)
#define PB push_back 
#define MP make_pair


int main()
{
	int T;
	cin >> T;
	REP(t,T)
	{
		int N;
		cout << "Case #" << (t+1) <<": ";
		cin >> N;
		//cout << N << endl;
		vector< string > input;
		set<char> charSet;
		set<string> subSet;
		vector< vector <int> > subVec;
		bool bOk = true;
		unsigned int maxLen = 0;
		REP(i, N)
		{
			string s;
			string sCons = "";
			vector<int> v;
			cin >> s;
			REP (j, s.size())
			{
				if (i > 0 && charSet.find(s[j]) == charSet.end())
				{
					bOk = false;
					break;
				}
				charSet.insert(s[j]);
				if (j > 0 && s[j] != s[j-1]) sCons += s[j];
				if (j == 0) sCons += s[j];
				if (j > 0 && s[j] == s[j-1]) v[v.size() - 1] += 1;
				else v.push_back(1);
			}
			//REP(j, v.size())
			//	cout << v[j] << " ";
			//cout << endl;
			subVec.push_back(v);
			//cout << sCons << endl;
			if (bOk && i > 0 && subSet.find(sCons) == subSet.end())
			{
				bOk = false;
				break;
			}
			if (! bOk) break;
			subSet.insert(sCons);
			//cout << s.length() << " " << maxLen << " " << (maxLen < s.length()) << endl;
			if (s.size() > maxLen) 
			{
				maxLen = s.size();
				//cout << s << endl;
				//cout << s.length() << endl;
				//cout << maxLen << endl;
			}
			input.push_back(s);
		}
		if (! bOk)
			cout << "Fegla Won" << endl;
		else
		{
			int res = 0;
			vector<int> v;
			
			
			REP (j,subVec[0].size())
			{
				__int64 sumLen = 0;
				REP(i,N)
				{
					sumLen += subVec[i][j];
				}
				//cout << sumLen << endl;
				v.push_back(sumLen / N);
			}
			REP(i,N)
			{
				REP(j,v.size())
				{
					res += abs(v[j] - subVec[i][j]);
				}				
			}
			cout << res << endl;
		}
	}
	
	return 0;
}

