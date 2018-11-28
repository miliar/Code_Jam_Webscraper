#include <cstdio>
#include <algorithm>
using namespace std;

int c=0;
void run(){
    int X,R,C,rm;
    scanf ("%d%d%d",&X,&R,&C);
    if (R<C) swap(R,C);
    if (X==1){
        printf ("Case #%d: GABRIEL\n",c);
        return;
    }
    if (X>=7){
        printf ("Case #%d: RICHARD\n",c);
        return;
    }
    if (R*C<X){
        printf ("Case #%d: RICHARD\n",c);
        return;
    }
    if (R<X&&C<X){
        printf ("Case #%d: RICHARD\n",c);
        return;
    }
    if (((R*C)%X)!=0){
        printf ("Case #%d: RICHARD\n",c);
        return;
    }
    /*if ((X==3||X==4)&&(R==1||C==1)){
        printf ("Case #%d: RICHARD\n",c);
        return;
    }
    if ((X==5||X==6)&&(R<3||C<3)){
        printf ("Case #%d: RICHARD\n",c);
        return;
    }*/
    /*if ((X==3)&&(R<4||C<4)){
        printf ("Case #%d: RICHARD\n",c);
        return;
    }
    if ((X==3)&&(R<4||C<4)){
        printf ("Case #%d: RICHARD\n",c);
        return;
    }*/
    //R longer than C
    if (X>3&&((R<3)||(C<2))){
        printf ("Case #%d: RICHARD\n",c);
        return;
    }
    if (X>4&&((R<4)||(C<3))){
        printf ("Case #%d: RICHARD\n",c);
        return;
    }
    if (R<X||C<X-1){
        printf ("Case #%d: RICHARD\n",c);
        return;
    }
    printf ("Case #%d: GABRIEL\n",c);
    return;
}

int main(){
    freopen ("D-small-attempt15.in","r",stdin);
    freopen ("outd2.txt","w",stdout);
    int T;
    scanf ("%d",&T);
    while (T--){
        c++;
        run();
    }


return 0;
}
