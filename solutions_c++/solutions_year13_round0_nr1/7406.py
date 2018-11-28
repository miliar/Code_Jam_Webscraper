#include <iostream>
#include <string>
#include <fstream>

using namespace std;

ifstream inputfile("A-large.in");

int main()
{
    int n; inputfile >> n;
    inputfile.ignore();

    for(int i = 0; i < n; i++){
        string game[4];
        string line;
        for(int j =0; j < 4; j++){
            getline(inputfile,line);
            game[j] = line;
        }

        int posx = 4,posy = 4;
        bool complete = true;
        for(int j = 0; j < 4; j++){
            for(int k = 0; k < 4; k++){
                if(game[j][k] == 'T'){
                    posy = j; posx=k;
                }
                else if(game[j][k] == '.')
                    complete = false;
            }
        }

        bool noT = false;
        if(posx == posy && posx == 4){
            noT = true;
        }

        char players[] = {'X', 'O'};
        bool won[] = {false, false};
        for(int j = 0; j < 2; j++){
            if(!noT)
                game[posy][posx] = players[j];
            for(int k = 0; k < 4; k++){
                if(game[k][0] == game[k][1] && game[k][1] == game[k][2] && game[k][2] == game[k][3] && game[k][3] == players[j])
                    won[j] = true;
                else if(game[0][k] == game[1][k] && game[1][k] == game[2][k] && game[2][k] == game[3][k] && game[3][k] == players[j])
                    won[j] = true;
                else if(game[0][0] == game[1][1] && game[1][1] == game[2][2] && game[2][2] == game[3][3] && game[3][3] == players[j])
                    won[j] = true;
                else if(game[0][3] == game[1][2] && game[1][2] == game[2][1] && game[2][1] == game[3][0] && game[3][0] == players[j])
                    won[j] = true;
            }
        }

        getline(inputfile,line);

        cout << "Case #" << i+1 << ": ";
        if(won[0])
            cout << "X won";
        else if(won[1])
            cout << "O won";
        else if(!complete)
            cout << "Game has not completed";
        else
            cout << "Draw";
        cout << endl;
    }


    inputfile.close();
    return 0;
}
