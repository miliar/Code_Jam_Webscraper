#include <iostream>
#include <cstring>
#include <cstdio>
#include <map>
#include <algorithm>
#include <vector>
#define maxn 10010
#define maxx_N 26
#define INF 0x7fffffff
#define eps 1e-6

using namespace std;
int card[4][4];
int main()
{
    freopen("D-large.in","r",stdin);
    freopen("D-large.out","w",stdout);
    int cas,test=1;
    scanf("%d",&cas);
    while(cas--){
        int n;
        double t;
        vector<double> ken,naomi;
        ken.clear();naomi.clear();
        scanf("%d",&n);
        for(int i=0;i<n;i++){scanf("%lf",&t);ken.push_back(t);}
        for(int i=0;i<n;i++){scanf("%lf",&t);naomi.push_back(t);}
        sort(ken.begin(),ken.end());
        sort(naomi.begin(),naomi.end());
        printf("Case #%d: ",test++);
        int k=0,kk=0;
        vector<double>::iterator it_k,it_n,it_e;
        //for(it_k=ken.begin();it_k!=ken.end();it_k++)printf("%lf ",*it_k);printf("\n");
        //for(it_n=naomi.begin();it_n!=naomi.end();it_n++)printf("%lf ",*it_n);printf("\n");
        it_e = ken.begin();it_k=ken.end()-1;
        for(it_n=naomi.end()-1;it_k>=it_e;){
            //printf("%lf %lf\n",*it_k,*it_n);
            if(*it_k>*it_n){
                k++;
                it_k--;
                it_n--;
            }
            else{
                it_e++;
                it_n--;
            }
        }
        for(it_k=ken.begin();it_k!=ken.end();it_k++){
            it_n = lower_bound(naomi.begin(),naomi.end(),*it_k);
            if(it_n==naomi.end())break;
            kk++;
            naomi.erase(it_n);
        }
        printf("%d %d\n",k,n-kk);
    }
    return 0;
}
