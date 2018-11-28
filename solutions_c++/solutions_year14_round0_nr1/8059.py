#include <iostream>

using namespace std;

int main()
{
    int numCases,cards[4][4],posibles[4],fila1,fila2,unica;
    bool esta[4];

    cin >> numCases;
    //cout << numCases << endl;
    for (int numCase = 0; numCase < numCases ; numCase++)
    {
        esta[0] = false;
        esta[1] = false;
        esta[2] = false;
        esta[3] = false;


        cin >> fila1;
        //cout << fila1 << endl;
        fila1--;
        for (int i=0; i < 4;i++)
            for (int j = 0 ; j < 4 ; j++)
                cin >> cards[i][j];
        posibles[0]=cards[fila1][0];
        posibles[1]=cards[fila1][1];
        posibles[2]=cards[fila1][2];
        posibles[3]=cards[fila1][3];

//        cout << endl;
//        for (int i=0 ; i<4 ; i++)
//            cout << posibles[i] << " ";
//        cout << endl;

        cin >> fila2;
        //cout << fila2 << endl;
        for (int i=0; i < 4;i++)
            for (int j = 0 ; j < 4 ; j++)
                cin >> cards[i][j];

        fila2--;
//        cout << endl;
//        for (int i=0 ; i<4 ; i++)
//            cout << cards[fila2][i] << " ";
//        cout << endl;


        if (cards[fila2][0] == posibles[0] ||
            cards[fila2][0] == posibles[1] ||
            cards[fila2][0] == posibles[2] ||
            cards[fila2][0] == posibles[3]  )
            esta[0] = true;
        if (cards[fila2][1] == posibles[0] ||
            cards[fila2][1] == posibles[1] ||
            cards[fila2][1] == posibles[2] ||
            cards[fila2][1] == posibles[3]  )
            esta[1] = true;
        if (cards[fila2][2] == posibles[0] ||
            cards[fila2][2] == posibles[1] ||
            cards[fila2][2] == posibles[2] ||
            cards[fila2][2] == posibles[3]  )
            esta[2] = true;
        if (cards[fila2][3] == posibles[0] ||
            cards[fila2][3] == posibles[1] ||
            cards[fila2][3] == posibles[2] ||
            cards[fila2][3] == posibles[3]  )
            esta[3] = true;

        int cuantos=0;
        for (int i=0 ; i<4 ; i++)
            if (esta[i]) {
                  //  cout << i <<endl;
                    cuantos++;
                    unica = cards[fila2][i];
            }
        //cout << cuantos<< endl;
        switch (cuantos) {
            case 0: cout << "Case #" << numCase+1 << ": Volunteer cheated!\n";
                    break;
            case 1: cout << "Case #" << numCase+1 << ": " << unica << "\n";
                    break;
            default :cout << "Case #" << numCase+1 << ": Bad magician!\n";
        }
    }
    return 0;
}
