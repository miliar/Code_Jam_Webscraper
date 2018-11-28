#include<bits/stdc++.h>

using namespace std;

int main()
{

    int casos;
    scanf("%d",&casos);
    for(int i = 0 ; i < casos ; i++)
    {
        int total,personas,smax;
        string linea;
        total = personas = 0;
        scanf("%d",&smax);
        cin >> linea;
        for(int j = 0 ; j < linea.size() ; j++)
        {
            int valor = linea[j] - '0';
            if(valor != 0)
            {
                if(personas < j)
                {
                    total+= j - personas;
                    personas += j - personas;
                }
                    personas += valor;
            }
            if(personas >= smax)
                break;
        }
        printf("Case #%d: %d\n",i+1,total);
    }
    return 0;
}
