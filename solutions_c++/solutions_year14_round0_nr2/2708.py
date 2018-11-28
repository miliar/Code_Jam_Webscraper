// cookie_clicker

#include <iostream>
#include <iomanip>

#define BASE_GEN_RATE 2.0

using namespace std;

double gSumTab[100000];

void pre_comp(unsigned int N, double F)
{
    unsigned int i;
    
    gSumTab[0] = 1.0 / BASE_GEN_RATE;
    
    for (i = 1; i < N; i++)
    {
        gSumTab[i] = gSumTab[i-1] + (1.0 / (BASE_GEN_RATE + i * F));        
    }
}

int main()
{
    unsigned int i;
    unsigned int T;
    
    cin>>T;
    
    for (i = 0; i < T; i++)
    {
        unsigned int j;
        unsigned int N;
        double C, F, X;
        double t, min_t;
        
        cin>>C>>F>>X;
        
        N = X / C + 1;
        pre_comp(N, F);                
        min_t = X / BASE_GEN_RATE;        
        for (j = 1; j < N; j++)
        {
            t = X / (BASE_GEN_RATE + j * F) + C * gSumTab[j-1];
            if (t < min_t)
            {
                min_t = t;
            }
        }
        
        cout<<"Case #"<<i+1<<": "<<fixed<<setprecision(7)<<min_t<<endl;
    }
    
    return 0;
}
