#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    int T;
    int r1, r2, n, C;
    int cards1[4];
    int cards2[4];
    int found;
    ifstream input("./input.in");
    ofstream output("output.out");
    if (!input.is_open())
    {
        return 1;
    }
    input >> T;
    int cas = 0;
    while(T--)
    {
        cas++;
        found = false;
        input >> r1;
        for (int i = 0; i < 4; i++)
        {
            for (int j = 0; j < 4; j++)
            {
                input >> n;
                if (r1 == i+1)
                {
                    cards1[j] = n;
                }
            }
        }
        input >> r2;
        for (int i = 0; i < 4; i++)
        {
            for (int j = 0; j < 4; j++)
            {
                input >> n;
                if (r2 == i+1)
                {
                    cards2[j] = n;
                }
            }
        }
        found = 0;
        for (int i = 0; i < 4; i++)
        {
            for (int j = 0; j < 4; j++)
            {
                if(cards1[i] == cards2[j])
                {
                    C = cards1[i];
                    found++;
                }
            }
        }
        output << "Case #" << cas << ": ";
        if (found == 0)
            output << "Volunteer cheated!" << endl;
        else if (found == 1)
            output << C << endl;
        else
            output << "Bad magician!" << endl;
    }
    return 0;
}
