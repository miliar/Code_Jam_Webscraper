#include <bits/stdc++.h>
#define ll          long long int
#define pb          push_back
#define mp          make_pair
#define vi          vector<int>
#define Max(a,b)    ((a)>(b)?(a):(b))
#define Min(a,b)    ((a)<(b)?(a):(b))
#define rep(i,a,b)  for(int i=a;i<b;i++)
#define all(a)      a.begin(),a.end()
#define F           first
#define S           second
#define sz(x)       (int)x.size()
#define hell        1000000007
#define endl        '\n'

using namespace std;

void solve(){
    int N;
    cin>>N;
    int a[N];
    rep(i,0,N)cin>>a[i];
    while(true){
        int k=max_element(a,a+N)-a;
        if(a[k]==0)break;
        vi p;
        rep(i,0,N){
            if(a[i]==a[k])p.pb(i);
        }
        if(p.size()==2){
            cout<<(char)('A'+p[0])<<(char)('A'+p[1])<<" ";
            a[p[0]]--;
            a[p[1]]--;
        }
        else{
            cout<<(char)('A'+k)<<" ";
            a[k]--;
        }
    }
}

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A1.out","w",stdout);
	int t=1;
	cin>>t;
	rep(i,0,t){
        cout<<"Case #"<<i+1<<": ";
		solve();
        cout<<endl;
	}
	return 0;
}
