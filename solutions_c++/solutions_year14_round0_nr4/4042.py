#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <deque>
using namespace std;

int main() {
   freopen ("input.txt","r",stdin);
   freopen ("output.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for (int k=1;k<=t;++k){
        printf("Case #%d: ",k);
        int n;
        cin>>n;
        vector <int> naomi;
        vector <int> ken;
        deque <int> na;
        deque <int> ke;
        int war;
        int dwar;
        war=dwar=0;
       
        for (int i=0;i<n;++i){
            double f;
            scanf("%lf",&f);
            naomi.push_back(int(100000*f+0.000001));
           
        }
       
        for (int i=0;i<n;++i){
            double f;
            scanf("%lf",&f);
            ken.push_back(int(100000*f+0.000001));
           
        }
       
        sort (ken.begin(),ken.end());
        sort (naomi.begin(),naomi.end());
       
        for (int i=0;i<n;++i){
            ke.push_back(ken[i]);
            na.push_back(naomi[i]);
        }
       
       
        while (!na.empty()){
            int nao,kef;
            nao=na.back();
            kef=ke.back();
           
            if (nao>kef){
                war++;
                na.pop_back();
                ke.pop_front();
            }else{
                ke.pop_back();
                na.pop_back();
            }
        }
       
        for (int i=0;i<n;++i){
            na.push_back(naomi[i]);
            ke.push_back(ken[i]);
        }
       
        while (!na.empty()){
            int nao,kerf;
            nao=na.front();
            kerf=ke.front();
           
            if (na>ke){
                dwar++;
                na.pop_front();
                ke.pop_front();
            }else{
                na.pop_front();
                ke.pop_back();
            }
        }
        printf("%d %d\n",dwar,war);
    }
   
    return 0;
}
