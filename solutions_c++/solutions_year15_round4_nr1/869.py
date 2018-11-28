#ifdef __GNUC__
#include <ext/hash_map>
#include <ext/hash_set>
#else
#include <hash_map>
#include <hash_set>
#endif

namespace std
{
 using namespace __gnu_cxx;
}

#include <fstream>
#include <vector>
#include <string>
#include <iostream>
#include <set>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <algorithm>
#include <math.h>
#include <cstdlib>
#include <climits>
#include <iomanip> 
using namespace std;

typedef long long LL;
typedef long double LD;
template<class T>

T prime(T a , T b)
{
	cout << a << "\t"<<b << endl;
	if ( a >= b)
		return (prime(b , a));
	if(a == 0)
		return b;
	return prime(a , b%a);
}

string its(int n)
{
	string ret;
	if(n == 0)
	{
		ret = "0";
		return ret;
	}
	while(n > 0)
	{
		ret += (n % 10 + '0');
		n /= 10;
	}
	reverse(ret.begin() , ret.end());
	return ret;
}

bool checkDir(vector<vector<char > > &dir, int ro, int co, char d ) {
	int row = dir.size();
	int col = dir[0].size();
	if (d == '^') {
		for (int r = ro - 1 ; r >=0; r --) {
			if (dir[r][co] !='.')
				return true;
		}
		return false;
	}
	if (d == 'v') {
		for (int r = ro + 1 ; r < row; r ++) {
			if (dir[r][co] !='.')
				return true;
		}
		return false;
	}
	if (d == '<') {
		for (int c = co - 1 ; c >=0; c --) {
			if (dir[ro][c] !='.')
				return true;
		}
		return false;

	}
	if (d == '>') {
		for (int c = co + 1 ; c <col; c ++) {
			if (dir[ro][c] !='.')
				return true;
		}
		return false;

	}
}

int main()
{
//==============in put=================
	ifstream curFile("A-large.in");
	vector<string> result;
	int T; // testcases count
    int row;
    int col;
	if(curFile.is_open())
	{
		curFile >> T;
		vector  <char> dirs;
        dirs.push_back('^');
        dirs.push_back('<');
 		dirs.push_back('>');
		dirs.push_back('v');
		for(int C = 0 ; C < T ; C++)
		{
//==============solution==================
			cout << "Enter Test case:" << C + 1 << endl;
			curFile >> row;
			curFile >> col;
			vector<vector<char> > dir (row, vector<char> (col, ' '));
			for (int r = 0 ; r < row ; r ++) {
				for (int c = 0 ; c < col ; c ++) {
					curFile >> dir[r][c];
				}
			}
			string R;
			int re = 0;
			for (int r = 0 ; r < row ; r ++) {
				for (int c = 0 ; c < col ; c ++) {
					bool find = 0;
					if (dir[r][c] == '.')
						continue;
					else if (checkDir(dir,r,c,dir[r][c])) {
						continue;
					}
					else {
						for (int i = 0 ; i < 4 ; i++) {
							if(checkDir(dir,r,c,dirs[i]))
							{
								re += 1;
								find = 1; break;
							}
						}
					}
					if (!find) 
							R = "IMPOSSIBLE";
				}
			}
			if (R.size() < 1)
				R = its(re);
			result.push_back(R);
//==============solution end==============
		}	
	}
	curFile.close();
//==============out put==================
	ofstream outfile;
	outfile.open("result.txt");
	if(outfile.is_open())
	{
//		outFile << setprecision(6);
		for(int i = 0; i < result.size() ; i++) {
			outfile << "Case #" << i + 1<< ": " <<result[i] << endl;
			cout << "Case #" << i + 1<< ": " <<result[i] << endl;
		}
	}
	outfile.close();
	return 0;
}
