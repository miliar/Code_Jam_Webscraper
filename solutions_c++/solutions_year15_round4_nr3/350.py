#include<bits/stdc++.h>
#include<ext/pb_ds/assoc_container.hpp>
#include<ext/pb_ds/trie_policy.hpp>
#pragma GCC optimize ("O3")
#define f first
#define s second
using namespace std;
using namespace __gnu_pbds;
typedef pair<double,double> par;
bool en[5005],fr[5005];
bool en2[5005],fr2[5005];
int main(){
    ios::sync_with_stdio(0);
    int T,t=0;
    cin>>T;
    while(T--){t++;
        vector<int> inp[205];
        trie<string,int>mp;
        memset(en,0,sizeof(en));
        memset(fr,0,sizeof(fr));
        int n;
        cin>>n;
        string s,ss;
        getline(cin,s);
        stringstream str;
        int id=1;
        getline(cin,s);
        str<<s;
        while(str>>s){
            if(!mp[s])
                mp[s]=id++;
            en[mp[s]]=1;
            }
        str.clear();
        getline(cin,s);
        str<<s;
        while(str>>s){
            if(!mp[s])
                mp[s]=id++;
            fr[mp[s]]=1;
            }
        str.clear();
        n-=2;
        for(int i=0;i<n;i++){
            getline(cin,s);
            str<<s;
            while(str>>s){
                if(!mp[s])
                    mp[s]=id++;
                inp[i].push_back(mp[s]);
                }
            sort(inp[i].begin(),inp[i].end());
            inp[i].resize(unique(inp[i].begin(),inp[i].end())-inp[i].begin());
            str.clear();
            }
        int mask=(1<<n)-1;
        int ans=0x7fffffff;
        for(int i=0;i<=mask;i++){
            memset(en2,0,sizeof(en2));
            memset(fr2,0,sizeof(fr2));
            for(int j=0;j<n;j++){
                if(i&(1<<j)){
                    for(int x:inp[j])
                        fr2[x]=1;
                    }
                else{
                    for(int x:inp[j])
                        en2[x]=1;
                    }
                }
            int cnt=0;
            for(int i=0;i<=id;i++)
                if((en[i]||en2[i])&&(fr[i]||fr2[i]))
                    cnt++;
            ans=min(ans,cnt);
            }
        printf("Case #%d: %d\n",t,ans);
        }
    return 0;
    }
