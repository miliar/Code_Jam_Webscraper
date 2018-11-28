#include<bits/stdc++.h>
using namespace std;

int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int test;
    int cases=0;
    for(scanf("%d",&test);test>0;--test){
        int n;
        double A[1010],B[1010];
        scanf("%d",&n);
        for(int i=0;i<n;++i) scanf("%lf",&A[i]);
        for(int i=0;i<n;++i) scanf("%lf",&B[i]);
        sort(A,A+n);
        sort(B,B+n);
        int res1=0;
        int res2=0;
        int k=n-1;
        int j=0;
        for(int i=n-1;i>=j;){
            if(A[i]>B[k]){ --i; ++res1;}
            else  ++j;
            --k;
        }
        bool taken[1010];
        memset(taken,true,sizeof taken);
        for(int i=0;i<n;++i){
            bool tmp=false;
            for(int j=0;j<n;++j) if(taken[j] && B[j]>A[i]){ taken[j]=false; ++res2;  tmp=true; break;}
            if(!tmp) for(int j=0;j<n;++j) if(taken[j]){ taken[j]=false; break;}
        }
        res2=n-res2;
        printf("Case #%d: %d %d\n",++cases,res1,res2);
    }
    return 0;
}
