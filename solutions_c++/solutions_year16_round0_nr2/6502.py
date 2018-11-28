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
string comp(string text){
	string ans = "";
	FOR(i,0,text.length()-1){
		if(text[i]!=text[i+1]){
			ans+=text[i];
		}
	}
	ans+=text[text.length()-1];
	return ans;
}

int main(){
	ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
	cin>>t;
	FOR(cas,1,t+1){
		cin>>cad;
		//cout<<cad<<'\n';
		cad = comp(cad);
		//cout<<cad<<'\n';
		int n = cad.length();
		if(n%2==0){
			if(cad[0]=='+')	cout<<"Case #"<<cas<<": "<<n<<"\n";
			else cout<<"Case #"<<cas<<": "<<n-1<<"\n";
		}else{
			if(cad[0]=='+') cout<<"Case #"<<cas<<": "<<n-1<<"\n";
			else cout<<"Case #"<<cas<<": "<<n<<"\n";
		}
	}
    return 0;
}
