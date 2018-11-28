#include <fstream>
#include <vector>
#include <iostream>
#include <sstream>
#include <cstdlib>
using namespace std;

int main()
{
    ifstream myfile ("A-small-attempt1.in");

    vector <string> lineInput;
    string line;
    int cases = 0;      int k=0;         int notDone = 0;    int currCase = 1;

    //track # of X/O: horizontal lines
    int xHScore = 0;    int oHScore = 0;
    //track # of X/O: vertical lines
    int xVScore = 0;    int oVScore = 0;
    //track # of X/O: diagonal lines
    int xD1Score = 0;   int oD1Score = 0;   int xD2Score = 0;   int oD2Score = 0;
    //flag if X/O has 4 in a row.
    int xWon = 0;       int oWon = 0;

////Open text file and read each line intto vector<string> lineInput.
    if(myfile.is_open())
        while(myfile.good()){
            getline(myfile, line);
            lineInput.push_back(line);
        }
    myfile.close();

////Convert the first line string to an integer and assign it to cases variable.
    line = lineInput.at(0);
    cases = atoi(line.c_str());

////Calculate total dimensions required to store game stats; create game stats Array.
    int total = cases*4;
    string matches[total][4];

////Read the vector of strings and convert into a 2D array of Chars.
    for(int i = 1; i < lineInput.size(); i++){
        line = lineInput.at(i);
        if(line != ""){
            for(int j = 0; j < 4; j++)
                matches[k][j] = line.at(j);
            k++;
        }
    }

    for(currCase = 0; currCase < cases; currCase++)
    {
////Analyze horizontal lines to see if someone has won.
        for(int i=0; i < 4; i++){
            for(int j=0; j < 4; j++){xVScore = 0; oVScore = 0;
                if(matches[i%4+currCase*4][j] == "X" || matches[i%4+currCase*4][j] == "T")
                    xHScore ++;
                else if(matches[i%4+currCase*4][j] == "O" || matches[i%4+currCase*4][j] == "T")
                    oHScore ++;
                if(matches[i%4+currCase*4][j] == ".")
                    notDone = 99;
            }
            ////Check and set the horziontal win flag for X or O.
            if(xHScore == 4)
                xWon = 1;
            if(oHScore == 4)
                oWon = 1;
            xHScore = 0; oHScore = 0;
        }
////Analyze vertical lines to see if someone has won.
        for(int j = 0; j < 4; j++){
            for(int i = 0; i < 4; i++){
                if(matches[i%4+currCase*4][j] == "X" || matches[i%4+currCase*4][j] == "T")
                    xVScore ++;
                if(matches[i%4+currCase*4][j] == "O" || matches[i%4+currCase*4][j] == "T")
                    oVScore ++;
            }
            ////Check and set the vertical win flag for X or O.
            if(xVScore == 4)
                xWon = 1;
            if(oVScore == 4)
                oWon = 1;
            xVScore = 0; oVScore = 0;
        }
////Analyze diagonal lines to see if someone has won.
        for(int i = 0; i < 4; i++){
            for(int j = 0; j < 4; j++){
                if(i == j){
                    if(matches[i%4+currCase*4][j] == "X" || matches[i%4+currCase*4][j] == "T")
                        xD1Score ++;
                    if(matches[i%4+currCase*4][j] == "O" || matches[i%4+currCase*4][j] == "T")
                        oD1Score ++;
                } if(i + j == 3){
                    if(matches[i%4+currCase*4][j] == "X" || matches[i%4+currCase*4][j] == "T")
                        xD2Score ++;
                    if(matches[i%4+currCase*4][j] == "O" || matches[i%4+currCase*4][j] == "T")
                        oD2Score ++;
                }
            }
        }
        ////Check and set the diagonal win flag for X or O.
        if(xD1Score == 4 || xD2Score == 4)
            xWon = 1;
        if(oD1Score == 4 || oD2Score == 4)
            oWon = 1;
        xD1Score = 0; oD1Score = 0; xD2Score = 0; oD2Score = 0;

////Check to see what the status of the game is and reset values.
        ofstream out;
        out.open("answer.txt", std::ios::app);
        if(xWon == 1){
            out << "Case #"<< currCase+1 << ": X won\n";
            xHScore = 0;    oHScore = 0;    notDone = 0;    xWon = 0;
            xVScore = 0;    oVScore = 0;
            xD1Score = 0;   xD2Score = 0;   oD1Score = 0;   oD2Score = 0;
        } else if(oWon == 1){
            out << "Case #"<< currCase+1 << ": O won\n";
            xHScore = 0;    oHScore = 0;    notDone = 0;    oWon = 0;
            xVScore = 0;    oVScore = 0;
            xD1Score = 0;   xD2Score = 0;   oD1Score = 0;   oD2Score = 0;
        } else if(notDone == 99){
            out << "Case #" << currCase+1 << ": Game has not completed\n";
            xHScore = 0;    oHScore = 0;    notDone = 0;
            xVScore = 0;    oVScore = 0;
            xD1Score = 0;   xD2Score = 0;   oD1Score = 0;   oD2Score = 0;
        } else if(xWon == 0 && oWon == 0 && notDone == 0){
            out << "Case #" << currCase+1 << ": Draw\n";
            xHScore = 0;    oHScore = 0;    notDone = 0;
            xVScore = 0;    oVScore = 0;
            xD1Score = 0;   xD2Score = 0;   oD1Score = 0;   oD2Score = 0;
        }
    }
    return 0;
}

