#include <vector>
#include <iostream>
#include <sstream>
#include <math.h>
#include <sys/time.h>
#include <cstdlib>
#include <algorithm>
#include <cassert>
#include <cstring>
#include <fstream>

#define FOR(i,a,b)  for(__typeof(b) i=(a);i<(b);++i)
#define REP(i,a)    FOR(i,0,a)
#define FOREACH(x,c)   for(__typeof(c.begin()) x=c.begin();x != c.end(); x++)
#define ALL(c)      c.begin(),c.end()
#define CLEAR(c)    memset(c,0,sizeof(c))
#define SIZE(c) (int) ((c).size())

#define PB          push_back
#define MP          make_pair
#define X           first
#define Y           second

#define ULL         unsigned long long
#define LL          long long
#define LD          long double
#define II         pair<int, int>
#define DD         pair<double, double>

#define VI          vector<int>
#define VVI         vector<VI >
#define VD                      vector<double>
#define VS          vector<string >
#define VII        vector<II >
#define VDD         vector< DD >

#define DUMP(a)       cerr << #a << ": " << a << endl;
using namespace std;

int tests;
int n;
int m;
LL original;
LL result;
VII e, o;
#define N 1000002013LL

void read_test(){
	cin >> n >> m;
	e.resize(m); o.resize(m);
	original = 0;
	REP(i,m){
		int oo, ee, pp;
		cin >> oo >> ee >> pp;
		e[i] = MP(ee,pp);
		o[i] = MP(oo,pp);
		LL tmp = ee-oo;
		tmp = ((tmp*(2*n-tmp+1))/2) % N;
		tmp = (pp*tmp) % N;
		original = (original+tmp)%N;
	}
}

void solve_test(){
	sort(ALL(e));
	sort(ALL(o));
	o.PB(MP(n+1,1));
	result = 0;
	REP(i,m){
		int j = 0;
		while (o[j].X <= e[i].X)
			j++;
		j--;
		do{
			int s = min(o[j].Y, e[i].Y);
			o[j].Y -= s;
			e[i].Y -= s;
			LL tmp = (e[i].X-o[j].X);
			tmp = (tmp*(2*n-tmp+1)/2) % N;
			tmp = (tmp*s) % N;
			result = (result + tmp) % N;
			if (o[j].Y == 0){
				o.erase(o.begin()+j);				
				j--;
			}
		} while (e[i].Y != 0);
	}
	result = (N+original - result) % N;
}

void dump_sol(int i){
	cout << "Case #" << i << ": ";
	cout << result << endl;
    cout.flush();
}

int main(int argc, char *argv[]){
	cin >> tests;
	for(int i=0; i < tests; i++){
		read_test();
    		solve_test();
	    	dump_sol(i+1);
	}
}
