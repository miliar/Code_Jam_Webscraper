#include <string>
#include <map>
#include <math.h>
#include <sstream>
#include <time.h>
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
#include <fstream>

using namespace std;

#define fx first
#define sx second

typedef pair<int,int> ii;
typedef vector<int> vec;
typedef vector<ii> vecp;
typedef long long int lli;
typedef unsigned long long int ulli;

int func(string str)
{
	int res = 0;
	int cur = 0;
	for (int i = 0; i < str.length(); ++i)
	{
		int q = str[i]-'0';
		if(q>1) cur+=q-1;
		if(q==0)
		{
			if(cur>0) --cur;
			else ++res;
		}
	}
	return res;
}

int main()
{
	ifstream input;
	input.open("A-large.in",ios::in);
	ofstream out;
	out.open("a.out",ios::out);

	int count;
	input>>count;

	for(int i=1; i<=count; ++i)
	{
		//getting the input
		int smax;
		string data;
		input>>smax>>data;

		//printing the output
		out<<"Case #"<<i<<": ";
		out<<func(data);
		

		if(i<count) out<<endl;
	}	

	return 0;
}
