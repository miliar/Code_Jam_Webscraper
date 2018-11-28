#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>

using namespace std;

int main(int argc, char* argv[])
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    int t;
    cin >> t;
    for(int maiusato=1; maiusato<=t; maiusato++)
    {
        int r[2];
        int mat[2][4][4];
        for(int i=0; i<2; i++)
        {
            cin >> r[i];
            r[i]--;
            for(int j=0; j<4; j++)
            {
                for(int k=0; k<4; k++)
                {
                    cin >> mat[i][j][k];
                }
            }
        }
        int occ=0;
        int lastnumber;
        for(int i=0; i<4; i++)
        {
            for(int j=0; j<4; j++)
            {
                if(mat[0][r[0]][i]==mat[1][r[1]][j])
                {
                    occ++;
                    lastnumber=mat[0][r[0]][i];
                    break;
                }
            }
        }
        if(occ==1)
        {
            cout << "Case #" << maiusato << ": " << lastnumber;
        }
        else if(occ==0)
        {
            cout << "Case #" << maiusato << ": " << "Volunteer cheated!";
        }
        else
        {
            cout << "Case #" << maiusato << ": " << "Bad magician!";
        }
        if(maiusato!=t)
            cout << endl;
    }
    return 0;
}
