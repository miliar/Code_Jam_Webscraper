#include <iostream>
#include <fstream>
#include <sstream>
#include <math.h>
#include <cstdio>
#include <cstdlib>
#include <string.h>
using namespace std;


int fun( int x ){
int broj;
broj = 0;

while( x > 0 ){
        x/=2;
        broj++;
            }

return broj-1;
}

int main(){
    ifstream ulazniTok("A-small-attempt1.in");

    int T;

    int i;
    int j;
    int q;
    //char uh;


    FILE *f;
    f = fopen("out.txt", "w");

    ulazniTok >> T;
     //   printf("%d\n",T);
    for( i = 0; i < T ; i++ ){
    int a;
    int b;
    char x;

    ulazniTok >> a;
    ulazniTok >> x;
    ulazniTok >> b;
    //printf("%d: %d %c %d\n",i+1, a,x,b);
    //printf(" %d & %d = %d \n", b, b-1, b&(b-1));
    //fprintf(f, "Case #%d: %d %c %d \n",i+1, a, x, b);
    int prolaz;
    prolaz = b&(b-1);

    if( prolaz == 0 ){

        fprintf(f, "Case #%d: %d\n",i+1, fun(b)-fun(a));
        }

    else fprintf(f, "Case #%d: impossible\n",i+1);
    }






fclose(f);

return 0;

}
