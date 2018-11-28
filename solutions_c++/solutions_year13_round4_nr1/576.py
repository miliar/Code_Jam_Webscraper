#include <stdio.h>
#include <string.h>
#include <vector>
#include <queue>
#include <algorithm>
#include <iostream>
#include <map>
#include <string>
#include <math.h>
#include <stack>
#include <list>

#define SZ 10000002
#define EPS 1e-10
#define pb push_back
#define pi (acos(-1.0))


using namespace std;

typedef long long Long;

const Long mod = 1000002013LL;
int n,m,start[107],end[107],p[107];


int ps[10005],entry[10005];
int vl[10005];
int tp;

Long calc(Long dd)
{
    if(dd<=0) return 0;
    Long ret = ( n*dd - (dd*(dd-1))/2 )%mod;
    return ret;
}

Long find(Long dd)
{
    if(dd<=0) return 0;
    Long ret = ( n*dd - (dd*(dd-1))/2 );
    return ret;
}

int main()
{
    int tst,cas;
    freopen("A.in","rt",stdin);
    freopen("A.out","wt",stdout);
    scanf("%d",&tst);


    for(cas=1;cas<=tst;cas++) {
        scanf("%d%d",&n,&m);
        tp = 0;

        Long prev = 0;
        for(int i=0;i<m;i++) {
            scanf("%d%d%d",&start[i],&end[i],&p[i]);
            prev = ( prev + calc(end[i]-start[i])*p[i] ) %mod;
            for(int j=0;j<p[i];j++) ps[tp++] = i , entry[tp-1] = start[i],vl[tp-1] = -1;
        }

        for(int i=0;i<tp;i++) {
            for(int j=i+1;j<tp;j++) {
                if(entry[i]<entry[j]) swap(entry[i],entry[j]),swap(ps[i],ps[j]);
            }
        }

       // cout<<prev<<endl;



        Long ans = 0;
        Long t1,t2;

        for(int i=1;i<=n;i++) {
            for(int j=0;j<tp;j++) {
                //if(i==3) cout<<start[ps[j]]<<" "<<end[ps[j]]<<endl;
                if(start[ps[j]]<=i&&end[ps[j]]>=i) vl[j] = 1;
                else vl[j] = -1;
            }
            for(int j=0;j<tp;j++) {
                if(vl[j]!=-1) {

                    for(int k=j+1;k<tp;k++) {
                        if(vl[k]!=-1) {
                           // cout<<"here"<<endl;
                            t1 = find(end[ps[j]] - entry[j]) + find(end[ps[k]]-entry[k]);
                            t2 = find(end[ps[j]] - entry[k]) + find(end[ps[k]]-entry[j]);
                            if(t1>t2) {
                                swap(entry[j],entry[k]);
                            }
                        }
                    }
                }
            }






        }


        for(int i=0;i<tp;i++) {
            //cout<<ps[i]<<" "<<entry[i]<<endl;
            ans = (ans + calc(end[ps[i]]-entry[i]))%mod;
        }
        Long save = prev - ans;
        save = (save%mod + mod)%mod;
        //cout<<ans<<endl;

        printf("Case #%d: %lld\n",cas,save);




    }
    return 0;
}
