#include<bits/stdc++.h>
using namespace std;
#define LLT long long int


int main()
{
    LLT t,k,c,s;
    scanf("%lld", &t);
    for(int i=1; i<=t;i++) {
        scanf("%lld %lld %lld",&k,&c,&s);
        cout<<"Case #"<<i<<": ";
        if(s<k) {
            cout<<"IMPOSSIBLE"<<endl;
            continue;
        }
        for(LLT j=1;j<=s;j++)
            cout<<j<<" ";
        cout<<endl;
    }
    return 0;
}
