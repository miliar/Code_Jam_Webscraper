#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
#include <cstring>

#define lld long long int 
#define EOL '\0'
#define PEL cout<<endl;
#define N 1000002
#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define rep(n) for(int i =0;(i)<(int)(n);(i)++)
#define repi(n) for(int i =0;(i)<(int)(n);(i)++)
#define repj(n) for(int j =0;(j)<(int)(n);(j)++)
#define repij(n,m) for(int i =0;(i)<(int)(n);(i)++) for(int j =0;(j)<(int)(m);(j)++)
#define rep1n(n) for(int i=1;i<(int )(n);i++)

#define SSTR( x ) dynamic_cast< std::ostringstream & >( \
                  std::ostringstream() << std::dec << x ).str()


using namespace std;

int ps = 0;
int pos[N];

bool isvowel(char c ) { 
	return c == 'a' || c=='e' || c == 'i' || c== 'o' || c=='u';
}

int main() 
{
	freopen("D:\\MyCode\\CJ\\data\\A-large.in", "r",stdin);
	freopen("D:\\MyCode\\CJ\\data\\test.out", "w",stdout);
	//cout<<"read"<<endl;
	int t; cin>>t;
	for(int tc=1;tc<=t;tc++) {
	string a;
	cin>>a;
	int n,len = a.length();
	long long int sc=0;; 
	cin>>n;
	ps=0;
	
	for(int i=0,j=0;i<len;i++ ) { 
		for(;j<n && i+j < len; ) {
			if(!isvowel(a[i+j])) { 
				j++;
			}
			else {
				i = i+j;j=0; break;
			}
		}
		if(j==n) {
			pos[ps++] = i;
			j = n-1;
		}
	}
	
	
	for(int i=0,curr=0;i+n<=len && curr < ps;i++) {
		//cout<<i<<" "<<curr<<" "<< pos[curr]<<" "<<sc<<endl;
		if(pos[curr]<i) curr++; if(curr >=ps ) break;
		sc += ( len+1-(pos[curr]+n));		
		//cout<<i<<" "<<curr<<" "<< pos[curr]<<" "<<sc<<endl;
	}
	
	cout<<"Case #"<<tc<<": "<<sc<<endl;
	}
	return 0;
}