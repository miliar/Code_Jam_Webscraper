#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <set>
#include <map>
#include <complex>
#include <bitset>
#include <iomanip>
#include <utility>

#define xx first
#define yy second
#define ll long long
#define ull unsigned long long
#define pb push_back
#define pp pop_back
#define pii pair<int,int>
#define vi vector<int>
#define mp make_pair
using namespace std;
const int maxn=20;
string s[maxn];
int cnt[maxn];
int mark[maxn];
int n,m,t;
int ans=0;
int mm=0;
void Bt(int x){
    if(x==m+1){
        for(int i=1;i<=n;i++)if(cnt[i]==0)return;
        int mx=0;
        vector<string>tmp;
        tmp.clear();
        for(int i=1;i<=n;i++){
            tmp.clear();
            for(int j=1;j<=m;j++){
                if(mark[j]==i){
                    string now="";
                    tmp.pb(now);
                    for(int k=0;k<s[j].size();k++){
                        now+=s[j][k];
                        tmp.pb(now);
                    }
                }
            }
            sort(tmp.begin(),tmp.end());
            tmp.resize(unique(tmp.begin(),tmp.end())-tmp.begin());
            mx+=tmp.size();
        }
        if(mx>ans){
            ans=mx;
            mm=1;
        }
        else if(mx==ans){
            mm++;
        }
        return;
    }
    for(int i=1;i<=n;i++){
        mark[x]=i;
        cnt[i]++;
        Bt(x+1);
        mark[x]=0;
        cnt[i]--;
    }
    return;
}
int main(){
    ifstream cin("1.in");
    ofstream cout("1.out");
    cin>>t;
    for(int l=1;l<=t;l++){
        memset(mark,0,sizeof(mark));
        memset(cnt,0,sizeof(cnt));
        cin>>m>>n;
        for(int i=1;i<=m;i++)cin>>s[i];
        ans=0;
        mm=0;
        Bt(1);
        cout<<"Case #"<<l<<": "<<ans<<" "<<mm<<endl;
    }
}
