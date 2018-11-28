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

int main(){
	int t;
	cin>>t;
	REP(test,t){
		int fr;
		cin>>fr,fr--;
		vvi fc(4,vi(4));
		REP(i,4){
			REP(j,4){
				cin>>fc[i][j];
			}
		}
		vi fp;
		REP(i,4){
			fp.push_back(fc[fr][i]);
		}

		int sr;
		cin>>sr,sr--;
		vvi sc(4,vi(4));
		REP(i,4){
			REP(j,4){
				cin>>sc[i][j];
			}
		}
		vi sp;
		REP(i,4){
			sp.push_back(sc[sr][i]);
		}

		sort(ALL(fp));
		sort(ALL(sp));
		vi intersection(4);
		vi::iterator it=set_intersection(ALL(fp),ALL(sp),intersection.begin());
		intersection.resize(it-intersection.begin());
		cout<<"Case #"<<test+1<<": ";
		if(intersection.size()==0){
			cout<<"Volunteer cheated!"<<endl;
		}else if(intersection.size()>1){
			cout<<"Bad magician!"<<endl;
		}else{
			const int v=intersection[0];
			cout<<v<<endl;
		}
	}
}