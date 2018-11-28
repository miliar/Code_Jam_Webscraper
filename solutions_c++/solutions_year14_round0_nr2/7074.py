#include <cstdio>

int main(int argc, char** argv)
{
    int T;
    scanf("%d", &T);
    
    for(int t = 1; t <= T; ++t)
    {
        printf("Case #%d: ", t);
        double C, F, X;
        scanf("%lf %lf %lf", &C, &F, &X);
        
        int f = 0;
        double time_to_build_farms = 0.0;
        double ans = X;
        
        while(true)
        {
            double this_answer = time_to_build_farms + X/(2.0 + f*F);
            time_to_build_farms += C/(2.0 + f*F);
            
            if(this_answer > ans)
                break;
            ans = this_answer;
            ++f;
        }
        
        printf("%.7lf\n", ans);
    }
    
    return 0;
}