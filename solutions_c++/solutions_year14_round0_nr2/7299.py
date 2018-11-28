#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <vector>
#include <list>
#include <map>
#include <set>
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

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(int)(b);i++)
#define REP(i,a) for(int i=0;i<(int)(a);i++)
#define ALL(i) i.begin(),i.end()
#define rALL(i) i.rbegin(),i.rend()
#define PB push_back

typedef vector<int> vi;
typedef vector<vector<int> > vvi;

template<class T> string i2a(T x) {ostringstream oss; oss<<x; return oss.str();}

void printvec(vector<int> a)
{
 cout<<"Vecteur:  ";
 REP(i,a.size()) cout<<a[i]<<"  ";
 cout<<endl;
}

int main()
{

   freopen("B-large.in", "r", stdin);
   freopen("B-large.out", "w", stdout);

	int cases;
	cin>>cases;
	REP(k, cases) {
		cout<<"Case #"<<k+1<<": ";
		double c,f,x;
		cin>>c>>f>>x;
		if(x <= c) {
			cout<<x/2<<endl;
			continue;
		}
		double step = 2;
		double secs = 0.0;
		int cur = 0;
		while(true) {
			secs += c/step;
			cur = c;
			double buy = x/(step+f), nbuy = (x - c)/step;
		//	cout<<"sec, buy, nbuy="<<secs<<" "<<buy<<" "<<nbuy<<endl;
			if(buy < nbuy) {
				cur = 0;
				step += f;
			} else {
				secs += nbuy;
				break;
			}
		}
		cout<<std::setprecision(7)<<secs<<std::fixed<<endl;
	}
    return 0;
}
