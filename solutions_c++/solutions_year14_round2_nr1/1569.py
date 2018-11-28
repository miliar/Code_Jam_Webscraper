#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <climits>
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
#include <memory.h>

#define pb push_back
#define ll long long
#define mp make_pair
#define f first
#define s second
#define all(x) x.begin(),x.end()
#define rall(x) x.rbegin(),x.rend()
#define pi acos(-1.0)
#define EPS 1e-9

using namespace std;
string unique(string s){
	string ret;
	for(int i=0;i<s.size();i++){
		if(ret.empty())ret+=s[i];
		else{
			if(ret[ret.size()-1]!=s[i])ret+=s[i];
		}
	}
	return ret;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large4.out","w",stdout);
	int t,cs=0;cin>>t;
	while(t--){
		int n;cin>>n;set<string> st;string s;vector<string> v(n);
		for(int i=0;i<n;i++){
			cin>>v[i];s=unique(v[i]);st.insert(s);
		}
		cout<<"Case #"<<++cs<<": ";
		if(st.size()!=1){cout<<"Fegla Won\n";continue;}
		int ans=0;
		for(int i=0;i<s.size();i++){
			char c=s[i];vector<int> tmp;
			for(int j=0;j<n;j++){
				int cnt=0;
				while(!v.empty() && v[j][0]==c){
					cnt++;v[j].erase(v[j].begin()+0);
				}
				tmp.pb(cnt);
			}
			int cc=INT_MAX;
			for(int i=1;i<=1000;i++){
				int cnt=0;
				for(int j=0;j<tmp.size();j++){
					cnt+=abs(tmp[j]-i);
				}
				cc=min(cc,cnt);
			}
			ans+=cc;
		}
		cout<<ans<<"\n";
	}
	return 0;
}
