#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <iterator>
#include <iostream>
#include <functional>
#include <sstream>
#include <numeric>
#include <list>
#include <map>

using namespace std;

bool isPalin(int n)
{
	string r;
	ostringstream c;
	c<<n;
	r=c.str();
	int sz=r.size()-1;
	for (int i=0;i<r.size();i++)
	{
		if ( r[i] != r[sz-i] )
			return false;
	}
	return true;
}

int main()
{
	set<int> s;
	for (int i=1;i<33;i++)
	{
		if ( isPalin(i) && isPalin(i*i) )
			s.insert(i*i);
	}

	FILE *in=fopen("S:/input.in.txt","r");
    FILE *out=fopen("S:/output.txt","w");
	int T = 0;
    fscanf(in,"%d",&T); 
	
    for (int ii=0;ii < T ;ii++)
    {
		int A = 0;
		int B = 0;
		int cnt=0;
		fscanf(in,"%d %d",&A, &B);
		vector<string> v;
		for (int i=A;i<=B; i++)
		{
			if ( s.find(i) != s.end() ) cnt++;
		}
		fprintf(out,"Case #%d: %d\n",ii+1,cnt);
	}
	return 0;
}