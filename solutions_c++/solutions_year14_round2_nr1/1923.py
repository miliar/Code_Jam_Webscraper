#include<bits/stdc++.h>
#define ull unsigned long long
#define ll long long
#define pb push_back
#define mem(a,p) memset(a,p,sizeof(a))
#define fi first
#define se second
#define mp make_pair
#define gcd __gcd
#define rep(i,a,b) for(int i=a;i<b;++i)
#define all(a) a.begin(),a.end()
#define sz(a) ((int)(a.size()))
#define DREP(a) sort(all(a));a.erase(unique(all(a)),a.end())
using namespace std;
#define VI vector<int>
#define PII pair<int,int>

int main() {
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    string s1,s2;
    int t,n;
    cin>>t;
    rep(cs,1,t+1) {
        cin>>n;
        cin>>s1>>s2;
        int len1=s1.size();
        int len2=s2.size();
        int i=1,j=1,cnt=0;
        bool flag=true;
        if(s1[0]!=s2[0])
            flag=0;
        while((i<len1||j<len2) && (flag)) {
            if(s1[i]!=s2[j]) {
                if(s1[i]==s1[i-1])
                    i++,cnt++;
                else if(s2[j]==s2[j-1])
                    j++,cnt++;
                else flag=false;
            } else
                i++,j++;
        }
        if(!flag)
            cout<<"Case #"<<cs<<": "<<"Fegla Won"<<"\n";
        else cout<<"Case #"<<cs<<": "<<cnt<<"\n";
    }
    return 0;
}

