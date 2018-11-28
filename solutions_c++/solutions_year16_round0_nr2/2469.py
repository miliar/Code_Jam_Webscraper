#include <bits/stdc++.h>
#define pb push_back
#define pii pair <int, int>
#define mp make_pair
#define F first
#define S second
#define ll long long
#define iosbase ios_base::sync_with_stdio(false)
#define sc scanf
#define pr printf
#define null NULL
#define getcx getchar_unlocked
#define lb lower_bound
#define ub upper_bound
#define all(x) x.begin(), x.end()
#define pll pair<ll,ll>
#define vi vector <int>
#define vll vector <ll>
 
#define maxs 200005
#define logmaxs 25
 
#define MOD 1000000007
#define eps 1e-9
#define llmax 1e18+5
#define intmax 1e9+5
#define intmin -intmax

#define pi 3.14159265358979

using namespace std;

vector <int> gr[1<<11];

int s[11];
int cnt;
map <string, int> M;

int m[1<<11][1<<11];

void eval(int n){
	cnt++;
	string _s="";
	for(int i=0; i<n; i++){
		if(s[i])_s+="+";
		else _s+="-";
	}
	M[_s]=cnt;
}

void subsets(int i, int n){
	if(i==n){
		eval(n);
		return ;
	}
	s[i]=0;
	subsets(i+1, n);
	s[i]=1;
	subsets(i+1, n);
}

void gen(int n){
	M.clear();
	for(int i=0; i<=(1<<n); i++){
		gr[i].clear();
	}

	memset(s, 0, sizeof s);
	memset(m, 0, sizeof m);
	cnt=0;
	subsets(0, n);

	map <string, int>::iterator it;
	for(it=M.begin(); it!=M.end(); it++){
		string tmp1=it->first;
		int id=it->second;
		for(int i=1; i<=tmp1.size(); i++){
			string tmp=tmp1;
			//cout<<tmp<<" "<<i<<" ";
			for(int j=0; j<i/2; j++){
				swap(tmp[j],tmp[i-1-j]);
			}
			//cout<<tmp<<" ";
			for(int j=0; j<i; j++){
				if(tmp[j]=='+')tmp[j]='-';
				else tmp[j]='+';
			}
			//cout<<tmp<<" ";
			int idx=M[tmp];
			if(idx==id)continue;
			if(m[id][idx]==0){
				m[id][idx]=1;
				gr[id].pb(idx);
			}
		}
		//cout<<endl;
	}
	// for(int i=1; i<=4; i++){
	// 	for(int j=0; j<gr[i].size(); j++)cout<<gr[i][j]<<" ";
	// 	cout<<endl;
	// }
}

int d[1<<11];
int vis[1<<11];

int dis(int src, int des){
	memset(vis, 0, sizeof vis);
	memset(d, 0, sizeof d);
	queue <int> q;
	q.push(src);
	vis[src]=1;
	while(!q.empty()){
		int u=q.front();
		q.pop();
		for(int i=0; i<gr[u].size(); i++){
			if(!vis[gr[u][i]]){
				q.push(gr[u][i]);
				d[gr[u][i]]=1+d[u];
				vis[gr[u][i]]=1;
			}
		}
	}
	return d[des];
}

int main(){
	iosbase;
	int t;
	cin>>t;	
	string s;
	for(int T=1; T<=t; T++){
		cin>>s;
		int n=s.size();
		gen(n);
		int src=M[s];
		string tar="";
		for(int i=0; i<n; i++)tar+="+";
		int des=M[tar];
		int ans=dis(src, des);
		pr("Case #%d: %d\n", T, ans);
	}
	return 0;
}