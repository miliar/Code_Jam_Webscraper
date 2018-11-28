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
		int r1;
		cin>>r1;

		int cands[4];

		FOR(i,0,4){
			if(i==r1-1){
				FOR(i,0,4)
					cin>>cands[i];

			}else{
				int dummy;
				cin>>dummy;
				cin>>dummy;
				cin>>dummy;
				cin>>dummy;
			}
		}

		int r2;
		cin>>r2;
		
		int num=0;
		int ans;

		FOR(i,0,4){
			if(i==r2-1){
				FOR(j,0,4){
					int cur;
					cin>>cur;

					FOR(k,0,4){
						if(cur==cands[k]){
							num++;
							ans=cur;
						}
					}
				}
			}else{
				int dummy;
				cin>>dummy;
				cin>>dummy;
				cin>>dummy;
				cin>>dummy;
			}
		}

		if(num==0){
			cout<<"Volunteer cheated!\n";
		}

		if(num==1){
			cout<<ans<<endl;
		}

		if(num>1){
			cout<<"Bad magician!\n";
		}

	}
}
