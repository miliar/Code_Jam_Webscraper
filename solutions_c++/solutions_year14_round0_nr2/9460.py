#include <stdio.h>

#define EPS 1e-6

int comparar(double a, double b)
{
    if(a - b > EPS)
        return 1;
    else if(b - a > EPS)
        return -1;
    return 0;
}

int main()
{
    int test;
    
    scanf("%d",&test);
    
    int casos = 1;
    
    while(test--)
    {
        double C, F, X;
        
        scanf("%lf %lf %lf",&C, &F, &X);
        
        double minimo = X / 2.0;
        
        double limite = minimo;
        
        double acum = 0.0;
        double a = 2.0;
        double A;
        double B;
        bool first = true;
        
        while(comparar(limite, acum) == 1)
        {
            acum += (C / a);
            a += F;
            A = acum + (X / a);
            
            minimo = (comparar(minimo, A) == 1) ? A : minimo;
            
            if(first)
            {
                B = A;
                first = false;
            }
            else
            {
                if(comparar(A, B) == 1)
                    break;
                
                B = A;
            }
        }
        
        printf("Case #%d: %.7lf\n",casos++, minimo);
    }
    
    return 0;
}