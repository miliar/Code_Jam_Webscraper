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

ifstream in("fair.in",ifstream::in);
ofstream out("fair.out",ios::out);

int map[20];
int start[20][2];

vector <LL> tmp;
vector <LL> a;

bool iscorrect(LL n){
	memset(map,0,sizeof(map));
	int l = 0,i;
	while(n){
		map[++l] = n%10;
		n/=10;
	}
	FOR(i,1,l/2){
		if(map[i]!=map[l-i+1])
			return false;
	}
	return true;	
}

void generate(int n){
	LL c,j,add,i,k,m;
	start[1][0] = 0;
	start[1][1] = 9;
	FOR(i,0,9)
		tmp.pb(i);
	start[2][0] = 10;
	start[2][1] = 18;
	FOR(i,1,9)
		tmp.pb(11*i);
	FOR(i,3,n){
		m = i-2;
		add = pow(10,i-1) + 1;
		c = 0;
		FOR(j,1,9){
			FOR(k,start[m][0],start[m][1]){
				tmp.pb(j*add+tmp[k]*10);
				++c;
			}
		}
		start[i][0] = start[i-1][1]+1;
		start[i][1] = start[i-1][1]+c;
	}
}


int main(){
	int i,j;
	int n,t;
	LL l,r,ans;
	generate(7);
	n = sz(tmp)-1;
	a.pb(0);
	a.pb(1);
	FOR(i,2,n){
		if(iscorrect(tmp[i]*tmp[i])){
			a.pb(tmp[i]*tmp[i]);
		}
	}
	sort(all(a));
	vector <LL>::iterator it = a.begin(),low,high;
	in>>t;
	FOR(i,1,t){
		in>>l>>r;
		low = lower_bound(all(a),l);
		high = upper_bound(all(a),r);
		ans = high - low;
		out<<"Case #"<<i<<": "<<ans<<endl;
	}
	return 0;
}
