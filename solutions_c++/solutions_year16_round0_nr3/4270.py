
#include<bits/stdc++.h>
using namespace std;
#define pii pair<int,int>
#define fs first
#define sc second
typedef long long ll;
ll pow(ll i , int j){
    ll res = 1;
    for(int k = 0 ; k<j;k++)
        res*=i;
    return res;

}
string tobin(int n , int sz){
    string ans = "1";
    while(n!=0){
        if(n%2)
            ans = "1"+ans;
        else
            ans = "0"+ans;
        n/=2;

    }
    while(ans.size()<sz-1){
        ans = "0"+ans;
    }
    ans = "1"+ans;
    return ans;


}
int main(){
    ios_base::sync_with_stdio(false);cin.tie(0);
        freopen ("file.out","w",stdout);
        freopen ("file.in","r",stdin);
        int n ,m;
        cin>>n;
        cin>>n>>m;
        n-=2;
        cout<<"Case #1:\n";
        for(int k = 0 ; k<(1<<n);k++){
            if(m==0)break;
            vector<int> v;
            bool tr = 1;
            for(int j = 2 ;j<11;j++){
                ll sum = pow((ll)j,n+1)+1;
                for(int f = 0 ;f<n;f++){
                    if(k &(1<<(f)))
                    sum+= pow((ll)j,f+1);
                }
                ll cn = 3;
                if(sum%2==0){
                    v.push_back(2);
                    continue;
                }
                bool fnd = 0;
                while(cn *cn <= sum){
                    if(sum%cn==0){
                        fnd = 1;
                        break;

                    }
                    cn+=2;
                }
                tr&=fnd;
                if(fnd)
                    v.push_back(cn);
                else
                    break;

            }
            if(tr){
                cout<<tobin(k,n+2)<<" ";
                for(int i =0 ;i< v.size();i++)
                    cout<<v[i]<<" ";
                cout<<"\n";
                m--;

            }

        }





//    freopen ("file.out","w",stdout);
//    freopen ("file.in","r",stdin);
//    int t , n ,sol;
//    cin>>t;
//    for(int p = 1 ; p<=t;p++){
//        cin>>n;
//        if(!n){
//            cout<<"Case #"<<p<<": INSOMNIA"<<'\n';
//            continue;
//        }
//        bool dg[10];
//        memset(dg,0 , sizeof dg);
//        int res = n;
//        bool ans =  upd(res,dg);
//        for(int i  = 2 ;i<100;i++){
//            if(ans)break;
//            res = n*i;
//            ans =  upd(res,dg);
//
//        }
//        cout<<"Case #"<<p<<": "<<res<<'\n';
//
//    }
//

    return 0;

}

