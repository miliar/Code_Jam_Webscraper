#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef pair<double,double> pdd;
typedef pair<int, double> pid;
typedef unsigned long long ull;
typedef vector<pii> vpii;
typedef vector<pid> vpid;

#define FO(i,s,e,p) for(int i=(s);i<(e);i+=p)
#define FOD(i,s,e,p) for(int i=(s);i>(e);i-=p)


#define FOR(i,s,e) FO(i,s,e,1)
#define FORE(i,s,e) FOR(i,s,e+1)
#define FORD(i,s,e) FOD(i,s,e,1)
#define FORDE(i,s,e) FORD(i,s,e-1)

#define REP(i,n) FOR(i,0,n)
#define SORT(v) sort((v).begin(),(v).end())
#define UN(v) sort((v).begin(),(v).end()),v.erase(unique(v.begin(),v.end()),v.end())
#define CL(a,b) memset(a,b,sizeof(a))
#define pb push_back
#define mp make_pair

int main() {
	int T, c=1;
	cin>>T;
	while(T--){
		long long r, t;
		cin>>r>>t;
		long long s=0;
		long long n = r+1;
		while(t > 0){
			t -= (n+r)*(n-r);
			n+=2; r+=2; if (t>=0)s++;
		}
		cout<<"Case #"<<c++<<": "<<s<<endl;
	}
	
	return 0;
}
