#include<bits/stdc++.h>
#define ll long long int
using namespace std;
int main(){
    freopen("output.txt","w",stdout);
    ll t,c,z=0,k,l,r,m;
    char s[1005];
    scanf("%lld",&t);
    while(t--){
            c=0;r=0;m=0;
            cin>>l>>s;
            c+=((int)s[0])-48;
    for(ll i=1;i<=l;i++){
        k=((int)s[i])-48;r=0;
        while(c+r<i){r++;}
        c+=k;c+=r;m+=r;
    }
    cout<<"Case #"<<++z<<": "<<m<<endl;
    }
    return 0;
}
