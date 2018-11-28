/*
ID: rohangu1
LANG: C++
TASK: 
*/

#include <iostream>
#include <fstream>
#include <utility>
#include <algorithm>
#include <vector>
#include <cstring>
#include <cmath>
#include <set>
#include <string>
#include <queue>
#include <cstdio>
#include <iterator>

using namespace std;

typedef vector<int> vi;
typedef vector< vi > vvi;
typedef pair<int,int> ii;
typedef long long LL;

#define np next_permutation
#define FOR(i,a,b) for(i=a;i<=b;i++)
#define FORr(i,a,b) for(i=a;i>=b;i--)
#define tr(c, it) \
		for(typeof(c.begin()) it = c.begin() ; it != c.end() ; it++)
#define max(a,b) (a>b?(a):(b))
#define min(a,b) (a>b?(b):(a))
#define all(a) (a).begin(),(a).end()
#define mp(i,j) make_pair(i,j)
#define sz(a) a.size()
#define pb(i) push_back(i) 
#define fx first
#define sx second
#define MOD 1000000007

ifstream in("p1.in",ifstream::in);
ofstream out("p1.out",ios::out);

int main(){
	int i,j;
	LL n,t,c,r,test;
	in>>test;
	FOR(c,1,test){
		LL ans = 0;
		in>>r>>t;
		i = 1;
		while(2*r+2*i-1<=t){
			ans++;
			t = t - (2*r+2*i-1);
			i+=2;
		}
		out<<"Case #"<<c<<": "<<ans<<endl;
	}
	return 0;
}
