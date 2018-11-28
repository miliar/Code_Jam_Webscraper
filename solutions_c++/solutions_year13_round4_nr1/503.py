#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <set>
#include <vector>
#include <cmath>
#include <queue>
using namespace std;
typedef long long LL;
const int N = 10009;
const int inf=1000000000;//1e9
const int mod =1000002013;
int a[N],b[N],p[N];
int overlap(int i,int j){
    if (a[i]>=a[j]&&b[i]<=b[j]) return 0;
    if (a[j]>=a[i]&&b[j]<=b[i]) return 0;
    return (a[i]>=a[j]&&a[i]<=b[j]&&b[i]>b[j])||(a[j]>=a[i]&&a[j]<=b[i]&&b[j]>b[i]);
}
int emp(int i){
    return a[i]==b[i];
}
int main(){
    int T,n,m;
    freopen("A-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>T;
    for (int t=1;t<=T;t++){
        LL ans=0;
        cin>>n>>m;
        for (int i=0;i<m;i++){
            cin>>a[i]>>b[i]>>p[i];
        }
        //int cnt=0;
        while (1){
                int find=false;
        for (int i=0;i<m;i++){
            for (int j=0;j<m;j++) if (i!=j)
            if (!emp(i)&&!emp(j))
            if(overlap(i,j))
            {
                //if (!overlap(i,j)) continue;
               // cout<<i<<" "<<j<<endl;
                find=true;
                int minc=min(p[i],p[j]);
                if (p[i]>p[j]){
                    a[m]=a[i];
                    b[m]=b[i];
                    p[m]=p[i]-p[j];
                    m++;
                }else if (p[i]<p[j]){

                    a[m]=a[j];
                    b[m]=b[j];
                    p[m]=p[j]-p[i];
                    m++;
                }
                LL first=max(a[i],a[j])-min(a[i],a[j]);
               // LL second=min(b[i],b[j])-max(a[i],a[j]);
                LL num=max(b[i],b[j])-min(b[i],b[j]);
                ans+=1LL*minc*first%mod*num%mod;
               // cout<<first<<" "<<num<<endl;
                int ai=a[i],bi=b[i],aj=a[j],bj=b[j];
                a[i]=max(ai,aj);
                b[i]=min(bi,bj);
                p[i]=minc;

                a[j]=min(ai,aj);
                b[j]=max(bi,bj);
                p[j]=minc;
            }
        }
        if (!find) break;
        //cnt++;
       // if (cnt>10) break;
        }
        //for (int i=0;i<m;i++)
         //   cout<<a[i]<<" "<<b[i]<<" "<<p[i]<<endl;
        cout<<"Case #"<<t<<": "<<ans<<endl;
    }
}
