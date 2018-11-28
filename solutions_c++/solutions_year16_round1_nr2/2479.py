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
 
#define maxs 205
#define logmaxs 25
 
#define MOD 1000000007
#define eps 1e-9
#define llmax 1e18+5
#define intmax 1e9+5
#define intmin -intmax

#define pi 3.14159265358979

using namespace std;

vector <vector <int> > V;

int sub[50];

int sz;

bool cmp(vector <int> v1, vector <int> v2){
	return (v1[0]<v2[0]);
}


int m[55][55];
vector <vector <int> > ans, ans1;

bool exists(vector <int> v, int n){
	for(int i=0; i<ans1.size(); i++){
		vector <int> vm=ans1[i];
		int fl1=1;
		for(int j=0; j<n; j++){
			if(vm[j]!=v[j]){
				fl1=0;
				break;
			}
		}
		if(fl1)return true;
	}
	return false;
}


bool check(vector <vector <int> > v, int n){
	memset(m, 0, sizeof m);
	for(int i=0; i<v.size(); i++){
		for(int j=0; j<n; j++){
			m[i][j]=v[i][j];
		}
	}
	for(int i=0; i<n; i++){
		for(int j=1; j<n; j++){
			if(m[j][i]<=m[j-1][i])return false;
		}
	}

	int cnt=0;
	for(int i=0; i<n; i++){
			vector <int> vv;
			for(int j=0; j<n; j++){
				vv.pb(m[j][i]);
			}
			if(!exists(vv, n)){
				cnt++;
				if(cnt>1)break;
			}
		}
		if(cnt==1)
	return true;
	
	return false;
}


int fl;


void eval(){
	vector <vector <int> > tmp;
	ans1.clear();
	for(int i=0; i<sz; i++){
		if(sub[i]==1){
			tmp.pb(V[i]);
		}
		else ans1.pb(V[i]);
	}
	if(tmp.size()!=(sz+1)/2)return ;
	
	sort(tmp.begin(), tmp.end(), cmp);

//cout<<"here";
	//return ;
	
	for(int i=1; i<tmp.size(); i++){
		if(tmp[i][0]==tmp[i-1][0])return ;
	}
	int n=(sz+1)/2;
	//cout<<n<<" ";
	//return ;
	if(check(tmp, n)){
		// for(int i=0; i<tmp.size(); i++){
		// 	for(int j=0; j<n; j++)cout<<tmp[i][j]<<" ";
		// 	cout<<endl;
		// }
		fl=1;
		ans=tmp;
	}
}

void subsets(int i){
	//cout<<i<<" ";
	//return ;
	if(i==sz){
		eval();
		return ;
	}
	if(!fl){
		sub[i]=0;
		subsets(i+1);
	}
	if(!fl){
		sub[i]=1;
		subsets(i+1);
	}
	
}




int main(){
	iosbase;
	int t,n,x;
	cin>>t;
	for(int T=1; T<=t; T++){
		cin>>n;
		for(int i=0; i<2*n-1; i++){
			vector <int> v;
			for(int j=0; j<n; j++){
				cin>>x;
				v.pb(x);
			}
			V.pb(v);
		}
		sz=2*n-1;
		memset(sub, 0, sizeof sub);
		fl=0;
		//cout<<"call";
		subsets(0);
		cout<<"Case #"<<T<<": ";
		for(int i=0; i<n; i++){
			vector <int> vv;
			for(int j=0; j<n; j++){
				vv.pb(m[j][i]);
			}
			if(!exists(vv, n)){
				for(int i=0; i<vv.size(); i++){
					cout<<vv[i]<<" ";
				}
				break;
			}
		}
		cout<<endl;
		ans1.clear();
		ans.clear();
		V.clear();
	}
	return 0;
}