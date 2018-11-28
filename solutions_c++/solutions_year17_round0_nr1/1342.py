#include<bits/stdc++.h>
#define rep(i,x,y) for(i=x;i<y;i++)
#define pb(f) push_back(f)

#define ll long long
#define scs(a) scanf("%s",a)
#define mp make_pair
#define fi first
#define se second
#define mod 1000000007LL
#define inf 100000000000000009LL

const int N=200005;
using namespace std;
typedef pair<ll,ll> pii;
typedef vector<int> vi;
typedef vector< pii > vpii;
using namespace std;

FILE *fin=freopen("1.in","r",stdin); FILE *fout=freopen("out.txt","w",stdout);
int main(){
    int t;
    string s;int k;
    cin>>t;
    int cas=0;
    while(t--){
        cas++;
        cout<<"Case #"<<cas<<": ";
        cin>>s>>k;
        int i,n=s.length();
        s=" "+s;
        int cnt=0;
        for(i=1;i<=n;i++){
            int j=i+k-1;
            if(s[i]=='+') continue;
            if(j>n) break;
            cnt++;
            for(int k=i;k<=j;k++) {
                if(s[k]=='-') s[k]='+';
                else s[k]='-';
            }
        }
        if(i<n+1){
            cout<<"IMPOSSIBLE"<<endl;continue;
        }
        cout<<cnt<<endl;
    }
}
