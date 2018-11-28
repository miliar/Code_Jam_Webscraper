#include <stdio.h>
#include <vector>
#include <iostream>
#include <stack>
using namespace std;

#define MAX 1000000
int table[MAX+5];
const int vowels[5] = {'a','e','i','o','u'};

void solve(){

    int c;
    int len =0;
    int n;
    while ( (c=getchar()) != ' ' )
        table[len++] = c;
    scanf("%d\n",&n);

    /*
    printf("%d-----------\n",n);
    for (int i=0;i<len;i++)
        printf("%c",table[i]);
    putchar('\n');
    */

    int index = 0;
    long long int res = 0;
    int prev=-1;
    int prev_prev = -1;

    for (int i=0;i<len;i++)
    {
        int j ;
        for ( j=0;j<5;j++)
            if ( vowels[j] == table[i] )
                index = 0,j=6;
            if ( j == 5 ) index++;

        if ( index > n ){
            prev = i -n+1;
           res += ((long long int) (prev - prev_prev)) * ((long long int) (len - i));
           prev_prev = prev; 
        }
        if ( index == n ){
//            printf("%d<---%d\n",len,i);
            prev = i-n+1;

  //          printf("%d---%d\n",prev,prev_prev);
            res += ((long long int) (prev - prev_prev)) * ((long long int) (len-i));

           prev_prev = prev; 
        }
    }

    printf("%lld\n",res);
}

int main(){
    int t;
    scanf("%d\n",&t);
    for (int i=1;i<=t;i++)
    {
        printf("Case #%d: ",i);
        solve();
    }
    return 0;
}
