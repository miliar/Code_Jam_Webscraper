//14/04/2013
//kizarae@gmail.com

#include <iostream>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <vector>

using namespace std;

void decide(vector<char> match);
bool win(vector<char> match, char winner, int i1, int i2, int i3, int i4);

//Messy, I know
//Using redirects to standard input and output
int main ()
{
    int n;
    char* line = new char[5];
    vector<char> match;
    
    //Get number of cases
    cin.getline(line, 5);
    n = atoi(line);
    
    int count = 0;
    for (int z=0; z<n; z++)//For each case
    {
        for (int y=0; y<4; y++)//For each row
        {
            cin.getline(line, 5);
            for (int x=0; x<4; x++)//for each column
            {
                match.push_back(line[x]);
                count++;
            }
        }
        cout << "Case #" << (z+1) << ": ";
        decide(match);
        match.clear();//Reset for next match
        cin.getline(line, 5);//discard
    }
    
    return 0;
}

void decide(vector<char> match)
{    
    //hor
    for (int z=0; z<16; z+=4)
    {
        if (win(match,'O',z,z+1,z+2,z+3))
        {
            cout << "O won\n";
            return;
        }
        if (win(match,'X',z,z+1,z+2,z+3))
        {
            cout << "X won\n";
            return;
        }
    }
    
    //vert
    for (int z=0; z<4; z++)
    {
        if (win(match,'O',z,z+4,z+8,z+12))
        {
            cout << "O won\n";
            return;
        }
        if (win(match,'X',z,z+4,z+8,z+12))
        {
            cout << "X won\n";
            return;
        }
    }
    
    //diag
    if ((win(match,'O',0,5,10,15))||(win(match,'O',3,6,9,12)))
    {
        cout << "O won\n";
        return;
    }
    if ((win(match,'X',0,5,10,15))||(win(match,'X',3,6,9,12)))
    {
        cout << "X won\n";
        return;
    }
    
    //Draw or not finished
    for (int z=0; z<16; z++)
    {
        if (match[z]=='.')
        {
            cout << "Game has not completed\n";
            return;
        }
    }
    
    cout << "Draw\n";
}

bool win(vector<char> match, char winner, int i1, int i2, int i3, int i4) //Check if winning combination with line and player given
{
    if (((match[i1]=='T')||(match[i1]==winner))&&((match[i2]=='T')||(match[i2]==winner))&&((match[i3]=='T')||(match[i3]==winner))&&((match[i4]=='T')||(match[i4]==winner)))
    {
        return true;
    }
    else
    {
        return false;
    }
}
