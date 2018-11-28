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
#define pii pair<int,int>
using namespace std;
template <class X>
void input(vector<X>&a,int N){
    X temp;
    rep(i,0,N){
        cin>>temp;
        a.push_back(temp);
    }
}
bool solution(int* a,string k){
    int cur=0;
    rep(i,0,26){
        cur|=a[i];
    }
    if(!cur){
        sort(all(k));
        cout<<k;
        return true;
    }
    else{
        string p[10]={"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
        for(string i:p){
            for(char j:i){
                a[j-'A']--;
            }
            bool isneg=false;
            rep(i,0,26){
                if(a[i]<0)isneg=1;
            }
            if(isneg){
                for(char j:i){
                    a[j-'A']++;
                }
                continue;
            }
            else{
                string temp;
                temp.pb('0'+(find(p,p+10,i)-p));
                bool alpha=solution(a,k+temp);
                if(!alpha){
                    for(char j:i){
                    a[j-'A']++;
                }

                }
                else{
                    return true;
                }
            }
        }
    }
    return false;
}
void solve(){
    string s;
    cin>>s;
    int a[26]={0};
    for(char i:s){
        a[i-'A']++;
    }
    string ans;
    solution(a,ans);
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    freopen("A-small-attempt2.in","r",stdin);
    freopen("A-small-attempt2.out","w",stdout);
	int t;
	cin>>t;
	for(int i=0;i<t;i++){
        cout<<"Case #"<<i+1<<": ";
		solve();
        cout<<endl;
	}
	return 0;
}
