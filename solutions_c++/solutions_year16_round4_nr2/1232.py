#include<cstdio>
#include<cstring>
#include<string>
#include<cmath>
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main()
{
    int tn, i, j, n, k, r;
    double p[1000];
    freopen("gcbs.in", "r", stdin);
    freopen("gcbs.out", "w", stdout);
    scanf("%d", &tn);
    for(int tt = 1; tt<=tn;tt++){
        scanf("%d%d",&n,&k);
        for(i=0;i<n;i++)
            scanf("%lf",p+i);
        double ret = 0.0;
        for(i=0;i<(1<<n);i++){
            if(__builtin_popcount(i) == k){
                double np[1000];
                int pc = 0;
                for(j=0;j<n;j++)if(i&(1<<j))
                    np[pc++] = p[j];
                double tmp = 0.0;
                for(j=0;j<(1<<k);j++){
                    if(__builtin_popcount(j) == k/2){
                        double aa = 1.0;
                        for(r=0;r<k;r++){
                            if(j&(1<<r))
                                aa*=np[r];
                            else
                                aa*=(1-np[r]);
                        }
                        tmp += aa;
                    }
                }
                ret = max(ret, tmp);
            }
        }
        cout<<"Case #"<<tt<<": "<<ret<<endl;
    }
}
