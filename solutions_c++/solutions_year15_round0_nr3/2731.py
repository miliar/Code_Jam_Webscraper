#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define mp make_pair

map < pair <string, string> , string > mat;


int main()
{
	ios::sync_with_stdio(false);


	mat[mp("1", "i")] =  "i";
	mat[mp("1", "j")] =  "j";
	mat[mp("1", "k")] =  "k";
	
	mat[mp("-1", "i")] = "-i";
	mat[mp("-1", "j")] = "-j";
	mat[mp("-1", "k")] = "-k";

	mat[mp("i", "i")] = "-1";
	mat[mp("i", "j")] = "k";
	mat[mp("i", "k")] = "-j";
	
	mat[mp("-i", "i")] = "1";
	mat[mp("-i", "j")] = "-k";
	mat[mp("-i", "k")] = "j";
	
	mat[mp("j", "i")] = "-k";
	mat[mp("j", "j")] = "-1";
	mat[mp("j", "k")] = "i";
	
	mat[mp("-j", "i")] = "k";
	mat[mp("-j", "j")] = "1";
	mat[mp("-j", "k")] = "-i";
	
	mat[mp("k", "i")] = "j";
	mat[mp("k", "j")] = "-i";
	mat[mp("k", "k")] = "-1";
	
	mat[mp("-k", "i")] = "-j";
	mat[mp("-k", "j")] = "i";
	mat[mp("-k", "k")] = "1";
	

	int TC;
	cin >> TC;

	for (int cases = 1; cases <= TC; cases++)
	{
		int L, X;
		cin >> L >> X;

		string S = "", str;
		cin >> str;
		for (int i = 0; i < X; i++)
			S += str;

		int n = S.size();
		bool I = false, J = false, K = false;
		
		string prev = "1";	
		for (int i = 0; i < n; i++)
		{
			string p = ""; p += S[i];
			string next = mat[mp(prev, p)];
			
			if(next == "i")
				I = true;
			else if(next == "k" && I)
				J = true;	
			prev = next;
		}

		if(prev == "-1" && I && J)
				K = true;
		
		string ans;
		if(I && J && K)
			ans = "YES";
		else
			ans = "NO";

		cout << "Case #" << cases << ": ";
		cout << ans << "\n";
	}
	
	return 0;
}