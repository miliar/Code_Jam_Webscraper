// {{{ Boilerplate Code <--------------------------------------------------
//
// vim:filetype=cpp foldmethod=marker foldmarker={{{,}}}

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

#define FOR(I,A,B)	for(int I = (A); I < (B); ++I)
#define REP(I,N)	FOR(I,0,N)
#define ALL(A)		(A).begin(), (A).end()

using namespace std;

// }}}

int main(){
	int T;
	cin>>T;

	FOR(count,0,T){
		cout<<"Case #"<<(count+1)<<": ";

		int N;
		long long  P;

		cin>>N>>P;
		
		P--;

		int win=0;
		int lose=(1LL<<N)-1;
		
		long long current=0;

		FOR(i,0,N){
			current+=(1LL<<(N-i-1));
			if(P>=current)
				win=i+1;
		}
		
		FOR(i,0,N+1){
			lose=i;
			if(((1LL<<(N-i))-1)<=P)
				break;

		}
		win=(win!=N)?((1LL<<(win+1))-2):((1LL<<N)-1);
		cout<<win<<" "<<((1LL<<N)-(1<<lose))<<"\n";

	}
}
