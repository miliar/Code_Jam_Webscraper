#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

ifstream fin("a.in");
ofstream fout("a.out");

int A, B, T;
int Row[20][3];
vector<int> V;

int main()
{
    fin >> T;

    for(int t = 1; t <= T; t++)
    {
        fin >> A;
        V.clear();

        for(int i = 1; i <= 4; i++)
            for(int j = 1; j <= 4; j++)
            {
                int x;
                fin >> x;
                Row[x][1] = i;
            }

        fin >> B;

        for(int i = 1; i <= 4; i++)
            for(int j = 1; j <= 4; j++)
            {
                int x;
                fin >> x;
                Row[x][2] = i;
            }

        for(int i = 1; i <= 16; i++)
            if(Row[i][1] == A && Row[i][2] == B)
                V.push_back(i);

        fout << "Case #" << t << ": ";

        if(V.size() == 1)
            fout << V[0] << "\n";
        else if(V.empty())
            fout << "Volunteer cheated!\n";
        else
            fout << "Bad magician!\n";
    }
}
