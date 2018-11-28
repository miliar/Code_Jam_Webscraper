#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

ifstream fin("input.txt");
#define cin fin

bool Existe(int busca, int arr[4])
{
    for(int i = 0; i<4;i++)
    {
        if(arr[i] == busca)
            return true;
    }
    return false;
}

int main()
{
    int nroCasos;
    cin >> nroCasos;
    int caseNmbr = 1;
    while(nroCasos--)
    {
        int fila1;
        cin >> fila1;
        int cont = 1;
        int dummy[4];
        while(fila1 > cont)
        {
            for(int i = 0; i < 4;i++)
                cin >> dummy[i];
            cont++;
        }
        int firstChoice[4];
        for(int i = 0;i<4;i++){
            cin >> firstChoice[i];
        }
        for(int i = fila1; i <4;i++)
        {
            for(int i = 0; i < 4;i++)
                cin >> dummy[i];
        }
        
        int fila2;
        cin >> fila2;
        cont = 1;
        while(fila2 > cont)
        {
            for(int i = 0; i < 4;i++)
                cin >> dummy[i];
            cont++;
        }
        int secondChoice[4];
        for(int i = 0;i<4;i++)
            cin >> secondChoice[i];
        for(int i = fila2; i <4;i++)
        {
            for(int i = 0; i < 4;i++)
                cin >> dummy[i];
        }
        int sol = 0;
        for(int i = 0;i < 4;i++)
        {
            if(Existe(firstChoice[i],secondChoice))
            {
                if(sol == 0)
                {
                    sol = firstChoice[i];
                }else{
                    sol = -1;
                    break;
                }
            }
        }
        
        cout << "Case #" << caseNmbr << ": ";
        switch(sol){
            case 0:
                cout << "Volunteer cheated!" << endl;
            break;
            case -1:
                cout << "Bad magician!" << endl;
            break;
            default:
                cout << sol << endl;
            break;
        }
        
        caseNmbr++;
    }
    
    return 0;
}
