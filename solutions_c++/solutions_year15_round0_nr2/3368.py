#include<stdio.h>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<string.h>
#include<iostream>
#include<stdlib.h>
#include<math.h>
#include<algorithm>
#define eps 1e-7
using namespace std;

int gcd(int a,int b) { return b==0?a:gcd(b,a%b); }
int Min(int a,int b) { return a<b?a:b; }
int Max(int a,int b) { return a>b?a:b; }



int a[1200] ;
int main() {
    int t , step = 0 ;
    int n , i , j , max1 , min1 , sum ;

		freopen("B-large.in","r",stdin);
		freopen("B-large.out","w",stdout);

    scanf("%d", &t) ;
    while( t-- ) {
        scanf("%d", &n) ;
        for(i = 0 ; i < n ; i++) {
            scanf("%d", &a[i]) ;
            max1 = Max(max1,a[i]) ;
        }
        min1 = max1 ;
        for(i = 1 ; i <= max1 ; i++) {
            sum = i ;
            for(j = 0 ; j < n ; j++) {
                if( a[j] > i ) {
                    if( a[j]%i == 0 )
                        sum += (a[j]/i-1) ;
                    else
                        sum += (a[j]/i) ;
                }
            }
            min1 = Min(min1,sum) ;
        }
        printf("Case #%d: %d\n", ++step, min1) ;
    }
    return 0 ;
}
