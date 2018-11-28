#include <stdio.h> 
#include <stdlib.h>
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

int card1[4],card2[4];

int main(){
	ifstream ifs( "A-small-attempt0.in" );
	ofstream ofs( "test.txt" );
	int T;
	ifs>>T;
	vector<string>answer(T);
	REP(i,T){
		int ans1,ans2;
		ifs>>ans1;
		REP(j,4)REP(k,4){
			int t;
			ifs>>t;
			if(j==ans1-1)card1[k]=t;
		}
		ifs>>ans2;
		REP(j,4)REP(k,4){
			int t;
			ifs>>t;
			if(j==ans2-1)card2[k]=t;
		}
		int c=0,tt;
		REP(j,4)REP(k,4){
			if(card1[j]==card2[k]){
				tt=card1[j];
				c++;
			}
		}
		if(c==0){
			answer[i]="Volunteer cheated!";
		}else if(c==1){
			answer[i]=toString(tt);
		}else{
			answer[i]="Bad magician!";
		}
	}
	
	REP(i,T){
		ofs<<"Case #"<<i+1<<": "<<answer[i]<<endl;
	}
	return 0;
}
