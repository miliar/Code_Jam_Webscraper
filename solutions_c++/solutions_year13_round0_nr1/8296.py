#include <iostream>
using namespace std;

int main (){

    char M[4][4];
    int qtd,i,j,k, xl=0 , ol=0 ,xc=0,oc=0, win = 0,xd1=0,od1=0,xd2=0,od2=0,count;

    cin >> qtd;

    for(k=0;k<qtd;k++){

        for(i=0;i<4;i++)
        for(j=0;j<4;j++)
            cin >> M[i][j];

        count=0;
        win=0;
        xd2=0;
        od2=0;
        xd1=0;
        od1=0;

        for(i=0;i<4;i++){
            if(M[i][i] == 'O' || M[i][i] == 'T')
                od1++;

            else if(M[i][i] == 'X' || M[i][i] == 'T')
                xd1++;
        }

        if (xd1 == 4 ){
            cout << "Case #" << k+1 << ": " << "X won\n";
            win=1;
        }

        else if (od1 == 4 ){
            cout << "Case #" << k+1 << ": " << "O won\n";
            win=1;
        }

        if(win)
            continue;

        for(i=0,j=3;i<4;i++,j--){
            if(M[i][j] == 'X' )
                xd2++;
            else if (M[i][j] == 'O')
                od2++;
            else if (M[i][j] == 'T'){
                xd2++; od2++;
            }


        }

        if (xd2 == 4 ){
            cout << "Case #" << k+1 << ": " << "X won\n";
            win=1;
        }

        else if (od2 == 4 ){
            cout << "Case #" << k+1 << ": " << "O won\n";
            win=1;
        }

        if(win)
            continue;

        for(i=0;i<4;i++){

            xl=0;
            ol=0;
            xc=0;
            oc=0;


            for(j=0;j<4;j++){

                if(M[i][j] == 'X' || M[i][j] == 'T')
                    xl++;
                if (M[i][j] == 'O' || M[i][j] == 'T')
                    ol++;

                if(M[j][i] == 'X' || M[j][i] == 'T')
                    xc++;
                if (M[j][i] == 'O' || M[j][i] == 'T')
                    oc++;

                else if ( M[i][j] == '.')
                    count++;

            }


            if (xc == 4 || xl == 4  ){
                cout << "Case #" << k+1 << ": " << "X won\n";
                win=1;
            }

            else if (oc == 4 || ol == 4  ){
                cout << "Case #" << k+1 << ": " << "O won\n";
                win=1;
            }

        }

        if(win)
            continue;

        else if (count)
            cout << "Case #" << k+1 << ": Game has not completed\n" ;

        else
            cout << "Case #" << k+1 << ": Draw\n" ;


    }

    return 0;
}
