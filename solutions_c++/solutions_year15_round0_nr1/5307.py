#include<bits/stdc++.h>

using namespace std;


int main(void){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);

    int tst;
    cin>>tst;
    for(int ks=1;ks<=tst;ks++){
        int n;
        string s;
        cin>>n>>s;
        int tot=0,ans=0;
        for(int i=0;i<int(s.size());i++){
            int t=s[i]-'0';
            if(t){
                if(tot<i){
                    ans+=i-tot;
                    tot+=t+i-tot;
                }else tot+=s[i]-'0';
            }
        }
        cout<<"Case #"<<ks<<": "<<ans<<endl;

    }

    return 0;
}
