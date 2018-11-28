#include <iostream>
#include <fstream>
#include <boost/lexical_cast.hpp>

using namespace std;

int main()
{
    ifstream ifs ("in.txt");
    string buf;

    getline(ifs, buf);
    int numOfTestCase = boost::lexical_cast<int>(buf);

    char testCases[numOfTestCase][4][4];
    int rowNum = 0;
    int caseNum= 0;
    while (ifs && getline(ifs, buf))
    {
        if (buf.length() == 0 ||
                (buf[0] != 'O' && buf[0] != 'X' && buf[0] != 'T' && buf[0] != '.') )
        {
            rowNum = 0; // reset
            caseNum++;
            continue;
        }
        testCases[caseNum][rowNum][0] = buf[0];
        testCases[caseNum][rowNum][1] = buf[1];
        testCases[caseNum][rowNum][2] = buf[2];
        testCases[caseNum][rowNum][3] = buf[3];
//        cout << buf[0] << buf[1] << buf[2] << buf [3] << endl;
        rowNum++;
    }

    for (caseNum = 0; caseNum < numOfTestCase; caseNum++)
    {
        cout << "Case #" << caseNum + 1 << ": ";
        bool imcompletion = false;
        bool winnerFound = true;
        // Check each row
        for (int i=0; i < 4; i++)
        {
            char candidate = testCases[caseNum][i][0];
            if (candidate == 'T')
                candidate = testCases[caseNum][i][1];

            winnerFound = true;
            for (int j=0; j < 4; j++)
            {
                if (testCases[caseNum][i][j] == '.')
                {
                    imcompletion = true;
                    winnerFound = false;
                    break;
                }
                else if (testCases[caseNum][i][j] != 'T' &&
                         testCases[caseNum][i][j] != candidate)
                {
                    winnerFound = false;
                    break;
                }
            }
            if (winnerFound)
            {
                cout << candidate << " won" << endl;
                break;
            }
        }
        if (winnerFound)
            continue;

        // col
        for (int i=0; i < 4; i++)
        {
            char candidate = testCases[caseNum][0][i];
            if (candidate == 'T')
                candidate = testCases[caseNum][1][i];

            winnerFound = true;
            for (int j=0; j < 4; j++)
            {
                if (testCases[caseNum][j][i] == '.')
                {
                    imcompletion = true;
                    winnerFound = false;
                    break;
                }
                else if (testCases[caseNum][j][i] != 'T' &&
                         testCases[caseNum][j][i] != candidate)
                {
                    winnerFound = false;
                    break;
                }
            }
            if (winnerFound)
            {
                cout << candidate << " won" << endl;
                break;
            }
        }
        if (winnerFound)
            continue;

        {

            // slash
            char candidate = testCases[caseNum][0][0];
            if (candidate == 'T')
                candidate = testCases[caseNum][1][1];

            winnerFound = true;
            for (int j=0; j < 4; j++)
            {
                if (testCases[caseNum][j][j] == '.')
                {
                    imcompletion = true;
                    winnerFound = false;
                    break;
                }
                else if (testCases[caseNum][j][j] != 'T' &&
                         testCases[caseNum][j][j] != candidate)
                {
                    winnerFound = false;
                    break;
                }
            }
            if (winnerFound)
            {
                cout << candidate << " won" << endl;
                continue;
            }
        }


        {

            char candidate = testCases[caseNum][0][3];
            if (candidate == 'T')
                candidate = testCases[caseNum][1][2];

            winnerFound = true;
            for (int j=0; j < 4; j++)
            {
                if (testCases[caseNum][j][3-j] == '.')
                {
                    imcompletion = true;
                    winnerFound = false;
                    break;
                }
                else if (testCases[caseNum][j][3-j] != 'T' &&
                         testCases[caseNum][j][3-j] != candidate)
                {
                    winnerFound = false;
                    break;
                }
            }
            if (winnerFound)
            {
                cout << candidate << " won" << endl;
                continue;
            }

        }

        if(imcompletion)
            cout << "Game has not completed" << endl;
        else
            cout << "Draw" << endl;
    }

    return 0;
}
