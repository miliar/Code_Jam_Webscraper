#include<bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false);
    freopen("A5.in","r",stdin);
    freopen("output4.txt","w",stdout);
    cin.tie(0);
    int t,k=1;
    cin>>t;
    while(t--){
        long long n;
        set<int> mset;
        mset.insert(0);
        mset.insert(1);
        mset.insert(2);
        mset.insert(3);
        mset.insert(4);
        mset.insert(5);
        mset.insert(6);
        mset.insert(7);
        mset.insert(8);
        mset.insert(9);
        cin>>n;
        cout<<"Case #"<<k<<": ";
        if(n==0)
            cout<<"INSOMNIA\n";
        else{
            long long f=1,k1=n,k2=n;
            while(!mset.empty()){
                k1*=f;
                k2=k1;
                while(k1&&!mset.empty()){
                    mset.erase(k1%10);
                    k1/=10;
                }
                f++;
                k1=n;
            }
            cout<<k2<<"\n";
        }
        k++;
    }
    return 0;
}
