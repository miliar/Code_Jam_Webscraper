#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;
int arrayofno[2000];

int main() {
    int testcase,step=0;
    
    int number,i ,j,maximum_part_1,minimum_part_1,summation;
    
    scanf("%d",&testcase) ;
    
    while(testcase--)
	 {
        scanf("%d", &number) ;
        for(i=0;i<number;i++) 
		{
            scanf("%d", &arrayofno[i]) ;
            maximum_part_1 = max(maximum_part_1,arrayofno[i]) ;
        }
        
        minimum_part_1 = maximum_part_1 ;
        
        for(i=1;i<=maximum_part_1;i++) 
		{
            summation=i ;
            for(j=0;j<number;j++)
	 {
                if( arrayofno[j] > i ) {
                    if( arrayofno[j]%i == 0 )
                        summation += (arrayofno[j]/i-1) ;
                    else
                        summation += (arrayofno[j]/i) ;
                }
            }
            minimum_part_1 = min(minimum_part_1,summation) ;
        }
        printf("Case #%d: %d\n", ++step, minimum_part_1) ;
    }
    return 0 ;
}