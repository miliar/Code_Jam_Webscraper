#include <iostream>
#include <cmath>
#include <cstdio>
#include <fstream>

using namespace std;

bool ispowerof2(unsigned int x);
int gcd ( int a, int b );
int main () {
    int t, p, q, minimum;
    scanf("%d", &t);
    for(int CASE=1; CASE<=t; CASE++){
        scanf("%d/%d",&p,&q); //Monitor
        bool small=true;
        int GCD = gcd(p,q);
        p/=GCD;
        q/=GCD;
        if(ispowerof2(q)){
            if(p==1){
                int log=log2(q);
                printf("Case #%d: %d\n", CASE, log);
            }
            else{
                double a=p;
                a/=q;
                for(int i=1; i<=40; i++){
                    if(a>(1/pow(2, i))){
                        small=false;
                        printf("Case #%d: %d\n", CASE, i);
                        break;
                    }
                }
                if(small)
                    printf("Case #%d: impossible\n", CASE);
            }
        }
        else {
            printf("Case #%d: impossible\n", CASE);
        }
    }
};

bool ispowerof2(unsigned int x) {
   return x && !(x & (x - 1));
}
int gcd ( int a, int b )
{
  int c;
  while ( a != 0 ) {
     c = a; a = b%a;  b = c;
  }
  return b;
}
