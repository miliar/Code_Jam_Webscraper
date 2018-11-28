#include<stdio.h>
#include <cstdio>
using namespace std ;
int data[1200] ;
int main() {
    int t=1,tc;
    int n;
	int max,min;
	int total ;
    scanf("%d", &tc) ;
    while( t<=tc ) {
        scanf("%d", &n) ;
        for(int i = 0 ; i < n ; i++) {
            scanf("%d", &data[i]);
            if(data[i]>max)
            	max = data[i];
        }
        min = max;
        for(int i = 1 ; i <= max ; i++) {
            total = i ;
            for(int j = 0 ; j < n ; j++) {
                if( data[j] > i ) {
                    if( data[j]%i == 0 )
                        total += (data[j]/i-1);
                    else
                        total += (data[j]/i);
                }
            }
            if(total<min)
            	min=total;
        }
        printf("Case #%d: %d\n", t, min) ;
        t++;
    }
    return 0 ;
}

