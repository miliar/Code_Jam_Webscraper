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

int sz=7151;
int ss[18];

int ans;
string tmp;

ll power(ll base, ll expo, ll mod){
	ll res=1;
	while(expo){
		if(expo&1){
			res=res*base;
			res%=mod;
		}
		base=base*base;
		base%=mod;
		expo>>=1;
	}
	return res;
}

void eval(vector <int> v){
	int fl=1;
	for(int i=2; i<=10; i++){
		ll vv=0;
		for(int j=0, l=30; j<15; j++, l--){
			if(ss[j])
			vv+=power(i, l, v[i-2]);
			vv%=v[i-2];
		}
		vv+=power(i, 31, v[i-2]);
		vv%=v[i-2];
		if(vv!=0){
			fl=0;
			break;
		}
	}
	if(fl){
		ans=1;
		tmp+="1";
		for(int j=0; j<15; j++){
			if(ss[j])tmp+="1";
			else tmp+="0";
		}
	}
}

void subsets(int i, vector <int> v){
	if(i==15){
		eval(v);
		return ;
	}
	if(!ans){
		ss[i]=0;
		subsets(i+1, v);
	}
	if(!ans){
		ss[i]=1;
		subsets(i+1, v);
	}
}

vector <vector <int> > V;
vector <string> fin;

// the input of the program is the answer to small subtask
int main(){
	string s;
	for(int i=0; i<sz; i++){
		cin>>s;
		vector <int> v;
		int x;
		for(int j=2; j<=10; j++){
			cin>>x;
			v.pb(x);
		}
		memset(ss, 0, sizeof ss);
		ans=0;
		tmp="";
		subsets(0, v);
		if(ans){
			string str=tmp;
			str+=s;
			V.pb(v);
			fin.pb(str);
		}
		if(fin.size()==500)break;
	}
	cout<<"Case #1:"<<endl;
	for(int i=0; i<fin.size(); i++){
		cout<<fin[i]<<" ";
		for(int j=0; j<V[i].size(); j++){
			cout<<V[i][j]<<" ";
		}
		cout<<endl;
	}
	return 0;
}