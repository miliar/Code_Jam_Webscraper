#include <cstdio>
#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <string>
#include <functional>
#include <algorithm>
#include <cmath>
using namespace std;

int t, n, x, cnt, mi;

int main()
{
	ifstream infile("B-large.in");
	//ifstream infile("B-small-attempt1.in");
	//ifstream infile("in.txt");
    ofstream outfile;
    outfile.open("out.txt");
	infile >> t;
	for (int i = 1; i <= t; i++)
	{
		infile >> n;
		vector<int> diners (n);
		for (int j = 0; j < n; j++)
		{
			infile >> x;
			diners.push_back(x-1);
		}
		sort(diners.begin(), diners.end(), greater<int>());
		mi = diners[0]+1;
		for (int div = 1; div <= diners[0]; div++)
		{
			cnt=div;
			for (int k = 0; k < n; k++)
			{
				cnt+=(diners[k])/div;
				if(cnt>=mi) break;
			}
			mi = min(mi, cnt);
		}
		outfile << "Case #" << i << ": " << mi << endl;
	}
}