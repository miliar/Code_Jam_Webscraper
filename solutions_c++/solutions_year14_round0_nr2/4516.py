#include <iostream>
#include <cstdio>

using namespace std;

int main (){

    double res, total, F, persec, casa, ant_casa, ant_total, actual_casa, actual_total;
    int T;
    
    scanf("%d", &T);
    
    for (int i=0;i<T;i++){
        
        cin>>casa;
        cin>>F;
        cin>>total;
        persec=2;
        res=0;
        
        ant_total=total/persec;
        ant_casa=casa/persec;
        res=ant_casa;
            while (1){
                  
                persec+=F;
                
                actual_casa = casa/persec;
                actual_total = total/persec + res;
                res=res+actual_casa;
                
                if (ant_total<actual_total)
                   break;
                
                ant_total=actual_total;
                ant_casa=actual_casa;
                
                }
        printf("Case #%d: %0.7lf\n", i+1, ant_total);
        
        }
        
return 0;
    }
