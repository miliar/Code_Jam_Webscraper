#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <limits.h>
int arr[2001005];

int main()
{
    freopen("C-large-2.in","r",stdin);
    freopen("ouput.txt","w",stdout);
    int cases;
    double m , n ;

    for(int i = 0 ; i < 2001005 ; i++)
    arr[i] = 0 ;

    arr[1] = 1 ;
    arr[2] = 1 ;
    arr[3] = 1 ;
    arr[11] = 1 ;
    arr[22] = 1 ;
 arr[101] = 1 ;
arr[111] = 1 ;
arr[121] = 1 ;
arr[202] = 1 ;
arr[212] = 1 ;

arr[1001] = 1 ;
arr[1111] = 1 ;
arr[2002] = 1 ;

arr[10001] = 1 ;
arr[10101] = 1 ;
arr[10201] = 1 ;
arr[11011] = 1 ;
arr[11111] = 1 ;
arr[11211] = 1 ;
arr[20002] = 1 ;
arr[20102] = 1 ;

arr[100001] = 1 ;
arr[101101] = 1 ;
arr[110011] = 1 ;
arr[111111] = 1 ;
arr[200002] = 1 ;

arr[1000001] = 1 ;
arr[1001001] = 1 ;
arr[1002001] = 1 ;
arr[1010101] = 1 ;
arr[1011101] = 1 ;
arr[1012101] = 1 ;
arr[1100011] = 1 ;
arr[1101011] = 1 ;
arr[1102011] = 1 ;
arr[1110111] = 1 ;
arr[1111111] = 1 ;
arr[2000002] = 1 ;
arr[2001002] = 1 ;


    for(int i = 2 ; i <  2001005 ; i++)
    arr[i] = arr[i] + arr[i-1] ;

    scanf("%d",&cases);

    for(int c = 1 ; c <= cases ; c++)
    {

        scanf("%lf%lf",&m,&n);
    //    printf("%lf %lf \n",m,n) ;
        int aaa = sqrt(m);
        int bbb = sqrt(n);

        if(aaa >= 2001004 ) aaa = 2001004 ;
        if(bbb >= 2001004 ) bbb = 2001004 ;
        printf("Case #%d: %d\n",c,arr[bbb]-arr[aaa-1] );
    }

    return 0 ;
}
