#include<iostream>
using namespace std;

int a[4][4],b[4][4];

int main(){
	freopen("B-large.in","r",stdin);
	freopen("pa.txt","w",stdout);
    double buy, frequency, target, totaltime,rate;
    int cases;
	scanf("%d",&cases);
	for(int c=1 ; c<=cases ; c++){
		
        scanf("%lf%lf%lf",&buy, &frequency, &target);
        totaltime=0.0;
        rate=2.0;
        
        while (1) {
           
            if((buy/rate)+(target/(rate+frequency))<(target/rate)){
                totaltime+=buy/rate;
                rate+=frequency;
            }
               else{
                  
                   totaltime+=target/rate;
                   break;
               }

	}
        printf("Case #%d: %lf\n",c,totaltime);

    }
}
