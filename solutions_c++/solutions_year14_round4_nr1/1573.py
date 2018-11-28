#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>
using namespace std;
#define pb push_back
#define mp make_pair
#define MOD 1000000007
#define EPS (1e-10)
#define lef(x) (x<<1)
#define rig(x) (x<<1)+1
#define PI (2*acos(0.0))

int files[10000];

void solve(){
     int X,S;
     printf(" ");
     scanf("%d %d",&X,&S);
     for (int i=0;i<X;++i){
         scanf("%d",&files[i]);
     }
     sort(files,files+X);
     int ret=0;
     for (int i=0,j=X-1;i<=j;){
         ret++;
         if (i==j){
            break;
         }
         if (files[i]+files[j]<=S){
            i++;
            j--;
         }
         else{
              j--;
         }
     }
     printf("%d\n",ret);
}

int main(){
    int ntest;
    scanf("%d",&ntest);
    for (int test=1;test<=ntest;++test){
        printf("Case #%d:",test);
        solve();
    }
    return 0;
}
