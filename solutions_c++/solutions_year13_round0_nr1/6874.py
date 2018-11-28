#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int DEBUG = 0;
int GAME = 0;
bool INPROG = false;

void readInput(char [][4]);
void processResults(char [][4]);
void displayResult(char);

int main()
{
    char board[4][4];

    readInput(board);

    return 0;
}

void readInput(char a[][4])
{
    ifstream myIn;
    int boards = 0;

    myIn.open("A-large.in");
    myIn >> boards;

    for (int b = 0; b < boards; b++)
    {
        GAME++;
        for (int i = 0; i < 4; i++)
        {
            for (int j = 0; j < 4; j++)
            {
                myIn >> a[i][j];
                if (DEBUG == 1) cout << a[i][j];
            }
            
            if (DEBUG == 1) cout << endl;
        }

        if (DEBUG == 1) cout << endl;
        processResults(a);
    }

    myIn.close();
}

void processResults(char a[][4])
{
    int countX = 0,
        countO = 0;
    bool win = false;
    INPROG = false;

    // checks all horizontal possibilities
    for (int i = 0; i < 4 && !win; i++)
    {
        for (int j = 0; j < 4 && !win; j++)
        {
            if (a[i][j] == '.'){    INPROG = true;    }
            if (a[i][j] == 'X'){    countX++;       }
            if (a[i][j] == 'O'){    countO++;       }
            if (a[i][j] == 'T')
            {
                countX++;
                countO++;
            }

            if (countX == 4)
            {
                win = true;
                if (DEBUG) cout << "horizontal: " << i << endl;
                displayResult('X');
                countX = 0;
                countO = 0;
                return;
            }
            else if (countO == 4)
            {
                win = true;
                if (DEBUG) cout << "horizontal: " << i << endl;
                displayResult('O');
                countX = 0;
                countO = 0;
                return;
            }
        }

        countX = 0; countO = 0;
    }

    // checks all horizontal possibilities
    for (int j = 0; j < 4 && !win; j++)
    {
        for (int i = 0; i < 4 && !win; i++)
        {
            if (a[i][j] == '.'){    INPROG = true;    }
            if (a[i][j] == 'X'){    countX++;       }
            if (a[i][j] == 'O'){    countO++;       }
            if (a[i][j] == 'T')
            {
                countX++;
                countO++;
            }

            if (countX == 4)
            {
                win = true;
                if (DEBUG) cout << "vertical: " << i << endl;
                displayResult('X');
                countX = 0; countO = 0;
                return;
            }
            else if (countO == 4)
            {
                win = true;
                if (DEBUG) cout << "vertical: " << i << endl;
                displayResult('O');
                countX = 0; countO = 0;
                return;
            }
        }

        countX = 0; countO = 0;
    }

    // checks all diaganal possibilities
    for (int i = 0; i < 4; i++)
    {
        if (a[i][i] == 'X'){    countX++;       }
        if (a[i][i] == 'O'){    countO++;       }
        if (a[i][i] == 'T')
        {
            countX++;
            countO++;
        }

        if (countX == 4)
        {
            win = true;
            if (DEBUG) cout << "diagonal left" << endl;
            displayResult('X');
            countX = 0; countO = 0;
            return;
        }
        else if (countO == 4)
        {
            win = true;
            if (DEBUG) cout << "diagonal left" << endl;
            displayResult('O');
            countX = 0; countO = 0;
            return;
        }
    }
    countX = 0; countO = 0;
    for (int i = 3, j = 0; i >= 0 && j < 4; i--, j++)
    {
        if (a[i][j] == 'X'){    countX++;       }
        if (a[i][j] == 'O'){    countO++;       }
        if (a[i][j] == 'T')
        {
            countX++;
            countO++;
        }

        if (countX == 4)
        {
            win = true;
            if (DEBUG) cout << "diagonal right" << endl;
            displayResult('X');
            countX = 0; countO = 0;
            return;
        }
        else if (countO == 4)
        {
            win = true;
            if (DEBUG) cout << "diagonal right" << endl;
            displayResult('O');
            countX = 0; countO = 0;
            return;
        }
    }
    countX = 0; countO = 0;

    // if no results
    if (INPROG)
    {
        INPROG = false;
        displayResult('.');
        return;
    }

    displayResult('c');
    return;
}

void displayResult(char str)
{
    if (str == 'X')
    {
        cout << "Case #" << GAME << ": X won\n";
    }
    else if (str == 'O')
    {
        cout << "Case #" << GAME << ": O won\n";
    }
    else if (str == '.')
    {
        cout << "Case #" << GAME << ": Game has not completed\n";
    }
    else 
    {
        cout << "Case #" << GAME << ": Draw\n";
    }
}
