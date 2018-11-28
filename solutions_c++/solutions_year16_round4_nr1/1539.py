// {{{ Boilerplate Code <--------------------------------------------------
// vim:filetype=cpp:foldmethod=marker:foldmarker={{{,}}}

#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>

#define FOR(I,A,B) for(int I = (A); I < (B); ++I)
#define ALL(A)     (A).begin(), (A).end()

using namespace std;

// }}}

string extract(string in, int remain){
	string out;
	FOR(i,0,in.length()){
		if (in[i]=='P'){
			out += "PR";
		} else if (in[i]=='S') {
			if (remain<=2) {
				out += "PS";
			}else{
				out += "SP";
			}
		} else if (in[i]=='R') {
			if (remain==1) {
				out+="RS";
			}else{
				out+="SR";
			}
		}
	}

	if (remain==1)
		return out;

	return extract(out, remain-1);
}

int main(){
	int T;
	cin>>T;

	FOR(iter,0,T){
		cout<<"Case #"<<(iter+1)<<": ";

		string ret="IMPOSSIBLE";
		
		int N,P,R,S;
		cin>>N>>R>>P>>S;

		string tmp;
		int handct[128];

		tmp=extract("P",N);
		handct['P']=0;
		handct['S']=0;
		handct['R']=0;
		FOR(i,0,tmp.length()){
			handct[tmp[i]]++;
		}
		if(P==handct['P'] && S==handct['S'] && R==handct['R']){
			if(ret=="IMPOSSIBLE" || tmp<ret){
				ret=tmp;
			}
		}


		tmp=extract("R",N);
		handct['P']=0;
		handct['S']=0;
		handct['R']=0;
		FOR(i,0,tmp.length()){
			handct[tmp[i]]++;
		}
		if(P==handct['P'] && S==handct['S'] && R==handct['R']){
			if(ret=="IMPOSSIBLE" || tmp<ret){
				ret=tmp;
			}
		}


		tmp=extract("S",N);
		handct['P']=0;
		handct['S']=0;
		handct['R']=0;
		FOR(i,0,tmp.length()){
			handct[tmp[i]]++;
		}
		if(P==handct['P'] && S==handct['S'] && R==handct['R']){
			if(ret=="IMPOSSIBLE" || tmp<ret){
				ret=tmp;
			}
		}

		cout<<ret<<endl;
	}
}
