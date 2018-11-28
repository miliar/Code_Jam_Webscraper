#include<iostream>
#include<fstream>
#include <string>
using namespace std;

int main()
{
    ofstream output;
    ifstream input ("A-small-attempt1.in");
    output.open ("A-small-attempt1.out");
    string line;

    if(input.is_open())
    {
        int t;

        input >> t;
        for(int i = 1; i <= t; i++)
        {
            int ans1, ans2;
            int square1[4][4], square2[4][4];

            input >> ans1;
            for(int j = 0; j < 4; j++)
                for(int k = 0; k < 4; k++)
                    input >> square1[j][k];
            input >> ans2;
            for(int j = 0; j < 4; j++)
                for(int k = 0; k < 4; k++)
                    input >> square2[j][k];

            ans1--, ans2--;
            int card = 0, numberofcard;
            for(int j = 0; j < 4; j++)
                for(int k = 0; k < 4; k++)
                    if(square1[ans1][j] == square2[ans2][k])
                    {
                        card++;
                        numberofcard = square1[ans1][j];
                        break;
                    }

            if(card == 1)
                output << "Case #" << i << ": " << numberofcard << endl;
            else if(card > 1)
                output << "Case #" << i << ": Bad magician!" << endl;
            else if(card == 0)
                output << "Case #" << i << ": Volunteer cheated!" << endl;
        }
        output.close();
    }

    return 0;
}
