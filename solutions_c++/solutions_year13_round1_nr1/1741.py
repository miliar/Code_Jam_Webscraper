#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <cmath>
#include <fstream>
#include <time.h>
#include <sstream>
#include <stdio.h>
#include <cstring>
#include <queue>
#include <deque>
using namespace std;

#define ll long long
#define ul unsigned long long
#define pii pair<int,int>
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define REP(i, n) for (int (i) = 0; (i) < (n); (i) ++)

int main()
{
	ifstream in("2.in");
	ofstream out("output.txt");

	ul k, r, t;
	in>>k;
	REP(i, k)
	{
		in>>r>>t;
		ul rez = 0;
		ul q = r+1;
		ul sum = q*q - r*r;
		//cout<<"sum="<<sum<<"  "<<r<<"   "<<t<<"\n";
		while (sum <= t)
		{
			q+=2;
			sum += q*q;
			sum -= (q-1)*(q-1);
			rez++;
		}
		out<<"Case #"<<i+1<<": "<<rez<<"\n"; 
	}
	in.close();
	out.close();
	return 0;
}