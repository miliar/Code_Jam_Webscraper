#include <iostream>
#include <sstream>
#include <cstdio>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <cmath>
#include <algorithm>
#include <iomanip>
using namespace std;
#define sqr(x) ((x)*(x))
#define mp(x,y) make_pair((x),(y))
#define FOR(i,n) for(int i = 0 ; i<n ;i++)
#define f(i,x,y) for (int i = x; i < y; i++)
#define all(v) v.begin(),v.end()
#define pb push_back
#define sz(v) ((int)v.size())
#define fst first
#define snd second
#define itm1 fst.fst
#define itm2 fst.snd
#define itm3 snd
#define mt(a,b,c) mp(mp(a,b),c)
#define oo 2000000000

typedef long long ll  ;
typedef vector<int> vi ;
typedef pair<ll,ll> ill;
typedef pair<int,int> ii ;
typedef pair<ii, int> tri;
typedef vector<string> vs;

queue<string> q[100002];
string case1(string w, char c){
	w.pb(c);
	return w;
}

string case2(string w, char c){
	string k;
	k.pb(c);
	for(int l=0;l<w.size();l++){
		k.pb(w[l]);
	}
	return k;
}

int main(){
	string s;
	int t;
	vs ans;
	string w;
	string word1;
	string word2;
	int u;
	cin>>t;

	for(int i=1;i<=t;i++){
		cin>>s;
		ans.clear();
		for(int j=0;j<s.size();j++){
			char c=s[j];
			string aux;
			aux.pb(c);
			if(j==0){
				q[j].push(aux);
			}	
			else{
				while(!q[j-1].empty()){
					w=q[j-1].front();
					q[j-1].pop();
					word1=case1(w,c);
					word2=case2(w,c);
					//cout<<word1<<" "<<word2<<endl;
					q[j].push(word1);
					q[j].push(word2);
				}
			}
			u=j;
		}
		while(!q[u].empty()){
			ans.pb(q[u].front());
			q[u].pop();
		}
		sort(all(ans));
		cout<<"Case #"<<i<<": ";
		cout<<ans[ans.size()-1]<<endl;
	}

}