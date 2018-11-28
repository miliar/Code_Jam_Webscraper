#include <algorithm>
#include <fstream>
#include <iostream>
#include <iterator>
#include <list>
#include <queue>
#include <stack>
#include <string>
#include <vector>

using namespace std;

ifstream fin("data.txt");
ofstream fout("output.txt");

int c[16];
int choose[16];

void runonce()
{
    fill(choose, choose+16, 0);

    int row;
    fin >> row;
    --row;   

    for (int i = 0; i < 16; ++i)
        fin >> c[i];

    for (int i = 0; i < 4; ++i)
        choose[c[row * 4 + i]-1]++;

    fin >> row;
    --row;

    for (int i = 0; i < 16; ++i)
        fin >> c[i];

    for (int i = 0; i < 4; ++i)
        choose[c[row * 4 + i]-1]++;

    int result = -1;
    int count = 0;
    for (int i = 0; i < 16; ++i)
        if (choose[i] == 2)
        {
            result = i;
            ++count;
        }


    if (count == 1)
    {
        fout << result + 1 << endl;
    }
    else if (count > 1)
    {
        fout << "Bad magician!" << endl;
    }
    else
    {
        fout << "Volunteer cheated!" << endl;
    }
}

int main()
{
    int case_count;
    fin >> case_count;
    
    for (int case_id = 1; case_id <= case_count; ++case_id)
    {
        fout << "Case #" << case_id << ": ";
        runonce();
    }

    return 0;
}