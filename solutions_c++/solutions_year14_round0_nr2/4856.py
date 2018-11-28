#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define eps 1e-8
int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int T,CASE=0;
    double c,f,x,an,rt,ps,qr,ans;
    cin>>T;
    while(T--){
        cin>>c>>f>>x;
        ps = 2.0;
        rt = x/ps;
        an = c/ps ;
        ps = ps + f;
        qr = x/ps;
        ans = 0;
        while(rt + eps> an+qr){
            //cout<<an<<endl;
            ans = ans + an;
            rt = an + qr;
            rt = x/ps;
            an = c/ps ;
            ps = ps + f;
            qr = x/ps;
        }
        ans = ans + rt;
        //cout<<rt<<endl;
        cout<<"Case #"<<++CASE<<": ";
        printf("%.7lf\n",ans);
    }
}
