#include <iostream>
#include <string>
#include <cstring>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <climits>
#include <cctype>
#include <cmath>
#include <sstream>
#include <cstdlib>
#include <climits>
#include <ctime>
#include <set>
#include <map>
#include <numeric>
#include <utility>
#include <deque>
#include <queue>
#include <stack>
#include <iomanip>
#include <complex>
#include <list>
#include <bitset>
#include <fstream>
#include <limits>
#include <memory.h>
#include<windows.h>
#include<iterator>
//#include<bits/stdc++.h>

using namespace std;

#define loop(i,j,n) for(int i=(j); i<(n);i++)
#define ll long long
#define all(x) x.begin(),x.end()
#define SZ(x) ((int)((x).size()))
#define PB push_back
#define VI vector<int>
#define LLVI vector<long long int>
#define VS vector<string>
#define READ(s) freopen(s, "r", stdin)
#define WRITE(s) freopen(s, "w", stdout)

int main() {
	READ("A-small-attempt2.in");
	WRITE("A-small-attempt2.out");
	int m[4][4];
	int v[16];
	int n,l;
	int c = 1;
	vector<int> card;
 
	cin >> n;
	while (n--)
		{
 /*
			for(int i = 0; i < 16; i++)
				v[i] = 0;
 */
 			fill_n(v,16,0);
			for(int k = 0; k < 2; k++)
				{
					cin >> l;
					for(int i = 0; i < 4; i++)
						for(int j = 0; j < 4; j++)
							cin >> m[i][j];
						for(int i = 0; i < 4; i++)
							{
								v[m[l-1][i]-1] += 1;
							}
				}
 
			for(int i = 0; i < 16; i++)
				{
					/*cout << "i = " << i << endl;
					cout << "v[i] = " << v[i] << endl;*/
					if(v[i] == 2)
					card.push_back(i+1);
				}
			if (card.size() == 1)
				cout << "Case #" << c <<": " << card[0] << endl;
			else if (card.size() > 1)
				cout << "Case #" << c <<": Bad magician!" << endl;
			else
				cout << "Case #" << c <<": Volunteer cheated!" << endl;
			c++;
			card.clear();
}
 
}
