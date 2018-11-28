#include<cstdio>
#include<cstring>
#include<iostream>
#include<cmath>
using namespace std;
typedef long long LL;
const int N=10;
long double r,t;
int main(){
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T,cas=0;scanf("%d",&T);
    while (T--){
        cin>>r>>t;
        long double b=2*r-1,tmp=sqrt(b*b+8*t);
        LL ret=(LL)((sqrt(b*b+8*t)-b)/4);
        printf("Case #%d: ",++cas);
        cout<<ret<<endl;
    }
    return 0;
}
