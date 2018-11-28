//
//  main.cpp
//  CodeJam1
//
//  Created by Tony Baik on 4/12/13.
//  Copyright (c) 2013 Tony Baik. All rights reserved.
//

#include <iostream>
#include <string>
using namespace std;

int main(int argc, const char * argv[])
{

    int T = 0;

    cin >> T;
    
    for(int i = 0; i < T; i++)
    {
        string tictac[16];
        int count = 0;
        int total = 0;
        int place[4][4];
        bool o_won = false;
        bool x_won = false;
        int dots = 0;
        for(int j=0; j < 4; j++)
        {
            string temp = "";
            cin >> temp;
            //cout << temp << endl;
            for(int l=0; l < 4; l++)
            {
                string f = temp.substr(l, 1);
                tictac[j * 4 + l] = f;
                //cout << f << endl;
            }
            
        }
        count = 0;
        for(int j=0; j < 4; j++)
        {
            for(int k=0; k < 4; k++)
            {
                
                if(tictac[count] == "O")
                    place[j][k] = -1;
                else if(tictac[count] == "X")
                    place[j][k] = 1;
                else if(tictac[count] == "T")
                    place[j][k] = 9;
                else if(tictac[count] == ".")
                {
                    dots++;
                    place[j][k] = 0;
                }
                //cout << place[j][k] << endl;
                //cout << tictac[count] << endl;
                count++;
            }
        }

        
        cout << "Case #";
        int te = i + 1;
        cout << te;
        cout << ": ";
        //horizontal
        for(int p=0; p<4;p++)
        {
            total = 0;
            for(int k=0; k < 4; k++)
            {
                total += place[p][k];
            }
            //cout << total << endl;
            if(total == 4 || total == 12)
                x_won = true;
            else if(total == -4 || total == 6)
                o_won = true;
        }
        //vertical
        for(int p=0; p<4;p++)
        {
            total = 0;
            for(int k=0; k < 4; k++)
            {
                total += place[k][p];
            }
            if(total == 4 || total == 12)
                x_won = true;
            else if(total == -4 || total == 6)
                o_won = true;
        }
        
        //diagonal
        total = place[0][0] + place[1][1] + place[2][2] + place [3][3];
        if(total == 4 || total == 12)
            x_won = true;
        else if(total == -4 || total == 6)
            o_won = true;
        total = place[3][0] + place[2][1] + place[1][2] + place[0][3];
        if(total == 4 || total == 12)
            x_won = true;
        else if(total == -4 || total == 6)
            o_won = true;
        
        if(x_won && o_won)
            cout << "Draw" << endl;
        else if(x_won)
            cout << "X won" << endl;
        else if(o_won)
            cout << "O won" << endl;
        else if(!x_won && !o_won && dots > 0)
            cout << "Game has not completed" << endl;
        else
            cout << "Draw" << endl;

    }
    return 0;
}

