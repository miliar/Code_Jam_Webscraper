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

int main(){
	int T;
	cin>>T;

	FOR(iter,0,T){
		cout<<"Case #"<<(iter+1)<<": ";

		int N,K;
		cin>>N>>K;

		vector <__int128> P;

		FOR(i,0,N){
			double tmpin;
			cin>>tmpin;
			__int128 tmp=(__int128)((tmpin+0.001)*100.0);

			P.push_back(tmp);
		}

		__int128 prob[32];

		__int128 retp=0;

		FOR(choicepatt,0,1<<N){
			int ct=0;
			FOR(i,0,N){
				ct+=(choicepatt>>i)&1;
			}

			if(ct!=K)
				continue;
			
			__int128 tieprob=0;

			int cur=0;
			FOR(i,0,N){
				if((choicepatt>>i)&1){
					prob[cur++]=P[i];
				}
			}

			FOR(tiepatt,0,1<<K){
				int vtct=0;
				FOR(i,0,K){
					vtct+=(tiepatt>>i)&1;
				}
				if(vtct!=K/2){
					continue;
				}
				__int128 tmpprob=1;
				FOR(i,0,K){
					if((tiepatt>>i)&1){
						tmpprob*=prob[i];
					}else{
						tmpprob*=100-prob[i];
					}
				}
				tieprob+=tmpprob;
			}

			retp=max(retp,tieprob);
		}

		__int128 one=1;
		FOR(i,0,K){
			one*=100;
		}

		cout<<setprecision(10)<<fixed<<((double)retp/(double)one)<<endl;
	}
}
