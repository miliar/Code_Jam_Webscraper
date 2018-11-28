#include <cstdio>
using namespace std;

void solve (int test){
     double c,f,x;
     double rate = 2, sol=0;
     
     scanf ("%lf%lf%lf",&c,&f,&x);
     
     double t1, t2;
     
     for (int i=0;1;++i){
         t1 = x/rate;
         t2 = c/rate + c/f;
         if ( t1 < t2 ){
            sol += t1;
            break;
         }
         sol += c/rate;
         rate += f;
     }
     
     printf ("Case #%d: %.9lf\n",test,sol);
     
     return;
}

int main (){
    int t;
    scanf ("%d",&t);
    for (int i=0;i<t;++i){
        solve ( i+1 );
    }
    return 0;
}
