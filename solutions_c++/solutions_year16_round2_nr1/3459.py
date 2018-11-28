#include <iostream>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <iomanip>

template<typename T> inline bool chkmin(T &a, const T &b) { return a > b ? a = b, 1 : 0; }
template<typename T> inline bool chkmax(T &a, const T &b) { return a < b ? a = b, 1 : 0; }

using namespace std;
int table[26]={0};
vector<int> res;
bool dp()
{
	int sum = 0;
	for(int i = 0;i < 26; i++)
	{
		sum += table[i];

	}
	if (sum == 0) return true;
	
	if (table[25]>0)
	{
		res.push_back(0);
		table[25]--; table['E'-'A']--;table['R'-'A']--;table['O'-'A']--;
			for(int i = 0; i < 26; i++)
 				if(table[i] < 0)
 					cout << 0 <<endl;
		if(dp())
			return true;
		else
		{
			table[25]++; table['E'-'A']++;table['R'-'A']++;table['O'-'A']++;
			res.pop_back();
		}
	}


		if (table['O'-'A']>0  && table['N'-'A']>0 && table['E'-'A']>0 )
	{
		res.push_back(1);
		table['O'-'A']--; table['N'-'A']--;table['E'-'A']--;
					for(int i = 0; i < 26; i++)
 				if(table[i] < 0)
 					cout << 1 <<endl;
		if(dp())
			return true; 
		else
		{
			table['O'-'A']++; table['N'-'A']++;table['E'-'A']++;
			res.pop_back();
		}
	}


		if (table['T' - 'A'] > 0 && table['W'-'A']>0  && table['O'-'A'] > 0 )
	{
		res.push_back(2);
		table['T'-'A']--;  table['W'-'A']--; table['O'-'A']--;
					for(int i = 0; i < 26; i++)
 				if(table[i] < 0)
 					cout << 2 <<endl;
		if(dp())
			return true;
		else
		{
			table['T'-'A']++;  table['W'-'A']++; table['O'-'A']++;
			res.pop_back();
		}
	}


		if ( table['T'-'A']>0 && table['H'-'A']>0 && table['R'-'A']>0 && table['E'-'A'] > 1  )
	{
		res.push_back(3);
		table['T'-'A']--; table['H'-'A']--; table['R'-'A']--; table['E'-'A']-=2;
					for(int i = 0; i < 26; i++)
 				if(table[i] < 0)
 					cout << 3 <<endl;
		if(dp())
			return true;
		else
		{
			table['T'-'A']++; table['H'-'A']++; table['R'-'A']++; table['E'-'A']+=2;
			res.pop_back();
		}
	}

		if ( table['F'-'A']>0 && table['O'-'A']>0 && table['U'-'A']>0 && table['R'-'A']>0 )
	{
		res.push_back(4);
		table['F'-'A']--; table['O'-'A']--; table['U'-'A']--; table['R'-'A']--;
					for(int i = 0; i < 26; i++)
 				if(table[i] < 0)
 					cout << 4 <<endl;
		if(dp())
			return true;
		else
		{
			table['F'-'A']++; table['O'-'A']++; table['U'-'A']++; table['R'-'A']++;
			res.pop_back();
		}
	}

		if (table['F'-'A']>0  && table['I'-'A']>0 && table['V'-'A']>0 && table['E'-'A']>0 )
	{
		res.push_back(5);
		table['F'-'A']--; table['I'-'A']--; table['V'-'A']--; table['E'-'A']--;
					for(int i = 0; i < 26; i++)
 				if(table[i] < 0)
 					cout << 5 <<" " <<char(i+'A')<< endl;
		if(dp())
			return true;
		else
		{
			table['F'-'A']++; table['I'-'A']++; table['V'-'A']++; table['E'-'A']++;
			res.pop_back();
		}
	}

		if ( table['S'-'A'] > 0 && table['X'-'A']>0  && table['I'-'A'] > 0)
	{
		res.push_back(6);
		table['S'-'A']--;table['I'-'A']--;table['X'-'A']--;
					for(int i = 0; i < 26; i++)
 				if(table[i] < 0)
 					cout << 6 << " " << char(i +'A') << endl;
		if(dp())
			return true;
		else
		{
		 table['S'-'A']++;table['I'-'A']++;table['X'-'A']++;
			res.pop_back();
		}
	}

		if (table['S'-'A']>0  && table['E'-'A'] >= 2 && table['V'-'A']>0 && table['N'-'A']>0 )
	{
		res.push_back(7);
		table['S'-'A']--; table['E'-'A']-=2;table['V'-'A']--;table['N'-'A']--;
					for(int i = 0; i < 26; i++)
 				if(table[i] < 0)
 					cout << 7 <<endl;
		if(dp())
			return true;
		else
		{
			table['S'-'A']++; table['E'-'A']+=2;table['V'-'A']++;table['N'-'A']++;
			res.pop_back();
		}
	}

		if (table['E'-'A']>0  && table['I'-'A']>0 && table['G'-'A']>0 && table['H'-'A']>0 && table['T'-'A']>0 )
	{
		res.push_back(8);
		table['E'-'A']--; table['I'-'A']--;table['G'-'A']--;table['H'-'A']--; table['T'-'A']--;
					for(int i = 0; i < 26; i++)
 				if(table[i] < 0)
 					cout << 8 <<endl;
		if(dp())
			return true;
		else
		{
		table['E'-'A']++; table['I'-'A']++;table['G'-'A']++;table['H'-'A']++; table['T'-'A']++;
			res.pop_back();
		}
	}

		if (table['N'-'A'] >= 2  && table['I'-'A']>0 &&table['E'-'A']>0 )
	{
		res.push_back(9);
		table['N'-'A'] -=2; table['I'-'A']--; table['E'-'A']--;
					for(int i = 0; i < 26; i++)
 				if(table[i] < 0)
 					cout << 9 <<endl;
		if(dp())
			return true; 
		else
		{
			table['N'-'A'] +=2; table['I'-'A']++; table['E'-'A']++;
			res.pop_back();
		}

	}

	return false;


}
int main()
{
 
 int T;
 cin >> T;
 for(int t = 1; t <= T; t++ )
 {
 	cout << "Case #"<<t<<": ";
 	memset(table, 0, sizeof(table));
 	res.clear();
 	string s;
 	cin >> s;
 	for(int i = 0; i < s.length(); i++)
 		table[s[i]-'A']++;
 	if( dp() )
 	{
 		sort(res.begin(), res.end());
 		for(int i = 0; i < res.size(); i++)
 			cout << res[i];
 		cout << endl;
 	}




 } 

  return 0;
}