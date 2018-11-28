#include <bits/stdc++.h>
#define ll long long int
#define ull unsigned long long int
#define pb push_back
#define mp make_pair
#define vi vector<int>
#define vvi vector<vi>
#define Max(a,b) ((a)>(b)?(a):(b))
#define Min(a,b) ((a)<(b)?(a):(b))
#define rep(i,a,b) for(ll i=a;i<b;i++)
#define all(a) a.begin(),a.end()
#define sum(a) accumulate(all(a),0)
#define endl '\n'
#define hell 1000000007

using namespace std;
template <class X>
void input(vector<X>&a,int N){
    X temp;
    rep(i,0,N){
        cin>>temp;
        a.push_back(temp);
    }
}
void solve(int t){
    string s;
    cin>>s;
    int ans=0;
    int n=s.length()-1;
    while(n>=0){
        if(s[n]=='+'){
            n--;
        }
        else{
            if(s[0]=='-'){
                reverse(s.begin(),s.begin()+n+1);
                rep(i,0,n+1){
                    if(s[i]=='+')s[i]='-';
                    else s[i]='+';
                }
                ans++;
                continue;
            }
            else{
                int k=0;
                while(s[k]=='+'){
                    s[k]='-';
                    k++;
                }
                ans++;
            }
        }
    }
    cout<<"Case #"<<t<<": "<<ans<<endl;
}
int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
	int t;
	cin>>t;
	rep(i,0,t){
		solve(i+1);
	}
	return 0;
}
