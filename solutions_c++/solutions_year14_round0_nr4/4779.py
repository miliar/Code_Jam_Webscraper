#include<cstdio>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<climits>
#include<cctype>
#include<iostream>
#include<algorithm>
#include<queue>
#include<vector>
#include<map>
#include<string>
#include<set>
#include<stack>
#define ll long long
#define MAX 1000
#define INF INT_MAX
#define eps 1e-6
#define REP(i,n) for (int i=0; i<n; i++)
#define FOR(i,s,t) for (int i=(s); i<=(t); i++)

using namespace std;


int main(){
    int T,n;
    double a[MAX],b[MAX];
    FILE *fp = fopen("out.txt", "w");
    scanf("%d",&T);
    for (int cas = 1; cas<=T; cas++){
        scanf("%d",&n);
        for (int i=0; i<n; i++)
            scanf("%lf",&a[i]);
        for (int i=0; i<n; i++)
            scanf("%lf",&b[i]);
        sort(a,a+n);
        sort(b,b+n);
       // for (int i=0; i<n; i++)
         //   printf("%lf  %lf\n",a[i],b[i]);  
        int i = 0, j = 0,cnt1 = 0,cnt2 = 0;
        while (i<n && j<n){
            if (a[i] < b[j])
                i++;
            else{
                i++;
                j++;
                cnt1++;
            }
        }
        i = 0;
        j = 0;
        while (i<n &&j <n){
            if (b[j] < a[i])
                j++;
            else{
                i++;
                j++;
                cnt2++;
            }
        }
      //  printf("%d  %d\n",cnt1,n-cnt2);
      fprintf(fp,"Case #%d: %d %d\n",cas,cnt1,n-cnt2);
    }
    return 0;
}
