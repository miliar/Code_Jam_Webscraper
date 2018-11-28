#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <set>
#include <map>
#include <sstream>
#include <queue>
#include <stack>
#include <math.h>
#include <utility>
#include <iterator>
#include <fstream>
#include <stdio.h>
#include <cstring>

using namespace std;

template<class T>
string tostring(T a){stringstream ss; ss<<a; return ss.str();}

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int,int> II;
typedef long long LL;
#define SZ(a) int((a).size()) 
#define PB push_back 
#define ALL(c) (c).begin(),(c).end() 
#define FOR(i,n) for(int (i)=0;(i)<(int)(n);(i)++)
#define LOOP(i,a,b) for((i)=(a);(i)<(b);(i)++)
#define MP(a,b) make_pair((a),(b))
#define LAST(t) (t[SZ(t)-1])


int main(){
	ifstream be("B-large.in");
	ofstream ki("ki.txt");
	int T; be>>T;
	FOR(tt,T){
		int n,m; be>>n>>m;
		vector<vector<int> > f(n,vector<int>(m));
		FOR(i,n)
			FOR(j,m)
				be>>f[i][j];

		bool ok=true;
		FOR(i,n)
			FOR(j,m){
				int b=f[i][j];
				bool ok1=true;
				FOR(k,n)
					if(f[k][j]>b)
						ok1=false;
				bool ok2=true;
				FOR(k,m)
					if(f[i][k]>b)
						ok2=false;
				if(!ok1 && !ok2)
					ok=false;
			}

		ki<<"Case #"<<tt+1<<": "<<(ok?"YES":"NO")<<endl;
		
	}

	ki.close();
	return 0;
}