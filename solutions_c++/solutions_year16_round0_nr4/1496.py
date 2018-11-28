#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

int k,c,s;
int main()
{
    int T;
    cin>>T;
    for(int tcases=1;tcases<=T;++tcases){
        printf("Case #%d:",tcases);
        cin>>k>>c>>s;
        if(k==s)
            for(int i=1;i<=k;++i) cout<<" "<<i;
        cout<<endl;
    }
    return 0;
}
