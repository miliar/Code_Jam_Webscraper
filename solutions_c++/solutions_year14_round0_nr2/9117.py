
#include <string>
#include <iostream>
#include <cstdio>

int main(int argc, const char * argv[])
{
    int T;
    scanf("%d", &T);
    
    for(int i=0; i<T; i++)
    {
        double C, F, X;
        scanf("%lf %lf %lf", &C, &F, &X);
        
        printf("Case #%d: ", i+1);
        
        
        double elapsedSeconds = 0;
        double rate = 2.0f;
        while (1) {
            double factor = X / rate;
            bool shouldBuyFarm = factor > ((C / rate) + (X / (rate + F)));
            if (shouldBuyFarm) {
                elapsedSeconds += (C / rate);
                rate += F;
            }
            else {
                elapsedSeconds += (X / rate);
                break;
            }
        }
        
        printf("%.7lf", elapsedSeconds);
        
        printf("\n");
    }
    
    return 0;
}
