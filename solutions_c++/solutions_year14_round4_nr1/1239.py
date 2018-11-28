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

	FOR(iteration,0,T){
		cout<<"Case #"<<(iteration+1)<<": ";

		int N,X;
		cin>>N>>X;

		vector<int> S;

		FOR(i,0,N){
			int tmp;
			cin>>tmp;

			S.push_back(tmp);
		}

		sort(ALL(S));

		int used=0;
		int remain=N;

		int ok[N];

		FOR(i,0,N){
			ok[i]=0;
		}



		while(remain){
			used++;
			remain--;

			int touse=-1;

			FOR(i,0,N){
				if(ok[i]==0){
					touse=i;
					break;
				}
			}

			ok[touse]=1;

			for(int i=N-1;i>=0;i--){
				if(S[touse]+S[i]<=X && ok[i]==0){
					ok[i]=1;
					remain--;
					break;
				}

			}
		}

		cout<<used;

				

		cout<<endl;
	}

}
