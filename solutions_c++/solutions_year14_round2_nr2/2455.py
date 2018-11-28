#include <cstring>
#include <cstdio>
#include <iostream>

using namespace std;

int main()
{
    freopen("a.in","r",stdin);
    freopen("out.txt","w",stdout);
    long long int cnt,j,a,b,n,i,t,p=0,k;
    scanf("%lld", &t);
    while(t--) {
        p++;
        cnt=0;
        scanf("%lld", &a);
        scanf("%lld", &b);
        scanf("%lld", &k);
        for(i=0;i<a;i++) {
            for(j=0;j<b;j++) {
                if((i&j)<k)
                    cnt++;
            }
        }
        cout<<"Case #"<<p<<": "<<cnt<<endl;
    }
    return 0;
}
