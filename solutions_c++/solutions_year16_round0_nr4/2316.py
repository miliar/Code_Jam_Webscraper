#include<bits/stdc++.h>
using namespace std;


int main()
{
    freopen("A.in","r",stdin),freopen("A1.out","w",stdout);
    int t;
    cin>>t;

    for(int cs=1;cs<=t;cs++) {
        long long k,c,s;
        cin>>k>>c>>s;
        printf("Case #%d:",cs);
        for(int i=1;i<=k;i++) printf(" %d",i);
        printf("\n");
    }

    return 0;
}
