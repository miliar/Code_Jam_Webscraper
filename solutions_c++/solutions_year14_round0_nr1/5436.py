#include <iostream>

using namespace std;

int T;
int numbers1[4];
int numbers2[4];

void ReadNumbers(int * numbers)
{
    int row;
    cin >> row;
    for (int r = 1; r <= 4; ++r)
    {
        if (r == row)
        {
            cin >> numbers[0] >> numbers[1] >> numbers[2] >> numbers[3];
        }
        else
        {
            int temp;
            cin >> temp >> temp >> temp >> temp;
        }
    }
}

void Solve(int t)
{
    int count = 0;
    int answer = -1;
    for (int i = 0; i < 4; ++i)
    {
        for (int j = 0; j < 4; ++j)
        {
            if (numbers1[i] == numbers2[j])
            {
                ++count;
                answer = numbers1[i];
            }
        }
    }
    cout << "Case #" << t << ": ";
    if (count == 0)
    {
        cout << "Volunteer cheated!";
    }
    else if (count == 1)
    {
        cout << answer;
    }
    else
    {
        cout << "Bad magician!";
    }
    cout << endl;
}

int main()
{
    cin >> T;
    for (int t = 1; t <= T; ++t)
    {
        ReadNumbers(numbers1);
        ReadNumbers(numbers2);
        Solve(t);
    }
}
