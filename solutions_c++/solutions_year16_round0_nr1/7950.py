#include<bits/stdc++.h>
using namespace std;

#define ll long long
ll a,b,c,i,j,n,m,k,q,t,x,y,z,ans,mnm,mxm;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    scanf(" %lld",&t);
    for(a=1; a<=t; a++) {
        scanf(" %lld",&n);
        if(n==0) printf("Case #%lld: INSOMNIA\n",a);
        else {
        vector<bool>v(11);
        for(b=0; b<10; b++) v[b]=false;
        c=0;m=1;
        while(1) {
            x=n*m;
            z=x;
            while(x>0) {
                y=x%10;
                v[y]=true;
                x/=10;
            }
            m++;
            c=0;
            for(j=0; j<10; j++) {
                if(v[j]) c++;
            }
            if(c==10) {
                printf("Case #%lld: %lld\n",a,z);
                break;
                }
            }
        }
    }
    return 0;
}
