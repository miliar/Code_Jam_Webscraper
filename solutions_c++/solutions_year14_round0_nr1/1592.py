#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
using namespace std;

#define REP(i,N) for (int i = 0; i < N; ++i)

//cout.precision(6);
//cout.setf( std::ios::fixed, std:: ios::floatfield ); // floatfield set to fixed

typedef unsigned long long int ulli;
typedef unsigned int ui;
typedef long long ll;

typedef vector<int> vi;

int main()
{
    int T;
    cin >> T;
    
    for (int csIx = 1; csIx <= T; ++csIx)
    {
        int m1[4][4], m2[4][4];
        int a1, a2;
        cin >> a1;
        REP(i,4)
        {
            REP(j,4)
            {
                cin >> m1[i][j];
            }
        }
        cin >> a2;
        REP(i,4)
        {
            REP(j,4)
            {
                cin >> m2[i][j];
            }
        }
        
        int res;
        int c = 0;
        REP(j,4)
        {
            int test = m1[a1-1][j];
            REP(j2,4)
            {
                if (m2[a2-1][j2] == test)
                {
                    res = test;
                    c++;
                }
            }
        }
        
        cout << "Case #" << csIx << ": ";
        if (c == 1)
        {
            cout << res;
        }
        else if (c == 0)
        {
            cout << "Volunteer cheated!";
        }
        else
        {
            cout << "Bad magician!";
        }
        cout << endl;
    }
    
    return 0;
}
