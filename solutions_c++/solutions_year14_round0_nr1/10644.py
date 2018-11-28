#include <iostream>
#include <fstream>
using namespace std;
#define cin input
#define cout output
int main()
{
    ifstream input("input.txt");
    ofstream output("output.txt");
    int a, b, c, d, e, pos[2][5], lent[5][5], match=0, good;
    cin >> a;
    for(int i = 0; i<a; i++)
    {
        for(int k = 0; k<2; k++)
        {
            cin >> b;
            for(int i1 = 0; i1<4; i1++)
            {
                for(int i2=0; i2<4; i2++)
                {
                    cin >> lent[i1][i2];

                }
            }
            for(int j = 0; j<4; j++)
            {
                pos[k][j]=lent[b-1][j];
            }
        }
        for(int k = 0; k<4; k++)
        {
            for(int m = 0; m<4; m++)
            {
                if(pos[0][k]==pos[1][m])
                {
                    match++;
                    good=pos[0][k];
                }
            }
        }
        cout << "Case #"<< i+1 << ": ";
        if(match>1) cout << "Bad magician!" << endl;
        else if(match<1) cout << "Volunteer cheated!" << endl;
        else cout << good << endl;
        match=0;
        }
    return 0;
}
