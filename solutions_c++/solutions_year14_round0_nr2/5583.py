#include <cstdio>


int main()
{
    int T;
    double goal, factoryCost, factoryGain, gainingPer;
    scanf("%d", &T);
    
    for (int t = 1; t <= T; ++t)
    {
        scanf("%lf %lf %lf", &factoryCost, &factoryGain, &goal);
        
        gainingPer = 2;
        
        double timeTaken = 0;
        
        while (goal / (gainingPer + factoryGain) < (goal - factoryCost) / gainingPer)
        {
            timeTaken += factoryCost / gainingPer;
            gainingPer += factoryGain;
        }
        
        timeTaken += goal / gainingPer;
        
        printf("Case #%d: %.7f\n", t, timeTaken);
    }
}