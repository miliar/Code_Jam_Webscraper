#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker,"/STACK:100000000000")
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <complex>

using namespace std;
#define FR(i,n) for(int (i)=0;(i)<(n);(i)++)
#define FOR(i,c,n) for(int (i)=(c);(i)<(n);(i)++)
#define REP(it,v,cont) for(cont::iterator (it)=(v).begin();(it)!=(v).end();++(it)) 
#define CLR(a,c) memset((a),(c),sizeof (a))
#define ALL(v) (v).begin(),(v).end()
#define SQR(a) ((a)*(a))
typedef long long ll;
typedef unsigned long long  ull;
typedef long double lld;
typedef pair<int,int> PII;
typedef pair<ll,ll> PLL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;

int main(){
	freopen("a.in","r",stdin);	
	freopen("a.out","w",stdout);
	int tt;cin>>tt;
	FR(cas,tt){
		printf("Case #%d: ",cas+1);
		string s;cin>>s;
		stack<char> st;
		int res=0;
		FR(i,s.size()){
			//pop
			if(st.empty()) {
				st.push(s[i]);
				continue;
			}
			if(st.top()==s[i]){
				res+=2;
				st.pop();
				continue;
			}
			int rest = s.size()-i-1;
			if(rest<=st.size()){
				res+= st.top()==s[i]?2:1;
				st.pop();
			}else
				st.push(s[i]);
		}
		cout<<res*5<<endl;
	}
}