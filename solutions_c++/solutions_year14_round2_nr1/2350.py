#include <iostream>
#include <fstream>
//#include <stdint.h>
#include <string>
#include <cmath>
#include <climits>
#include <cstdio>
#include <algorithm>
#include <list>

using namespace std;

vector<string> ss;
int idx[102] = {0};
int ccounts[102] = {0};

int main(int argc, char* argv[])
{
	if(argc < 3)
	{
		cout << "No input/output file passed as argument\n";
	}
	
	freopen(argv[1], "r", stdin);
	freopen(argv[2], "w", stdout);
	
	int t, n;
	bool lose;
	string str;
	cin >> t;
	for (int ti = 1; ti <= t; ti++)
	{
		cin >> n;
		for(int ni = 0; ni < n; ni++)
		{
			cin >> str;
			ss.push_back(str);
		}
		for(int i = 0; i < n; i++)
		{
			ccounts[i] = 0;
			idx[i] = 0;
		}
		int i = 0;
		int sum = 0;
		char tmp;
		lose = false;
		while(i < str.length() && !lose)
		{
			tmp = str[i];
			int ssit = 0, tmpssit, tmpIdx;
			for(auto it = ss.begin(); it != ss.end() && !lose; it++)
			{
				tmpIdx = idx[ssit];
				// tmpssit = ssit;
				while(idx[ssit] < (*it).length() && (*it)[idx[ssit]] == tmp)
				{
					idx[ssit]++;
				}
				if(tmpIdx == idx[ssit])
				{
					lose = true;
				}
				else
				{
					ccounts[ssit] = idx[ssit] - tmpIdx;
				}
				ssit++;
			}
			
			int localsum = 0;
			for(int j = 0; j < n; j++)
			{
				localsum += ccounts[j];
			}
			int mid = round((1.0 * localsum)/n);
			localsum = 0;
			for(int j = 0; j < n; j++)
			{
				localsum += abs(ccounts[j] - mid);
			}
			sum += localsum;
			while(i < str.length() && str[i] == tmp)
			{
				i++;
			}
			if(i == str.length())
			{
				ssit = 0;
				for(auto it = ss.begin(); it != ss.end() && !lose; it++)
				{
					tmpIdx = idx[ssit];
					while(idx[ssit] < (*it).length() && (*it)[idx[ssit]] == tmp)
					{
						idx[ssit]++;
					}
					if(idx[ssit] != (*it).length())
					{
						lose = true;
					}
					ssit++;
				}
			}
			
		}
		cout << "Case #" << ti << ": ";
		if(lose)
			cout << "Fegla Won\n";
		else
			cout << sum << "\n";
		ss.clear();
	}
	
	return 0;
}