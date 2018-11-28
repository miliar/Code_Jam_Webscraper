#include<iostream>
#include<cstdio>

using namespace std;

void solve(){
    double c,f,x;
    cin>>c>>f>>x;
    double g=2.0;
    double t=0.0;
    double ans=2e9;
    for(int i=1;i<=int(x+1);++i){
        double res=x/g+t;
        ans=min(ans,res);
        t+=c/g;
        g+=f;
    }
    printf("%0.9f\n",ans);//cout<<ans<<endl;
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
