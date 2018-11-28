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


int main(){
    int t;cin >> t;
    vector<int> s_max(t);
    vector<string> s(t);
    rep(i,t){
	cin >> s_max[i];
	cin >> s[i];
    }
    rep(i,t){
	int cnt = 0;
	int res = 0;
	rep(j,s_max[i]+1){
	    if(cnt < j && s[i][j] -'0' != 0){
		res += (j-cnt);
		cnt += j+(s[i][j]-'0');
	    }
	    else{
		cnt += (s[i][j]-'0');
	    }
	}
	cout << "Case #" << i+1 << ": " << res << endl; 
    }
}
