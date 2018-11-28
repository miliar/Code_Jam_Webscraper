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
const double EPS = 1e-10;
const double PI  = acos(-1.0);

const int MAX=10;
int main(){
	int num_tests;
	cin>>num_tests;
	const ll MAX_PPL=pow(2,MAX);
	vi possible_losts(MAX_PPL);
	int cnt=1;
	int num=1;
	for(int i=0;i<MAX_PPL;){
		REP(j,num){
			possible_losts[i]=cnt-1;
			if(++i>=MAX_PPL)break;
		}
		cnt++;
		num*=2;
	}
	REP(test,num_tests){
		cout<<"Case #"<<test+1<<": ";
		int n,p;
		cin>>n>>p;
		const int ppl=pow(2,n);
		int must_person=0;
		int possible_person=0;
		REP(i,ppl){
			{
				int rank=ppl;
				REP(j,possible_losts[i]){
					rank/=2;
				}
				if(ppl-rank+1<=p){
					must_person=max(must_person,i);
				}
			}
			{
				int rank=ppl;
				REP(j,possible_losts[ppl-i-1]){
					rank/=2;
				}
				if(rank<=p){
					possible_person=max(possible_person,i);
				}
			}
		}
		cout<<must_person<<" "<<possible_person<<endl;
	}
}