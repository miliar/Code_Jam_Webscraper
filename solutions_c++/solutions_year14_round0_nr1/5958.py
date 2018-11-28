#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <fstream>

using namespace std;

// -1 = several solutions
// 0 = no solutions
// 0 < x < 15
string getAnswer(const vector<int> row1, const vector<int> row2)
{
    int answer = -1;


    for (int j = 0; j < row1.size(); ++j)
    {
        for (int i = 0; i < row2.size(); ++i)
        {
            if (row1[j] == row2[i])
                if (answer == -1)
                    answer = row1[j];
                else
                    return "Bad magician!";
        }
    }
    if (answer == -1)
        return "Volunteer cheated!";
    ostringstream convert;
    convert << answer;
    return convert.str();
}

/*vector<int> getNumbersInRow(const vector< vector<int> > &cards, const int &row)
{
    return cards[row];
}*/

int main()
{
    ifstream fin("A-small-attempt0.in");
    ofstream fout("A-small-attempt0.out");

    int numTests;
    fin >> numTests;

    for (int i = 0; i < numTests; ++i)
    {
        int row1, row2;
        fin >> row1;

        vector< vector<int> > cards1(4);
        
        for (int j = 0; j < 4; ++j)
        {
            cards1[j].resize(4);
            for (int i = 0; i < 4; ++i)
                fin >> cards1[j][i];
        }

        /*for (int j = 0; j < 4; ++j)
        {
            for (int i = 0; i < 4; ++i)
                cout << cards1[j][i];           
            cout << endl;
        }*/

        fin >> row2;

        vector< vector<int> > cards2(4);
        
        for (int j = 0; j < 4; ++j)
        {
            cards2[j].resize(4);
            for (int i = 0; i < 4; ++i)
                fin >> cards2[j][i];
        }

        /*for (int j = 0; j < 4; ++j)
        {
            for (int i = 0; i < 4; ++i)
                cout << cards2[j][i];           
            cout << endl;
        }*/


        fout << "Case #"<<i+1<<": " << getAnswer(cards1[row1-1], cards2[row2-1]) << endl;
    }
    return 0;
}