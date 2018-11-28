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
		
		int M,N;

		cin>>M>>N;

		vector <string> S;

		FOR(i,0,M){
			string tmp;
			cin>>tmp;
			S.push_back(tmp);
		}

		int worse=0;
		int worsecount=0;

		for(long long assign=0; assign<(1<<(2*M)); assign++){
			int cont = 0;
			FOR(i,0,M){
				if(((assign>>(2*i)) & 3)>=N)
					cont=1;
			}
			if(cont)
				continue;


			vector<set<string> > res;

			FOR(i,0,N)
				res.push_back(*(new set<string>()));

			//FOR(i,0,N)
				//res[i].insert("");

			FOR(i,0,11){
				FOR(j,0,M){
					if(S[j].length()>=i)
						res[(assign>>(2*j)) & 3].insert(S[j].substr(0,i));
				}
			}


			int tmp = 0;

			FOR(i,0,N){
				tmp += (int)res[i].size();
			}
			
			if(tmp>worse){
				worse=tmp;
				worsecount=0;
			}

			if(tmp==worse)
				worsecount++;



		}


		cout<<worse<<" "<<worsecount;

		cout<<endl;
	}

}
