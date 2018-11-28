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

int M[10001];
long answer[101][2];
int main(){
	ifstream ifs("A-large.in");
	ofstream ofs("test.txt");
	int T,N;
	ifs>>T;
	
	long res1=0;
	REP(tt,T){
		ifs>>N;
		long res1=0,res2=0,nw=0,mnw=0;
		REP(i,N){
			ifs>>M[i];
			if(M[i]<nw){
				res1+=nw-M[i];
				mnw=max(nw-M[i],mnw);
			}
			nw=M[i];
			
		}
		REP(i,N-1){
			res2+=min(mnw,(long)M[i]);
		}
		answer[tt][0]=res1;
		answer[tt][1]=res2;
	}
	
	
	REP(tt,T){
		cout<<answer[tt][0]<<" "<<answer[tt][1]<<endl;
		ofs<<"Case #"<<tt+1<<": "<<answer[tt][0]<<" "<<answer[tt][1]<<endl;
	}
	return 0;
}