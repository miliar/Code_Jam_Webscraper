// Author : Muhammad Rifayat Samee
// Problem : B
// Algorithm:
#pragma warning (disable : 4786)
#pragma comment(linker, "/STACK:16777216")

#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cctype>
#include<cstring>
#include<algorithm>
#include<string>
#include<set>
#include<vector>
#include<map>
#include<queue>
#include<stack>
#define MAX(a,b) (a>b)?a:b
#define MIN(a,b) (a<b)?a:b
#define INF 987654321
#define pi (2*acos(0.0))
#define eps 1e-12

#ifdef ONLINE_JUDGE
#define i64 long long
#else
#define i64 __int64
#endif

using namespace std;

int main(){

	freopen("B.in","r",stdin);
	freopen("B_large.out","w",stdout);
    double C,rate,F,X;
    int i,n,cases,ct=1;
    scanf("%d",&cases);
    while(cases--){
        scanf("%lf %lf %lf",&C,&F,&X);
        rate = 2;
        double res = 0;
        int mid,l = 0;
        int h = 100000000;
        while(l<h){
            mid = (l+h)/2;
            double r = C + (X*(2+mid*F))/(2+(mid+1)*F);
            if(X+eps<r){
                h = mid-1;
            }
            else{
                l = mid+1;
            }
        }
        for(n=h;;n++){
            double r = C + (X*(2+n*F))/(2+(n+1)*F);
            //printf("%lf %lf\n",X,r);
            if(X+eps<r)break;
        }
        // printf("%d\n",n);
        for(i=0;i<n;i++){
            res = res + (C/(2+i*F));
            //printf("%lf\n",res);
        }
        res = res + (X/(2+i*F));
        //printf("---%d %lf\n",i,2+(i-1)*F);
        printf("Case #%d: %.10lf\n",ct++,res);
    }
	return 0;
}
