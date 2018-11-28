#include <stdio.h> 
#include <stdlib.h>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <fstream>


using namespace std;
#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define CLR(a) memset((a), 0 ,sizeof(a))
#define REP(i,n) for(int i = 0; i < (int)(n); ++i)
#define ALL(a)  (a).begin(),(a).end()
#define RALL(a) (a).rbegin(), (a).rend()
#define PB push_back
#define MP make_pair
#define SZ(a) int((a).size())
#define EACH(i,c) for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); ++i)
#define EXIST(s,e) ((s).find(e)!=(s).end())
#define SORT(c) sort((c).begin(),(c).end())

//conversion
//------------------------------------------
inline int toInt(string s) {int v; istringstream sin(s);sin>>v;return v;}
template<class T> inline string toString(T x) {ostringstream sout;sout<<x;return sout.str();}

//typedef
//------------------------------------------
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int, int> PII;

//debug
#define dump(x)  cerr << #x << " = " << (x) << endl;
#define debug(x) cerr << #x << " = " << (x) << " (L" << __LINE__ << ")" << " " << __FILE__ << endl;



int main(){
	ifstream ifs( "B-large.in" );
	ofstream ofs( "test2.txt" );
	int T;
	ifs>>T;
	
	int answer[120];
	
	//REP(i,1000)tt[i]=i;
	
	REP(i,T){
		vector<int>Q;
		int D;ifs>>D;
		int maxP=0;
		REP(j,D){
			int P;ifs>>P;
			Q.PB(P);
			maxP=max(maxP,P);
		}
		SORT(Q);
		int res=maxP;
		FOR(j,1,maxP+1){
			int tmp=j;
			REP(jj,SZ(Q)){
				if(Q[jj]>j)tmp+=(Q[jj]/j+(Q[jj]%j!=0))-1;
			}
			res=min(res,tmp);
		}
		answer[i]=res;
	}
	REP(i,T){
		cout<<answer[i]<<endl;
		ofs<<"Case #"<<i+1<<": "<<answer[i]<<endl;
	}
	return 0;
}
