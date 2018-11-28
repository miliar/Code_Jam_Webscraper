#include<iostream>
#include<string>
#include<vector>
//#include<math.h>
//#include<utility>

using namespace std;

int main()
{
    int T;
    cin >> T;
    for(int i = 0; i < T; i++)
    {
        int smax;
        cin >> smax;
        int friends = 0;
        int stoodup = 0;
        for(int j = 0; j <= smax; j++)
        {
            char c;
            cin >> c;
            int nbnxtlvl;
            nbnxtlvl = c - '0';
            if((stoodup >= j)||(nbnxtlvl == 0))
                stoodup += nbnxtlvl;
            else
            {
                friends += j - stoodup;
                stoodup += friends + nbnxtlvl;
            }
        }
        cout << "Case #" << i+1 << ": " << friends << endl;
    }
}
