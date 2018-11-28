#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>
using namespace std;
typedef long long LL;

int main() {
	FILE *fin = freopen("B-large.in", "r", stdin);
	assert( fin!=NULL );
	FILE *fout = freopen("B-large.out", "w", stdout);
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++){
		//int n;
		string stuff;
		cin >> stuff;
		bool plus_hit = false;
		int flips = 0;
		if (stuff[0] == '-')
		{
			flips = 1;
		} else
		{
			plus_hit = true;
		}
		for (int i = 1; i < stuff.length(); i++)
		{
			if (stuff[i] == '+')
			{
				plus_hit = true;
			}
			else if (stuff[i] == '-' && plus_hit)
			{
				plus_hit = false;
				flips += 2;
			}
		}

		cout << "Case #" << t << ": ";
		cout << flips << endl;
		
	}
	return 0;
}