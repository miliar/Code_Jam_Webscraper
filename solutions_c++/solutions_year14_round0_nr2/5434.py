#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstdlib>

using namespace std; 

int main(){
    int nt;
    scanf(" %d",&nt);
    for(int t = 1 ; t <= nt ; t++){
        double c,f,x;
        scanf(" %lf %lf %lf",&c,&f,&x);
        
        double ans = x/2;        
        double taxa = 2.0;
        double tempo = 0.0;
        double accu = 0;
        while(accu < ans){
            ans = min(ans, accu + x/taxa);
            accu += c/taxa;
            taxa += f;           
        }
        printf("Case #%d: %.15lf\n",t,ans);
        
    }
    return 0;
}
