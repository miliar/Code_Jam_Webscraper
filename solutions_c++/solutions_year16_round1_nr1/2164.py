#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int,int>ii;
typedef vector<int> vi;
typedef vector <ii> vii;
#define PB push_back
#define MP make_pair
#define IN insert
#define F first
#define S second
#define SIZE(c) (c).size()
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define RESET(c,x) memset(c,x,sizeof(c))
#define FOR(i, c, n) for(int i = c; i < (int)n ; i++)
#define MOS(v,c,n) FOR(i,c,n)cout<<v[i]<<' ';cout<<'\n';
#define BAC(i, n, c) for(int i = n; i >= (int)c; i--)
#define FOREARCH(i, v) for (__typeof(v.begin()) i = v.begin(); i != v.end(); i++)
#define BACEARCH(i, v) for (__typeof(v.rbegin()) i = v.rbegin(); i != v.rend(); i++)
//--------Main---------//

int t;
string cad;
int main(){
	ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
	cin>>t;
	FOR(cas,1,t+1){
		cin>>cad;
		string ans="";
		ans+=cad[0];
		FOR(i,1,cad.length()){
			if(cad[i]<ans[0]){
				ans = ans + cad[i];
			}else{
				ans = cad[i]+ans;
			}
		}
		cout<<"Case #"<<cas<<": "<<ans<<'\n';
		
	}
	
	

    return 0;
}
