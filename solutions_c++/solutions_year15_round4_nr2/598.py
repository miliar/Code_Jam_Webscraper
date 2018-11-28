#include <iostream>

using namespace std;

int main()
{
    int te;
    cin>>te;
    for(int testy = 1; testy <= te; testy++)
    {
        int N;
        double V, X, R1, C1, R2, C2;
        cin>>N>>V>>X>>R1>>C1;
        if (N == 2)
            cin>>R2>>C2;
        if (C1 == C2)
        {
            N = 1;
            R1 += R2;
        }
        if (N==1)
        {
            if (C1 == X)
            {
                printf("Case #%d: %.10lf\n", testy, V/R1);
                continue;
            }
            printf("Case #%d: IMPOSSIBLE\n", testy);
            continue;
        }
        if (X < min(C1, C2) || X > max(C1, C2) )
        {
            printf("Case #%d: IMPOSSIBLE\n", testy);
            continue;
        }
        double alfa = (X - C2) / (C1 - C2);
        double potrzebapierwszego = alfa*V, potrzebadrugiego = (1.0-alfa)*V;
        double t = max( potrzebapierwszego/R1, potrzebadrugiego/R2 );
        printf("Case #%d: %.10lf\n", testy, t);
        
    }
    
    
   // system("PAUSE");    
    return 0;
}
