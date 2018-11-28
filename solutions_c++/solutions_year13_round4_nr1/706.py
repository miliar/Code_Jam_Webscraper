#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
const int M=1000002013;
struct st{
    long long t,p;
    int tp;
}a[10000],s[10000];
bool cmp(const struct st& a,const struct st& b){
    return a.t<b.t || (a.t==b.t && a.tp<b.tp);
}
int main()
{
    freopen("A2.in","r",stdin);
    freopen("A2.out","w",stdout);
    int T;
    cin>>T;
    for(int cas=1; cas<=T; cas++){
        long long n,m,e,o,p;
        cin>>n>>m;
        int i;
        long long cost=0;
        for (i=0; i<m; i++) {
            cin>>o>>e>>p;
            cost = (cost+((e-o)*(n+n-(e-o)+1)/2%M)*p%M)%M;
            a[2*i].p=a[2*i+1].p=p;
            a[2*i].t=o,a[2*i+1].t=e;
            a[2*i].tp=0,a[2*i+1].tp=1;
        }
        sort(a,a+2*m,cmp);
//        for (i=0; i<2*m; i++) cout<<a[i].tp<<' '<<a[i].t<<' '<<a[i].p<<endl;
        s[1] = a[0];
        int top=1;
        i=1;
        long long cost2=cost;
        cost=0;
        while (i<2*m){
            if (a[i].tp==0) s[++top]=a[i];
            else{
                while (a[i].p>0){
                    long long p = min(a[i].p, s[top].p), e=a[i].t,o=s[top].t;
//                    cout<<p<<' '<<s[top].p<<endl;
                    cost = (cost+((e-o)*(n+n-(e-o)+1)/2%M)*p%M)%M;
                    a[i].p-=p,s[top].p-=p;
                    if (s[top].p==0) top--;
                }
            }
            i++;
        }
        cout<<"Case #"<<cas<<": "<<(cost2-cost+M)%M<<endl;
    }
    return 0;
}
