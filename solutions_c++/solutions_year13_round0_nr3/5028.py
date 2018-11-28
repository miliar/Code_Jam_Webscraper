#include <cstdio>
#include <cmath>
#include <string>
#include <sstream>
#include <iostream>

using namespace std;

bool e_valido(int x);

int main (void)
{
    int n, contador = 0;
    scanf("%d", &n);
    
    int a, b;
    while (n > 0)
    {
        scanf("%d %d", &a, &b);
        
        int quant = 0;
        for (int i = a; i <= b; i++)
            if (e_valido(i))
                quant++;  
        
        printf("Case #%d: %d\n", ++contador, quant);
        
        n--;
    }
    return 0;
}

bool e_valido(int x)
{
    // Converte pra string
    string s;
    stringstream out;
    out << x;
    s = out.str();  
    
    // Testa de 0 até ceil(n/2) pra ver se x é palíndromo 
    for (int i = 0, n = ceil((float)s.length()/2.0), max = s.length() - 1; i < n; i++)
        if (s[i] != s[max - i])
            return false;
            
    double raizx = sqrt(x), teste;
    
    // Se tiver parte fracionária
    if (modf(raizx, &teste) != 0.0)
        return false;  
    
    // Converte pra string
    stringstream out2;
    out2 << (int)raizx;
    s = out2.str();  
    
    // Testa de 0 até floor(n/2) pra ver se raiz de x é palíndromo 
    for (int i = 0, n = ceil((float)s.length()/2), max = s.length() - 1; i < n; i++)
        if (s[i] != s[max - i])
            return false;
            
    return true;    
}