#include <cstdio>
#include <iostream>
using namespace std;
 
int main(){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    double tant,tac,farms,x,p,c,f;
    bool boo;
    scanf("%d",&t);
    for (int i=1;i<=t;i++){
        scanf("%lf %lf %lf",&c,&f,&x);
        boo = true;
        p = 2;
        tant = x/2;
        farms = 0;
        while(boo){
            farms = farms + (c/p);
            p = p + f;
            tac = farms + (x/p);
            if (tant <= tac)
                boo = false;
            else
                tant = tac;
            
        }
        printf("Case #%d: %.7lf\n", i, tant);
    }
    
}
