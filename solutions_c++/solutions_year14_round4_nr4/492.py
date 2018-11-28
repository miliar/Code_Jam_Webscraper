#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
int n,m;
string s[10];
int maxn;
int trie[200][27];
int done[200];
int root,N;
void add(string s){
    int i,t;
    t=root;
    for(i=0;i<s.size();i++){
        if(trie[t][s[i]-'A']!=0){
            t=trie[t][s[i]-'A'];
        }
        else{
            N++;
            trie[t][s[i]-'A']=N;
            t=trie[t][s[i]-'A'];
        }
    }
}
int calc(){
    int j,i,S=0;
    //cout<<m<<endl;
    for(i=1;i<=m;i++){
        memset(trie,0,sizeof(trie));
        root=1;N=1;
    for(j=1;j<=n;j++){
        if(done[j]==i){
            add(s[j]);
        }
    }
        S=S+N;
        if(N==1) return 0;
        //cout<<N<<" ";

        //cout<<endl;
    }
        return S;
}
    int ans;
void dfs(int x){
    if(x>n){
        int s=calc();
        if(s>maxn){
            maxn=s;
            ans=1;
        }
        else if(s==maxn){
            ans++;
        }
        return;
    }
    int i;
    for(i=1;i<=m;i++){
        done[x]=i;
        dfs(x+1);
    }
}
void init(){
    maxn=0;
    ans=0;
    cin>>n>>m;
    int i;
    for(i=1;i<=n;i++){
        cin>>s[i];
    }
    dfs(1);
    cout<<maxn<<" "<<ans<<endl;
}
int main(){
    freopen("4.in","r",stdin);
    freopen("4.out","w",stdout);
    int T,C;
    cin>>T;
    for(C=1;C<=T;C++){
        cout<<"Case #"<<C<<": ";
        init();
    }
}