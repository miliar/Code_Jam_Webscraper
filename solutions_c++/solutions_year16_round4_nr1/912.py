#include<bits/stdc++.h>
using namespace std;
int n,r,s,p;
string ss;
void dfs(int ii,char ch){
    if(ii==n){
        ss+=ch;
        return;
    }
    if(ch=='P'){
        dfs(ii+1,'P');
        dfs(ii+1,'R');
    }else if(ch=='R'){
        dfs(ii+1,'R');
        dfs(ii+1,'S');
    }else{
        dfs(ii+1,'P');
        dfs(ii+1,'S');
    }
    return;
}
bool ok(){
    int rr=0,_ss=0,pp=0;
    for(int i=0;i<(int)ss.size();i++){
        if(ss[i]=='P')pp++;
        else if(ss[i]=='R')rr++;
        else _ss++;
    }
//    cout<<rr<<" "<<_ss<<" "<<pp<<endl;
//    cout<<r<<" "<<s<<" "<<p<<endl;
    if(rr==r && _ss==s && pp==p)return 1;
    return 0;
}
void _sort(int ii,int jj){
    if(ii+1==jj){
        if(ss[ii]>ss[jj])swap(ss[ii],ss[jj]);
        return;
    }
    int dd=(jj-ii+1)/2;
    _sort(ii,ii+dd-1);
    _sort(ii+dd,jj);
    string x=ss.substr(ii,dd);
    string y=ss.substr(ii+dd,dd);
//    cout<<x<<" "<<y<<endl;
    if(x>y){
        for(int i=0;i<dd;i++){
            swap(ss[ii+i],ss[ii+dd+i]);
        }
    }
    return;
}
int main(){
//    ios_base::sync_with_stdio(0);
//    cin.tie(nullptr);
    freopen("in2","r",stdin);
    freopen("out2","w",stdout);
    int t;
    cin>>t;
    for(int z=1;z<=t;z++){
        cin>>n>>r>>p>>s;
        ss.clear();
        dfs(0,'P');
        _sort(0,ss.size()-1);
//        cout<<ss<<endl;
        string ans="";
        if(ok())ans=ss;
        ss.clear();
        dfs(0,'R');
        _sort(0,ss.size()-1);
//        cout<<ss<<endl;
        if(ok()){
            if(ans=="")ans=ss;
            else ans=min(ans,ss);
        }
        ss.clear();
        dfs(0,'S');
        _sort(0,ss.size()-1);
//        cout<<ss<<endl;
//        cout<<ans<<endl;
        if(ok()){
            if(ans=="")ans=ss;
            else ans=min(ans,ss);
        }
        cout<<"Case #"<<z<<": ";
        if(ans!="")cout<<ans<<"\n";
        else cout<<"IMPOSSIBLE\n";
    }
    return 0;
}
