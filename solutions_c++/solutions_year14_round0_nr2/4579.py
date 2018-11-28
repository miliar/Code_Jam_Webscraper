#include <vector>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <deque>
#include <algorithm>
#include <utility>
#include <functional>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <climits>
#include <cassert>
#include <memory>
#include <time.h>
using namespace std;
inline int toInt(string s) {int v; istringstream sin(s);sin>>v;return v;}
template<class T> inline string toString(T x) {ostringstream sout;sout<<x;return sout.str();}
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef pair<int, int> pii;
typedef long long ll;
#define ALL(a) (a).begin(),(a).end()
#define RALL(a) (a).rbegin(),(a).rend()
#define EXIST(s,e) ((s).find(e)!=(s).end())
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
const double EPS = 1e-9;
const double PI  = acos(-1.0);

bool shouldBuy(double curRate,double curCookie,double X,double C,double F){
	double T=(X-curCookie)/curRate;
	double cookieWithCurRate = curRate*T;
	double cookieWithExpectedRate = -C+(curRate+F)*T;
	return cookieWithCurRate < cookieWithExpectedRate;
}

double getNextEvent(double curRate,double curCookie,double targetCookie){
	return (targetCookie-curCookie)/curRate;
}

int main(){
	cout.precision(32);

	int numTests;
	cin>>numTests;
	REP(test,numTests){
		double C,F,X;
		cin>>C>>F>>X;

		cout<<"Case #"<<test+1<<": ";
		double rate=2,cookie=0,time=0;
		while(true){
			double nextFactoryEvent=getNextEvent(rate,cookie,C);
			double goalEvent=getNextEvent(rate,cookie,X);
			if(goalEvent<nextFactoryEvent){
				time+=goalEvent;
				break;
			}else{
				time+=nextFactoryEvent;
				cookie+=nextFactoryEvent*rate;
				if(shouldBuy(rate,cookie,X,C,F)){
					rate+=F;
					cookie-=C;
				}else{
					time+=getNextEvent(rate,cookie,X);
					break;
				}
			}
		}
		
		cout<<time<<endl;
	}
}