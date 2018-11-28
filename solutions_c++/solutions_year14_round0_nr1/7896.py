#include <iostream>

using namespace std;

int main()
{
    int t, r1, r2, arreglo1[4][4], arreglo2[4][4], cont = 0, num;

    cin >> t;

    for(int i = 0; i < t; i++)
    {
        cin >> r1;

        for(int j = 0; j < 4; j++)
        {
            for(int k = 0; k < 4; k++)
            {
                cin >> arreglo1[j][k];
            }
        }

        cin >> r2;

        for(int j = 0; j < 4; j++)
        {
            for(int k = 0; k < 4; k++)
            {
                cin >> arreglo2[j][k];
            }
        }

        for(int j = 0; j < 4; j++)
        {
            for(int k = 0; k < 4; k++)
            {
                if(arreglo1[r1-1][j] == arreglo2[r2-1][k])
                {
                    cont++;
                    num = arreglo1[r1-1][j];
                }
            }

            if(cont >= 2)
            {
                cout << "Case #" << i+1 << ":" << " Bad magician!" << endl;
                break;
            }
        }

        if(cont == 1)
        {
            cout << "Case #" << i+1 << ": " << num << endl;
        }
        else if(cont == 0)
        {
            cout << "Case #" << i+1 << ":" << " Volunteer cheated!" << endl;
        }

        cont = 0;
    }
    return 0;
}
