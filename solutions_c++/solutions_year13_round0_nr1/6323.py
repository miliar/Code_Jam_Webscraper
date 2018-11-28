#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

string parseGame(vector<string> g);
bool checkRows(vector<string> g, string& result);
bool checkCols(vector<string> g, string& result);
bool checkDiags(vector<string> g, string& result);
bool checkOver(vector<string> g, string& result);
bool whoWon(int numX, int numO, bool isT, string& result);

int main(int argc, char* argv[])
{
    ifstream inputFile(argv[1]);

    string line;

    getline(inputFile, line);

    int numCases = atoi(line.c_str());

    int cCase = 0;

    while (cCase < numCases) {

        // Parse input (next four lines)
        vector<string> game;

        for (int i = 0; i < 4; ++i) {
            getline(inputFile, line);
            game.push_back(line);
        }

        // Take out middle new line
        getline(inputFile, line);
        
        // Return something
        string output = parseGame(game);
        cout << "Case #" << cCase+1 << ": " << output << endl;
        ++cCase;
    }

    return 0;
}

/* Given a vector of four lines, how to determine the state of the game?
 *  - Check if rows have a winner
 *  - Check if cols have a winner
 *  - Check if diagonals have a winner
 *  - If no winner found, check if there are .'s remaining
 */ 

string parseGame(vector<string> g)
{
    string result;

    if (checkRows(g, result))
        return result;
    
    if (checkCols(g, result))
        return result;
    
    if (checkDiags(g, result))
        return result;
    
    if (checkOver(g, result))
        return result;
    
    result = "Draw";
    return result;
}

// Checks if anyone won in a row
bool checkRows(vector<string> g, string& result)
{
    int numX = 0;
    int numO = 0;
    bool isT = false;

    for (vector<string>::iterator it = g.begin(); it != g.end(); ++it) {   
        for (size_t i = 0; i < (*it).length(); ++i) {

            char c = (*it).at(i);

            if (c == 'X' ) 
                ++numX;
            else if (c == 'O')
                ++numO;
            if (c == 'T')
                isT = true;
        }
        if (whoWon(numX, numO, isT, result))
            return true;
        else {
            numX = 0;
            numO = 0;
            isT = false;
        }
    }

    return false;
}

// Checks if anyone won in a column
bool checkCols(vector<string> g, string& result)
{
    int numX = 0;
    int numO = 0;
    bool isT = false;
   
    for (int i = 0; i < 4; ++i) {
        for (vector<string>::iterator it = g.begin(); it != g.end(); ++it) {  
        
            char c = (*it).at(i);

            if (c == 'X' ) 
                ++numX;
            else if (c == 'O')
                ++numO;
            if (c == 'T')
                isT = true;
        } 
        if (whoWon(numX, numO, isT, result))
            return true;
        else {
            numX = 0;
            numO = 0;
            isT = false;
        }
    } 

    return false;
}

bool checkDiags(vector<string> g, string& result)
{
    int numX = 0;
    int numO = 0;
    bool isT = false;
    
    vector<string>::iterator it = g.begin();
    
    for (int i = 0; i < 4 && it != g.end(); ++i, ++it) {
            char c = (*it).at(i);

            if (c == 'X' ) 
                ++numX;
            else if (c == 'O')
                ++numO;
            if (c == 'T')
                isT = true;
    }    
    
    if (whoWon(numX, numO, isT, result)) {
        return true;
    }
    else {
        numX = 0;
        numO = 0;
        isT = false;
    }
    
    it = g.begin();
    
    for (int i = 3; i >= 0 && it != g.end(); --i, ++it) {
            char c = (*it).at(i);

            if (c == 'X' ) 
                ++numX;
            else if (c == 'O')
                ++numO;
            if (c == 'T')
                isT = true;
    }    
    if (whoWon(numX, numO, isT, result)) {
        return true;
    }
    else {
        result = "";
        return false;
    }
}

// General function that determins who won based on number of X's and O's
// and whether or not T is present
bool whoWon(int numX, int numO, bool isT, string& result) 
{
    if ( (numX == 4) || (numX == 3 && isT) ) {
        result = "X won";
        return true;
    }
    else if ( (numO == 4) || (numO == 3 && isT) ) {
        result = "O won";
        return true;
    }
    else {
        result = "";
        return false;
    }
}

bool checkOver(vector<string> g, string& result)
{

    for (vector<string>::iterator it = g.begin(); it != g.end(); ++it) {   
        for (size_t i = 0; i < (*it).length(); ++i) {
            if ((*it).at(i) == '.') {
                result = "Game has not completed";
                return true;
            }
        }
    }

    result = "";
    return false;
}




