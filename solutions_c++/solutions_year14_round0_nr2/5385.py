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
		cerr<<"Case #"<<(iteration+1)<<"\n";
		cout<<"Case #"<<(iteration+1)<<": ";

		double C,F,X;
		cin>>C>>F>>X;

		double ans=9999999;

		int count=0;
		double elapsed=0.0;

		while(true){
			double tmp=elapsed+X/(F*count+2.0);

			if(tmp<=ans)
				ans=tmp;
			else
				break;

			elapsed+=C/(2+F*count);
			count++;

		}

		cout<<fixed<<setprecision(7)<<ans;
			

		

		cout<<endl;
	}
}
