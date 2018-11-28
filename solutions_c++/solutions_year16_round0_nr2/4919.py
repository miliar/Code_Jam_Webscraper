#include<bits/stdc++.h>

#define xx first
#define yy second
#define LL long long
#define inf 100000000
#define pb push_back
#define vsort(v) sort(v.begin(),v.end())
#define pi acos(-1)
#define clr(a,b) memset(a,b,sizeof a)
#define bclr(a) memset(a,false,sizeof a)
#define pii pair<int,int>
#define MOD 1000000007
#define MP make_pair
#define MX 1005

using namespace std;


int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int test; cin>>test;
    for(int kase=1;kase<=test;kase++){
        string s; cin>>s;
        int len=s.length(),res=0;
        for(int i=1;i<len;i++){
            if(i==0 || s[i]==s[i-1]) continue;
            res++;
        }
        if(s[len-1]=='-') res++;
        cout<<"Case #"<<kase<<": "<<res<<endl;
    }
    return 0;
}

