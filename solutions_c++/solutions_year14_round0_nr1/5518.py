#include <iostream>
#include <fstream>
#define SIZE 4

using namespace std;

ifstream in("A-small-attempt0.in");
ofstream out("out.txt");

void write(int a[], int b[], int t)
{
    int num = 0, found;

    for (int i = 0; i < SIZE; i++)
    {
        for (int j = 0; j < SIZE; j++)
        {
            if (a[i] == b[j])
            {
                found = a[i];
                num++;
            }
        }
    }

    switch (num)
    {
        case 0:
            out << "Case #" << t << ": Volunteer cheated!" << endl;
            break;
        case 1:
            out << "Case #" << t << ": " << found << endl;
            break;
        default:
            out << "Case #" << t << ": Bad magician!" << endl;
    }
}

int main()
{
    int tests, row, data;
    int hand[SIZE], hand2[SIZE];

    in >> tests;

    for (int t = 1; t <= tests; t++)
    {
        in >> row;

        for (int i = 0; i < SIZE; i++)
        {
            for (int j = 0; j < SIZE; j++)
            {
                in >> data;

                if ((row - 1) == i)
                {
                    hand[j] = data;
                }
            }
        }

        in >> row;

        for (int i = 0; i < SIZE; i++)
        {
            for (int j = 0; j < SIZE; j++)
            {
                in >> data;

                if ((row - 1) == i)
                {
                    hand2[j] = data;
                }
            }
        }
        write(hand, hand2, t);
    }

    in.close();
    out.close();
    return 0;
}
