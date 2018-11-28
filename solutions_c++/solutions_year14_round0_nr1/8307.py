#include<iostream>
#include<cstdio>

using namespace std;
int a[17],b[17];
void solve(){
    int x1,x2;
    cin>>x1;
    for(int i=1;i<=4;++i)for(int j=1;j<=4;++j){int x;cin>>x;a[x]=i;}
    cin>>x2;
    for(int i=1;i<=4;++i)for(int j=1;j<=4;++j){int x;cin>>x;b[x]=i;}
    int ans=-1;
    bool was=0,many=0;
    for(int i=1;i<=16;++i)if(a[i]==x1 && b[i]==x2){if(!was){was=1;ans=i;}else many=1;}
    if(many)cout<<"Bad magician!";
    else if(!was)cout<<"Volunteer cheated!";
    else cout<<ans;
    cout<<endl;
}

int main(){
    //freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    for(int i=1;i<=t;++i){
        cout<<"Case #"<<i<<": ";solve();
    }

    return 0;
}
