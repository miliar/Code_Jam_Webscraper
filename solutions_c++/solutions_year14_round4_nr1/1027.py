#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <string>
#include <algorithm>
#include <math.h>
using namespace std;
const long long int modl=1000000007;
ifstream in("in.txt");
ofstream out("out.txt");
int main()
{
	int t,n,x,s[10000],g,p,q;
	in >> t;
	for(int i=1;i<=t;i++)
	{
		in >> n >> x;
		for (int j=0;j<n;j++) in >> s[j];
		sort(s,s+n);
		g=0;
		p=0;
		q=n-1;
		while (p<q)
		{
			if (s[p]+s[q]<=x)
			{
				g++;
				p++;
				q--;
			}
			else
			{
				g++;
				q--;
			}
		}
		if (p==q) g++;
		out << "Case #" << i << ": " << g << "\n";
	}
	return 0;
}
