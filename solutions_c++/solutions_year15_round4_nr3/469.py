#include<bits/stdc++.h>
#define next sled
#define pb push_back
const int N=120000;
using namespace std;
string st,s;
vector<string> v[201];
vector<int> c[201];
void make(int e){
    st="";
    for(int i=0;i<s.size();++i){
        if(s[i]==' '){
            v[e].pb(st);
            st="";
        }else st+=s[i];
    }
    v[e].pb(st);
}
int anse;
struct bohr{
    int next[26];
    int num;
};
vector<bohr> t;
bohr root;
int ls;
int sz,n,ans,f1[N],f2[N];
void add(string s){
    int v=0;
    for(int i=0;i<s.size();++i){
        if(t[v].next[s[i]-'a'])v=t[v].next[s[i]-'a'];
        else {
            t.pb(root);
            ++sz;
            t[v].next[s[i]-'a']=sz;
            v=sz;
        }
    }
    ls=v;
}
void go(int x){
    if(x>n){
        if(ans<anse){
      //      for(int j=3;j<=n;++j)
     //           ee[j]=ep[j];
            anse=ans;
        }
      /*  cout<<ans<<endl;
        for(int i=3;i<=n;++i)
            cout<<ep[i]<<' ';
        cout<<endl;
        */
        return;
    }
    for(int i=0;i<v[x].size();++i){
        if(f1[c[x][i]]==0&&f2[c[x][i]]!=0)++ans;
        ++f1[c[x][i]];
    }
   // cout<<x<<"  is "<<1<<endl;
    //ep[x]=1;
    go(x+1);
    for(int i=0;i<v[x].size();++i){
        if(f1[c[x][i]]==1&&f2[c[x][i]]!=0)--ans;
        --f1[c[x][i]];
    }

    for(int i=0;i<v[x].size();++i){
        if(f1[c[x][i]]!=0&&f2[c[x][i]]==0)++ans;
        ++f2[c[x][i]];
    }
   // cout<<x<<" is "<<2<<endl;
   // ep[x]=2;
    go(x+1);
    for(int i=0;i<v[x].size();++i){
        if(f1[c[x][i]]!=0&&f2[c[x][i]]==1)--ans;
        --f2[c[x][i]];
    }
}
int tek1;
main(){
    cin.tie(0);ios_base::sync_with_stdio(0);
    freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
    cin>>tek1;
    for(int tt=1;tt<=tek1;++tt){
     cout<<"Case #"<<tt<<": ";
      t.pb(root);
      sz=0;
      cin>>n;
      getline(cin,s);
      for(int i=1;i<=n;++i){
        v[i].clear();
        c[i].clear();
         getline(cin,s);
        // cout<<s<<endl;
         make(i);
         for(int j=0;j<v[i].size();++j)
            add(v[i][j]),c[i].pb(ls);
      }
      for(int i=0;i<v[1].size();++i)
        ++f1[c[1][i]];
      for(int i=0;i<v[2].size();++i){
        if(f1[c[2][i]]!=0&&f2[c[2][i]]==0)++ans;
        ++f2[c[2][i]];
      }
      anse=1e9;
      go(3);
      cout<<anse;
      cout<<"\n";
      ans=0;
      t.clear();
      for(int i=0;i<=sz;++i)
        f1[i]=f2[i]=0;
    }

}
