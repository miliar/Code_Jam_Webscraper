#include <iostream>
#include <string>
#include <vector>
using namespace std;

void main()
{

    int T;
    cin >> T;
    for(int C=0; C<T; ++C)
    {
        int ans;
        cin >> ans;
        int chk[4] = {0};
        for(int r=0; r<4; ++r)
        {
            int d[4] = {0};
            for(int i=0; i<4; ++i)
            {
                cin >> d[i];
                if(r+1==ans) chk[i] = d[i];
            }
        }
        int tst;
        cin >> tst;
        int found = 0;
        int correct = 0;
        for(int r=0; r<4; ++r)
        {
            int d[4] = {0};
            for(int i=0; i<4; ++i)
            {
                cin >> d[i];
                if(r+1==tst)
                {
                    for(int j=0; j<4; ++j)
                    {
                        if(chk[j]==d[i])
                        {
                            ++found;
                            correct = d[i];
                        }
                    }
                }
            }
        }
        cout << "Case #" << C+1;
        if(found == 0)
        {
            cout << ": Volunteer cheated!" << endl;            
        }
        else if(found ==1)
        {
            cout << ": " << correct << endl;
        }
        else
        {
            cout << ": Bad magician!" << endl;
        }
    }

}