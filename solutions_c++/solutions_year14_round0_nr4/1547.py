#include <cstdio>
#include <iostream>
#include <cmath>
#include <vector>
#include <cstdlib>
#include <set>
using namespace std;
#define pb push_back

vector<int>naomi,ken;
void solve(){
     int n;
     naomi.clear();
     ken.clear();
     scanf("%d",&n);
     
     double dt;
     for (int i=0;i<n;++i){
         scanf("%lf",&dt);
         naomi.pb((int)(dt*1000000000));
     }
     for (int i=0;i<n;++i){
         scanf("%lf",&dt);
         ken.pb((int)(dt*1000000000));
     }
     sort(naomi.begin(),naomi.end());
     sort(ken.begin(),ken.end());
     set<int>vk;
     set<int>::iterator it;
     int rn,rd;
     
     //normal war
     rn=0;
     for (int i=0;i<n;++i) vk.insert(ken[i]);
     for (int i=0;i<n;++i){
         it = vk.upper_bound(naomi[i]);
         if (it==vk.end()){
            vk.erase(vk.begin());
            rn++;
         }
         else{
              vk.erase(it);
         }
     }
     
     //deceitful war
     rd=0;
     for (int i=0;i<n;++i){
         if (naomi[i]<ken[0]){
            ken.erase(ken.begin()+(n-(1+i)));
         }
         else{
              ken.erase(ken.begin());
              rd++;
         }
     }
     printf("%d %d\n",rd,rn);
}
int main(){
    int ntest;
    scanf("%d",&ntest);
    for (int test=1;test<=ntest;++test){
        printf("Case #%d: ",test);
        solve();
    }
    return 0;
}
