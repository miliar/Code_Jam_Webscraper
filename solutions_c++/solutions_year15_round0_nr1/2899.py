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



int main(){
	ifstream ifs( "A-large.in" );
	ofstream ofs( "test.txt" );
	int T;
	ifs>>T;
	
	long answer[120];
	
	//REP(i,1000)tt[i]=i;
	REP(i,T){
		int num,res=0;
		string str;
		ifs>>num>>str;
		int sum=(int)(str[0]-'0');
		
		REP(j,num){
			int tmp=(int)(str[j+1]-'0');
			if(tmp!=0){
				res+=max((j+1-sum),0);
				sum=max(sum,j+1);
				sum+=tmp;
			}
		}
		answer[i]=res;
	}
	REP(i,T){
		cout<<answer[i]<<endl;
		ofs<<"Case #"<<i+1<<": "<<answer[i]<<endl;
	}
	return 0;
}
