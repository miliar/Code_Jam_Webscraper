#include <cstdio>
#include <cstring>
#include <algorithm>
#include<iostream>
using namespace std;
int arrayofno[2000];
 
int main() {
    int t,k=0;
 
    int th,i ,j,max1,min1,ans;
 
    cin>>t;
 
    while(t--)
	 {
        scanf("%d", &th) ;
        for(i=0;i<th;i++) 
		{
            scanf("%d", &arrayofno[i]) ;
            max1 = max(max1,arrayofno[i]) ;
        }
 
        min1 = max1;
 
        for(i=1;i<=max1;i++) 
		{
            ans=i ;
            for(j=0;j<th;j++)
	 {
                if( arrayofno[j] > i ) {
                    if( arrayofno[j]%i == 0 )
                        ans += (arrayofno[j]/i-1) ;
                    else
                        ans += (arrayofno[j]/i) ;
                }
            }
            min1 = min(min1,ans) ;
        }
        printf("Case #%d: %d\n", ++k, min1) ;
    }
    return 0 ;
}