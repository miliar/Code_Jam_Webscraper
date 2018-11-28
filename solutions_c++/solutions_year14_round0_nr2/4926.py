#include<iostream>
#include<cstdio>
using namespace std;

int main(){
    int t,index=1;
    cin>>t;
    while(t--){
        long double c,f,x,cal1,cal2,sum1=0.0,sum2=0.0,farm=0.0;
        long double incre_rate=2;
        cin>>c>>f>>x;
        cal2=x/incre_rate;
        sum2+=cal2;
        //incre_rate1+=f;
        cal1=c/incre_rate;
        sum1+=cal1+x/(incre_rate+f);
        while(sum1<sum2){
            sum2=sum1;
            sum1=0;
            farm++;
            int counter=0;
            incre_rate+=f;
            long double i=farm;
            while(i--){
                sum1=sum1+c/(2+f*counter);
                counter++;
            }

           sum1=sum1+c/incre_rate+x/(incre_rate+f);
           //cout<<sum1<<endl;

        }
        printf("Case #%d: %.7Lf\n",index,sum2);
        index++;

    }

    return 0;
}
