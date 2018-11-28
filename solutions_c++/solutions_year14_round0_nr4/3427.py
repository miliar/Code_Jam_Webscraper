#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <string.h>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
using namespace std;

int T;

int n;

vector<double> Naomi;
vector<double> Ken;

void read(){
     Naomi.clear();
     Ken.clear();
     for (int i=0;i<n;i++){
         double f;
         scanf("%lf",&f);
         Naomi.push_back(f);
         }
     for (int i=0;i<n;i++){
         double f;
         scanf("%lf",&f);
         Ken.push_back(f);
         }
     }

int Real_war_score(){
    int resNaomi=0;
    int l=0;
    int d=n-1;
    for (int i=Naomi.size()-1;i>=0;i--){
        if (Naomi[i]>Ken[d]){
           resNaomi++;
           l++;                  
           } else {
           d--;
           }
        }
    return resNaomi;
    }

int Fake_war_score(){
    int resNaomi=0;
    int l=0;
    int d=n-1;
    for (int i=0;i<Naomi.size();i++){
        if (Naomi[i]>Ken[l]){
           resNaomi++;
           l++;                  
           } else {
           d--;
           }
        }
    return resNaomi;
    }

int main(){
    scanf("%d",&T);
    for (int t=1;t<=T;t++){
        scanf("%d",&n);
        read();
        sort(Naomi.begin(),Naomi.end());
        sort(Ken.begin(),Ken.end());
        printf("Case #%d: %d %d\n",t,Fake_war_score(),Real_war_score());
        }
    return 0;
    }
