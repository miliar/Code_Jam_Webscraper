#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstdlib>
#include <cmath>

using namespace std; 

#define EPS 1e-8

#define MAXN 1010

int cmp(double a, double b){
    if(fabs(a - b) < EPS) return 0;
    if(a > b) return 1;
    return -1;    
}

double va[MAXN],vb[MAXN];

int main(){
    int nt;
    scanf(" %d",&nt);
    int n;
    for(int t = 1 ; t <= nt ; t++){
        scanf(" %d",&n);
        for(int i = 0 ; i < n ; i++) scanf(" %lf\n",&va[i]);
        for(int i = 0 ; i < n ; i++) scanf(" %lf\n",&vb[i]);
        sort(va,va+n);
        sort(vb,vb+n);
       
        
        //~ for(int i = 0 ; i < n ; i++) printf(" %.3lf",va[i]);
        //~ printf("\n");
        //~ for(int i = 0 ; i < n ; i++) printf(" %.3lf",vb[i]);
        //~ printf("\n");
        
        
        int pts1 = 0;
        int pts2 = 0;        
        int it1 = 0, it2 = 0;
        while(it1 < n && it2 < n){
            //~ printf("<< %lf %lf >>\n",va[it1],vb[it2]);
            if(cmp(va[it1],vb[it2]) >= 0) it2++,it1++,pts2++;
            else it1++;            
        }
        it1 = n - 1;
        int ini2 = 0;
        int fim2 = n - 1;
        while(ini2 <= fim2){
            if(cmp(va[it1],vb[fim2]) >= 0){
                ini2++;
                pts1++;
                it1--;
            }
            else{
                fim2--;
                it1--;
            }
        }
        printf("Case #%d: %d %d\n",t,pts2,pts1);
    
    }
    return 0;
}
