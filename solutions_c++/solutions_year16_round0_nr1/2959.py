#include<bits/stdc++.h>
using namespace std;

long long a,b,c;
bool mark[10];

void dem(long long a){
    while (a){
        c+=mark[a%10];
        mark[a%10]=0;
        a/=10;
    }
}

main(){
    //freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    for (int i=1;i<=t;i++){
        cin>>a;
        c=0;
        memset(mark,1,sizeof(mark));
        dem(a);
        b=a;
        for (int k=0;k<10000;k++){
            if (c==10){
                cout<<"Case #"<<i<<": "<<a<<endl;
                break;
            }
            a+=b;
            dem(a);
        }
        if (c!=10) cout<<"Case #"<<i<<": INSOMNIA\n";
    }
}
