#include <iostream>
#include <fstream>
#include <cstdio>


using namespace std;

int main()
{
    // open input file
//    ifstream ifs;
//    ifs.open("../input.txt");
    freopen("../a.in", "r", stdin);

    int T = 0;
    cin >> T;

    for (int test_case = 1; test_case <= T; test_case++)
    {
        int line[2][4] = {0};

        for (int arrangement = 0; arrangement < 2; arrangement++)
        {
            int volAnswer = 0;
            cin >> volAnswer;

            for (int i = 0; i < volAnswer; i++)
                cin.ignore(20, '\n');

            for (int i = 0; i < 4; i++)
                cin >> line[arrangement][i];

            for (int i = 0; i < 5 - volAnswer; i++)
                cin.ignore(20, '\n');
        }

        int count = 2;
        int answer = 0;
        for (int i = 0; (i < 4) && count; i++)
        {
            int d = line[0][i];
            for (int k = 0; k < 4; k++)
            {
                if (line[1][k] == d)
                {
                    count--;
                    if (!count)
                        break;
                    answer = d;
                }

            }
        }

        cout << "Case #" << test_case << ": ";

        switch (count)
        {
        case 2:
            cout << "Volunteer cheated!" << endl;
            break;
        case 1:
            cout << answer << endl;
            break;
        case 0:
        default:
            cout << "Bad magician!" << endl;
            break;
        }
    }



    return 0;
}

