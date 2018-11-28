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

int ar[100],tmp[100];
string str1[100];

int vis[100],True;
int grp[100][100],cnt[100],nC;
int tot;
int poss[1027];
int hi[100];

int fact;

bool cmp(const int &s1,const int &s2)
{
    return str1[s1]>str1[s2];
}

Long start[1000],end[1000],c5,have[1000];

int main()
{
    int tst,cas;
    freopen("B2.in","rt",stdin);
    freopen("B2.out","wt",stdout);
    scanf("%d",&tst);
    Long n,p;

    for(cas=1;cas<=tst;cas++) {

        scanf("%lld%lld",&n,&p);
        Long N = (1LL<<n);

        Long jog = (1LL<<n)/2LL;

        Long prv = 1;

        Long cur = 0;
        Long p5 = 0;
        c5 = 0;

        while(cur!=N) {
            if(cur+prv<=N) {

                start[c5] = cur;
                end[c5] = cur + prv - 1;
                have[c5] = p5;
                //for(int i=cur;i<cur+prv;i++) poss[i] = p5 ;
                c5++;

            }
            else {
                prv = 1;
                start[c5] = cur;
                end[c5] = cur + prv - 1;
                have[c5] = p5;
                c5++;
                //for(int i=cur;i<cur+prv;i++) poss[i] = p5 ;


            }
            cur = (cur + prv);
            p5 = p5 + jog;
            prv = prv*2LL;
            jog = jog/2LL;



        }

        Long ans1,ans2;

        for(int i=0;i<c5;i++) {
            if(have[i]<p) ans1 = end[i];
            if(start[i]<=p-1 && end[i]>=p-1) ans2 = have[i];
        }

        printf("Case #%d: %lld %lld\n",cas,ans1,ans2);


        /*for(int i=0;i<N;i++) {
            if(poss[i]<p) ans1 = i;

        }
        ans2 = poss[p-1];
        printf("Case #%d: %d %d\n",cas,ans1,ans2);*/





    }
    return 0;
}
