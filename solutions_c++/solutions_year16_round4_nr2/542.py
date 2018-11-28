#include <iostream>
#include <iomanip>
#include <fstream>
#include <stdlib.h>
#include <time.h>
#include<cstring>
#include<cstdio>
#include<vector>
#include<string>
#include<algorithm>
#include <limits.h>
#include<cmath>
#include<map>
#include<queue>
#include<set>
using namespace std;

#define N 100005
#define M 100005
#define LL long long

//为自己加油O(∩_∩)O~

const long long  mod =1000000007;
double q[233];
vector<double> v;
bool b[233];
double ans;
double f[233][233];
void suan()
{

    memset(f,0,sizeof(f));
    f[0][1]=v[0];
    f[0][0]=1-v[0];
    for (int j=0;j<v.size();j++){
        for (int k=0;k<=j+1;k++){
            f[j+1][k+1]+=f[j][k]*v[j+1];
            f[j+1][k]+=f[j][k]*(1-v[j+1]);
        }
    }
    int len=v.size();
    //printf("%.9f\n",f[len-1][len/2]);
    ans=max(ans,f[len-1][len/2]);
}
int main()
{
    freopen("out.txt","w",stdout);
    int T;
    scanf("%d",&T);
    int t=T;
    while (T--){
        int n,m;
        scanf("%d%d",&n,&m);
        for (int j=0;j<n;j++) scanf("%lf",&q[j]);
        sort(q,q+n);
        int qu=n-m;
        ans=0;
        for (int j=0;j+qu<=n;j++){
            memset(b,0,sizeof(b));
            for (int k=0;k<qu;k++) b[j+k]=1;
            v.clear();
            for (int k=0;k<n;k++)
                if (!b[k])
                    v.push_back(q[k]);
            suan();
        }
        printf("Case #%d: %.9f\n",t-T,ans);
    }
    return 0;
}








