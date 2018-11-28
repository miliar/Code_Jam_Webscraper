#include <iostream>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <ctime>
#include <functional>
#include <bitset>
#include <utility>
#include <sstream>
#include <fstream>
#include <stack>
#include <cstdlib>
#include <complex>
#include <set>
#include <map>

using namespace std;

#define INF 1070000000LL
#define pb push_back
#define irep(i,a,b) for(int i=a;i<b;i++)
#define rep(i,n) irep(i,0,n)

typedef long long lint;
typedef pair<int, int> pint;
struct Edge{
    int to,weight;
};
typedef vector<vector<Edge> > Graph;

#define FIRST "RICHARD"
#define SECOND "GABRIEL"

void print_ans(int i,string s){
    cout << "Case #" << i << ": " << s << endl;
}


int main(){
    int t;cin >> t;
    vector<int> x(t),r(t),c(t);
    rep(i,t){
	cin >> x[i] >> r[i] >> c[i];
    }
    rep(i,t){
	if(x[i] == 1){
	    print_ans(i+1,SECOND);
	    continue;
	}
	if(x[i] == 2){
	    if((r[i]*c[i])%2 == 0){
		print_ans(i+1,SECOND);
		continue;
	    }
	    else{
		print_ans(i+1,FIRST);
		continue;
	    }
	}
	if(x[i] == 3){
	    if(r[i]<x[i] && c[i]<x[i]){
		print_ans(i+1,FIRST);
		continue;
	    }
	    else{
		if((r[i]*c[i]>=6) && (r[i]*c[i]%3 == 0)){
		    print_ans(i+1,SECOND);
		    continue;
		}
		else{
		    print_ans(i+1,FIRST);
		    continue;
		}
	    }
	}
	if(x[i] == 4){
	    if(r[i]<x[i] && c[i]<x[i]){
		print_ans(i+1,FIRST);
		continue;
	    }
	    else{
		if((r[i]*c[i])>=12){
		    print_ans(i+1,SECOND);
		    continue;
		}
		else{
		    print_ans(i+1,FIRST);
		    continue;
		}
	    }
	}
    }
}
