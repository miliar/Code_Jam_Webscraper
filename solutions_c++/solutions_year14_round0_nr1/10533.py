#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cstddef>
#include <cctype>
#include <cfloat>
#include <climits>
#include <iomanip>
#include <algorithm>

#define SIZE 20000000

const double  pi = 2 * acos (0.0);

using namespace std;

int main(void)
{
    int tc,cs=0;
    cin >> tc;

    while(tc--)
    {
        int a[10][10],b[10][10],n,r1,r2;

        cin >> r1;

        for(int i = 0; i<4; i++)
        {
            for(int j=0; j<4; j++)
            {
                cin >> a[i][j];
            }
        }

        cin >> r2;

        for(int i=0; i<4; i++)
        {
            for(int j=0; j<4; j++)
            {
                cin >> b[i][j];
            }
        }

        int temp = 0;
        int man;
        for(int i=0; i<4; i++)
        {
            for(int j=0; j<4; j++)
            {
                if(a[r1-1][i]==b[r2-1][j])
                {
                    temp++;
                    man = a[r1-1][i];
                }
            }
        }
        if(temp==0)
        {
            cout << "Case #"<< ++cs << ": Volunteer cheated!" << endl;
        }
        else if(temp>1)
        {
            cout << "Case #"<< ++cs <<": Bad magician!" << endl;
        }
        else
        {
            cout << "Case #"<< ++cs <<": "<< man << endl;
        }

    }
    return 0;
}
