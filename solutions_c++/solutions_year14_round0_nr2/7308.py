#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include<stdio.h>
#include<climits>


using namespace std;

#define rep(i,a,b) for(int i=a;i<b;++i)
typedef long long ll;
#define s(n) cin>>n
#define p(n) cout<<n<<endl


int main(){

	int t;
	s(t);

	rep(k,0,t){

		double C,F,X;
		s(C);s(F);s(X);

		double nearest = (F*X-2*C)/(C*F)-1;
//		p(nearest);
		
		nearest = nearest>0?nearest:0;
		
		int turns  = nearest-(int)nearest==0?nearest:((int)nearest)+1;

//		p(turns);
		double sum =0;
		double diff = 2;

		while(turns>0){
			--turns;
			sum += 1/(diff);
			diff += F;
			//	p(diff);
		}

		double final = C*sum + X/diff;
		cout << std::setprecision(7) << std::fixed;
		cout<<"Case #"<<k+1<<": "<<final<<endl;

	}


	return 0;
}
