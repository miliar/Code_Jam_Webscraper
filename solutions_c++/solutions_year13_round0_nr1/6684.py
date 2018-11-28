#include <vector>
#include <iostream>
#include <string>

using namespace std;

int main()
{
    int T, cont;
    int contLinha[2], transversalA[2], transversalB[2];
    int coluna[2][4];
    char c;
    int ascii;
    int vencedor;
    int jogadas;
    
    /*
    * X - 88
    * O - 79
    * T - 84
    * . - 46
    */

    while(cin >> T)
    {
        for(int cont = 1; cont <= T; cont++)
        {
            jogadas = 0;
            vencedor = 0;
            memset(coluna, 0, sizeof(coluna));
            memset(transversalA, 0, sizeof(transversalA));
            memset(transversalB, 0, sizeof(transversalB));
            for(int i = 0; i < 4; i++)
            {
                memset(contLinha, 0, sizeof(contLinha));
                for(int j = 0; j < 4; j++)
                {
                    cin >> c;
                    if(vencedor == 0)
                    {
                        ascii = (int) c;
                        if(ascii == 84)
                        {
                            jogadas++;
                            contLinha[0]++;
                            contLinha[1]++;
                            coluna[0][j]++;
                            coluna[1][j]++;
                            if(i == j)
                            {
                                transversalA[0]++;
                                transversalA[1]++;     
                            }
                            else if((j + i) == 3)
                            {
                                transversalB[0]++;
                                transversalB[1]++; 
                            }
                        }
                        else if(ascii == 79)
                        {
                            jogadas++;
                            contLinha[0]++;
                            coluna[0][j]++;
                            if(i == j) transversalA[0]++;  
                            else if((j + i) == 3) transversalB[0]++;
                        }
                        else if(ascii == 88)
                        {
                            jogadas++;
                            contLinha[1]++;
                            coluna[1][j]++;
                            if(i == j) transversalA[1]++;  
                            else if((j + i) == 3) transversalB[1]++;
                        }
                    }
                }     
                if(contLinha[0] == 4) vencedor = 79;
                else if(contLinha[1] == 4) vencedor = 88;
            } 
            if(vencedor == 0)
            {
                if(transversalA[0] == 4) vencedor = 79;
                else if(transversalA[1] == 4) vencedor = 88;
                else if(transversalB[0] == 4) vencedor = 79;
                else if(transversalB[1] == 4) vencedor = 88;
                else if(coluna[0][0] == 4) vencedor = 79;
                else if(coluna[0][1] == 4) vencedor = 79;
                else if(coluna[0][2] == 4) vencedor = 79;
                else if(coluna[0][3] == 4) vencedor = 79;
                else if(coluna[1][0] == 4) vencedor = 88;
                else if(coluna[1][1] == 4) vencedor = 88;
                else if(coluna[1][2] == 4) vencedor = 88;
                else if(coluna[1][3] == 4) vencedor = 88;
            }
            
            if(vencedor != 0) cout << "Case #" << cont << ": " << (char) vencedor << " won" << endl;
            else if(jogadas == 16) cout << "Case #" << cont << ": Draw" << endl;
            else cout << "Case #" << cont << ": Game has not completed" << endl;
            
        }          
    }
    return 0;
}
