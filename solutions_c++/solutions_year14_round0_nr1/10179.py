#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    int arr1[4][4];
    int arr2[4][4];
    int T,ans1,ans2,cntr,result;
    ifstream input;
    input.open("A-small-attempt0.in");

    ofstream output;
    output.open("output.txt",std::ofstream::trunc);

    input >> T;

    for (int cases = 0; cases<T; cases++)
    {
        output << "Case #" << cases + 1 << ": ";

        input >> ans1;
        for (int i=0;i<4;i++)
            for (int j=0;j<4;j++)
                input >> arr1[i][j];

        input >> ans2;
        for (int i=0;i<4;i++)
            for (int j=0;j<4;j++)
                input >> arr2[i][j];

        cntr = 0;
        for (int i = 0;i<4;i++)
            for (int j=0;j<4;j++)
            {
                if (arr1[ans1-1][i] == arr2[ans2-1][j])
                {
                    cntr++;
                    result = arr1[ans1-1][i];
                }
            }

        if (cntr == 1)
            output << result <<endl;
        else if (cntr == 0)
            output << "Volunteer cheated!" << endl;
        else
            output << "Bad magician!" << endl;
    }
    return 0;
}
