#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cmath>
#include<cstring>
#include<map>
#include<set>
#include<vector>
#include<queue>
using namespace std;

typedef pair<int,int> pii;
typedef vector<pii> vii;
typedef vector<int> vi;

#define FOR(i,a,b) for(int i=a;i<=b;i++)
#define DFOR(i,a,b) for(int i=a;i>=b;i--)
#define mp(x,y) make_pair((int)x,(int)y)
#define fi first
#define se second
#define all(a) (a).begin(),(a).end()
#define BUG(x) {cout << #x << " = " << x << endl;}
#define PR(x,a,b) {cout << #x << " = "; FOR(i,a,b) cout << x[i] << ' '; cout << endl;}
#define ll long long
#define DEBUG 1

int main(){
    if (DEBUG==1){
        freopen("B-large.in","r",stdin);
        freopen("output.txt","w",stdout);
    }
    int t;
    string s;
    cin>>t;
    getline(cin,s);
    int n;
    int oo=1000000000;
    int a[111];
    int ans=0;
    int index=0;
    FOR(test,1,t){
        getline(cin,s);
        int n= s.length();
        FOR(i,1,n)a[i]=s[i-1]=='+'?1:0;
        ans=0;
        index=1;
        DFOR(i,n,1){
            if (a[i]!=index){
                ans++;
                index=1-index;
            }
        }
        cout<<"Case #"<<test<<": "<<ans;
        if (test<t) cout<<endl;
    }
    return 0;
}
