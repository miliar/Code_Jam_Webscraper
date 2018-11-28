#include<bits/stdc++.h>
using namespace std;
long long t,l,n,a;
set <int> s;
void get_num(long long n){
    while(n>0){
        s.insert(n%10);
        n/=10;
    }
}
int main(){
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    cin>>t;
    for(l=0;l<t;l++){
        cin>>n;
        cout<<"Case #"<<l+1<<": ";
        if (n==0) cout<<"INSOMNIA"<<endl; else {
            a=n;
            s.clear();
            while(s.size()<10){
                get_num(n);
                n+=a;
            }
            cout<<n-a<<endl;
        }
    }
    return 0;
}
