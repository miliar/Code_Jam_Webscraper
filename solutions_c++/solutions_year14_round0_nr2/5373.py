#include<stdio.h>
bool evalue(double Xgoal, double Fextar, double Cost, double basic){

    return ((Xgoal - Cost) / basic) > (Xgoal / (basic + Fextar));

}

int main(){
    int T;
    scanf("%d\n", &T);
    int count = 0;
    while(T--){
        double basicRate = 2;
        double Cost, Fextar, Xgoal;
        scanf("%lf %lf %lf\n", &Cost, &Fextar, &Xgoal);
        double sumTime = 0;
        if(Xgoal <= Cost)
            printf("Case #%d: %lf\n", ++count, Xgoal / basicRate);
        else{
            double farmTime = Cost / basicRate;
            sumTime += farmTime;

            while(evalue(Xgoal, Fextar, Cost, basicRate)){
                basicRate += Fextar;
                sumTime += Cost / basicRate;
            }

            sumTime += ( Xgoal - Cost ) / basicRate;
            printf("Case #%d: %lf\n", ++count, sumTime);
        }
    }
    return 0;
}
