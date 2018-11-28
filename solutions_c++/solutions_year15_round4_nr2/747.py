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
		int N;
		cin>>N;

		double V,X;
		cin>>V>>X;

		vector <pair <double, double> > source;

		FOR(i,0,N){
			pair <double, double> t;
			cin>>(t.second)>>(t.first);

			source.push_back(t);

		}

		sort(ALL(source));

		if(source.size()==1){
			if(source[0].first!=X){
				cout<<"IMPOSSIBLE"<<endl;
				continue;
			}else{
				cout<<setprecision(10)<<(V/source[0].second)<<endl;
				continue;
			}
		}

		if(X<(source[0].first) || (source[1].first)<X){
			cout<<"IMPOSSIBLE"<<endl;
			continue;
		}

		if(source[0].first == source[1].first){
			cout<<setprecision(10)<<(V/(source[0].second+source[1].second))<<endl;
			continue;
		}

		double v1=V*(X-(source[0].first))/((source[1].first)-(source[0].first));
		double v2=V*((source[1].first)-X)/((source[1].first)-(source[0].first));

		cout<<setprecision(10)<<max(v1/(source[1].second),v2/(source[0].second));



		cout<<endl;
	}

}
