#include <iostream>
#include <fstream>

struct State
{
    unsigned short int currentRow;
    short int tX, tY;
    unsigned short int xColumnSum[4];
    unsigned short int oColumnSum[4];
    unsigned short int xPrincipalDiagSum;
    unsigned short int oPrincipalDiagSum;
    unsigned short int xSecondaryDiagSum;
    unsigned short int oSecondaryDiagSum;
    bool xWon;
    bool oWon;

    State() : currentRow(0), xWon(false), oWon(false), tX(-1), tY(-1), xPrincipalDiagSum(0), oPrincipalDiagSum(0), xSecondaryDiagSum(0), oSecondaryDiagSum(0)
    {
        for (int i=0 ; i<4; i++)
        {
            xColumnSum[i]=0;
            oColumnSum[i]=0;
        }
    }
    ~State() {}

    /**
     * @brief addRow adds a row to the state
     * @param s the line read from file
     * @return true if a solution has been found, false otherwise
     */
    void addRow(std::string s)
    {
        // stats of this row
        unsigned short int xRow = 0;
        unsigned short int oRow = 0;
        unsigned short int t = 0;

        // assign stats
        for (unsigned short i = 0 ; i<4 ; i++)
        {
            // stats for rows and columns
            s[i]=='X'?xRow++,xColumnSum[i]++:s[i]=='O'?oRow++,oColumnSum[i]++:s[i]!='.'?t++:t;

            // principal and secondary diagonal
            if (currentRow == 0)
            {
                if (i == 0)
                    s[i]=='X'?xPrincipalDiagSum++:s[i]=='O'?oPrincipalDiagSum++:oPrincipalDiagSum;
                else if (i == 3)
                    s[i]=='X'?xSecondaryDiagSum++:s[i]=='O'?oSecondaryDiagSum++:oSecondaryDiagSum;
            }
            else if (currentRow == 1)
            {
                if (i == 1)
                    s[i]=='X'?xPrincipalDiagSum++:s[i]=='O'?oPrincipalDiagSum++:oPrincipalDiagSum;
                else if (i == 2)
                    s[i]=='X'?xSecondaryDiagSum++:s[i]=='O'?oSecondaryDiagSum++:oSecondaryDiagSum;
            }
            else if (currentRow == 2)
            {
                if (i == 2)
                    s[i]=='X'?xPrincipalDiagSum++:s[i]=='O'?oPrincipalDiagSum++:oPrincipalDiagSum;
                else if (i == 1)
                    s[i]=='X'?xSecondaryDiagSum++:s[i]=='O'?oSecondaryDiagSum++:oSecondaryDiagSum;
            }
            else if (currentRow == 3)
            {
                if (i == 3)
                    s[i]=='X'?xPrincipalDiagSum++:s[i]=='O'?oPrincipalDiagSum++:oPrincipalDiagSum;
                else if (i == 0)
                    s[i]=='X'?xSecondaryDiagSum++:s[i]=='O'?oSecondaryDiagSum++:oSecondaryDiagSum;
            }

        }

        // if t was found
        if (t==1)
        {
            tX = currentRow;
            tY = s[0]=='T'?0:s[1]=='T'?1:s[2]=='T'?2:3;
        }

        // check if row is a solution
        if (xRow==4 || (xRow==3 && t==1)) // this row is a winning one for x
            xWon = true;
        else if (oRow==4 || (oRow==3 && t==1)) // this row is a winning one for o
            oWon = true;

        // increase row count
        currentRow++;

        // if last row, decide for a soluton
        if(currentRow == 4)
        {
            // check columns for x win
            // check columns for o win
            // check columns for x win with t
            // check columns for o win with t
            for (unsigned int i=0 ; i<4; i++)
            {
                if (xColumnSum[i] == 4)
                    xWon = true;
                if (oColumnSum[i] == 4)
                    oWon = true;
                if (xColumnSum[i] == 3 && tY == i)
                    xWon = true;
                if (oColumnSum[i] == 3 && tY == i)
                    oWon = true;
            }

            // check principal diagonal for win
            // check principal diagonal for win with t
            if (xPrincipalDiagSum == 4)
                xWon = true;
            if (oPrincipalDiagSum == 4)
                oWon = true;
            if (xPrincipalDiagSum == 3 && ((tX==0&&tY==0) || (tX==1&&tY==1) || (tX==2&&tY==2) || (tX==3&&tY==3)))
                xWon = true;
            if (oPrincipalDiagSum == 3 && ((tX==0&&tY==0) || (tX==1&&tY==1) || (tX==2&&tY==2) || (tX==3&&tY==3)))
                oWon = true;

            // check secondary diagonal for win
            // check secondary diagonal for win with t
            if (xSecondaryDiagSum == 4)
                xWon = true;
            if (oSecondaryDiagSum == 4)
                oWon = true;
            if (xSecondaryDiagSum == 3 && ((tX==0&&tY==3) || (tX==1&&tY==2) || (tX==2&&tY==1) || (tX==3&&tY==0)))
                xWon = true;
            if (oSecondaryDiagSum == 3 && ((tX==0&&tY==3) || (tX==1&&tY==2) || (tX==2&&tY==1) || (tX==3&&tY==0)))
                oWon = true;
        }
    }

    std::string solution()
    {
        if (currentRow != 4)
            throw "Insert enough rows first.";
        unsigned int numMoves = 0;
        for (unsigned int i = 0; i<4 ; i++)
            numMoves += (xColumnSum[i]+oColumnSum[i]);
        if (tX!=-1)
            numMoves++;
        bool finished = numMoves==16;
        if (!xWon && !oWon && finished)
            return "Draw";
        if (xWon)
            return "X won";
        if (oWon)
            return "O won";
        return "Game has not completed";
    }
};

int main()
{
    std::ifstream input;
    std::ofstream output;
    std::string line;
    unsigned int numCases;

    input.open("large.txt");
    output.open("output.txt");
    input >> numCases;

    std::getline(input, line); // consume first line
    // std::getline(input, line); // consume white line

    for (unsigned int i = 0 ; i<numCases ; i++)
    {
        State s;
        for (unsigned int y = 0 ; y<4 ; y++)
        {
            std::getline(input, line);
            s.addRow(line);
        }
        output << "Case #" << i+1 << ": " << s.solution() << std::endl;
        std::getline(input, line); // consume white line
    }
    return 0;
}
