#include <cstdio>
#include <cstring>

#define MAX 110

int jardim[MAX][MAX];
int n, m;

bool celula_valida(int coluna, int linha);

int main (void)
{
    int t, contador = 0;
    scanf("%d", &t);
    
    while (t > 0)
    {
        scanf("%d %d", &n, &m);
        
        memset(jardim, 0, sizeof(jardim));
        
        // i == n && j == m
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                scanf("%d", &jardim[i][j]);            
             
        bool resposta = true;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                if (!celula_valida(i, j))
                {
                    resposta = false;
                    goto HELL;
                }
                
        HELL:
        
        printf("Case #%d: %s\n", ++contador, resposta ? "YES" : "NO");     
        
        t--;
    }
    
    return 0;
}

bool celula_valida(int linha, int coluna)
{
    // Checa coluna
    bool coluna_valida = true;
    for (int j = 0; j < m; j++)
        if (jardim[linha][j] > jardim[linha][coluna])
        {
            coluna_valida = false;
            break;
        }
        
    // Checa linha
    bool linha_valida = true;
    for (int i = 0; i < n; i++)
        if (jardim[i][coluna] > jardim[linha][coluna])
        {
            linha_valida = false;
            break;
        }    
    
    return (linha_valida || coluna_valida);
}