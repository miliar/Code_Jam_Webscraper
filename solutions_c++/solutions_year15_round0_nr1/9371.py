#include <iostream>
#include <fstream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <iomanip>
#include <algorithm>
#include <queue>
#include <fstream>

using namespace std;

#define ll long long
#define INF 1000000000


int main(void) 
{
	

	ifstream cin ("A-large (1).in");
	ofstream cout ("out.txt");

	int t;
	cin >> t;
	
	for (int i = 0; i < t; i++)
	{
		int n;
		cin >> n;
		
		string s;
		cin >> s;
		
		int kiek = 0;
		int ats = 0;
		
		for (int j = 0; j < s.size(); j++)
		{
			if (kiek < j)
			{
				ats += j - kiek;
				kiek = j;
			}
			
			kiek += int(s[j] - '0');
		}
		
		cout << "Case #" << i+1 << ": " << ats << endl;
	}
	//while (true) {}
}

