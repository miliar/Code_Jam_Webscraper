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

typedef vector<double> vd;

int choose_move(double naomi_told,vd &ken,vi &ken_used){
	int ken_move=-1;
	REP(j,ken.size()){
		if(!ken_used[j]&&ken[j]>naomi_told){
			ken_move=j;
			break;
		}
	}
	if(ken_move==-1){
		REP(j,ken.size()){
			if(!ken_used[j]){
				ken_move=j;
				break;
			}
		}
	}
	return ken_move;
}

int play_war(vd &naomi,vd &ken,vi &naomi_used,vi &ken_used){
	int ret=0;
	REP(i,naomi.size()){
		if(!naomi_used[i]){
			int ken_move=choose_move(naomi[i],ken,ken_used);
			int score=ken[ken_move]<naomi[i];
			vi new_naomi_used(naomi_used);
			new_naomi_used[i]=1;
			vi new_ken_used(ken_used);
			new_ken_used[ken_move]=1;
			ret=max(ret,play_war(naomi,ken,new_naomi_used,new_ken_used)+score);
		}
	}
	return ret;
}


int play_d_war(vd &naomi,vd &ken,vi &naomi_used,vi &ken_used){
	int ret=0;
	REP(i,ken.size()){
		if(!ken_used[i]){
			int ken_move=i;
			int naomi_move=choose_move(ken[ken_move],naomi,naomi_used);
			int score=ken[ken_move]<naomi[naomi_move];
			vi new_naomi_used(naomi_used);
			new_naomi_used[naomi_move]=1;
			vi new_ken_used(ken_used);
			new_ken_used[ken_move]=1;
			ret=max(ret,play_d_war(naomi,ken,new_naomi_used,new_ken_used)+score);
		}
	}
	return ret;
}


int main(){
	int numTests;
	cin>>numTests;
	REP(test,numTests){
		int n;
		cin>>n;
		vd naomi(n),ken(n);
		REP(i,n){
			cin>>naomi[i];
		}
		REP(i,n){
			cin>>ken[i];
		}
		cout<<"Case #"<<test+1<<": ";

		sort(ALL(naomi));
		sort(ALL(ken));

		int war_score;
		{
			vi naomi_used(n);
			vi ken_used(n);
			war_score=play_war(naomi,ken,naomi_used,ken_used);
		}
		int d_war_score;
		{
			vi naomi_used(n);
			vi ken_used(n);
			d_war_score=play_d_war(naomi,ken,naomi_used,ken_used);
		}
		cout<<d_war_score<<" "<<war_score<<endl;
	}
}