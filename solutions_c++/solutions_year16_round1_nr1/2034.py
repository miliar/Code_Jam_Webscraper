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
#include <array>
#define PR(x) cout<<#x<<"="<<x<<endl
#define READ2(x,y) scanf("%d %d",&x,&y)
#define REP(i,a,b) for(int i=a;i<b;i++)
#define RP(i,a) for(int i=0;i<a;i++)
#define tr(iter,container) for(auto iter = container.begin();iter!=container.end();iter++) 
#define S(x) cin>>x
#define PRARR(x,n) for(int i=0;i<n;i++) cout<<#x<<"["<<i<<"]= "<<x[i]
#define rd(arr,i,n) for(int i=0;i<n;i++) cin>>arr[i]
#define PB push_back
#define SUM(arr,n,sum) {sum=0;for(int i=0;i<n;i++) sum+=arr[i]; }
#define VC vector
#define CLR(arr) memset(arr,0,sizeof(arr))
#define FILL(arr,val) memset(arr,val,sizeof(arr))
using namespace std;

vector<string> lst;
auto dfs(const string &s, string curString, int idx){
	if (idx == s.size()) {
		lst.push_back(curString);
		return;
	}
	auto nxtMove = max(curString + s[idx], s[idx]+curString);
	dfs(s,move(nxtMove), idx+1);
}
auto solve(string s){
	dfs(s, "",0);
	sort(lst.begin(), lst.end());
	return lst.back();
}	

int main(){
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i){
		lst.clear();
		string s;
		cin >> s;
		cout << "Case #"<<i<<": "<<solve(s) << endl;
	}
}
