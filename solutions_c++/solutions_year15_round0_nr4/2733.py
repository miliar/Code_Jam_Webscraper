#include <iostream>
#include <string>
using namespace std;

int main()
{
    std::ios::sync_with_stdio(false);

    bool testing = false;

    //Solving runs
    if(!testing)
    {
        int T;

        cin >> T;

        for(int testcase = 0;testcase<T;testcase++)
        {
            int X,R,C;
            cin >> X;
            cin >> R;
            cin >> C;

            if(X >= 7) //selecting a self cloding piece
            {
                cout << "Case #" << testcase + 1 << ": RICHARD" << endl;
            }
            else if((R*C)%X != 0) //size does not allow any tiling
            {
                cout << "Case #" << testcase + 1 << ": RICHARD" << endl;
            }
            else if(max(R,C) < X) //choosing an X by 1 will win here
            {
                cout << "Case #" << testcase + 1 << ": RICHARD" << endl;
            }
            else if(min(R,C) < (X+1)/2 ) //can select a shape that cannot fit onto the grids dimensions
            {
                cout << "Case #" << testcase + 1 << ": RICHARD" << endl;
            }
            else if(X == 1 or X == 2 or X == 3)
            {
                cout << "Case #" << testcase + 1 << ": GABRIEL" << endl;
            }

            //cases for X4
            else if(X==4 and (R==2 or C==2))
            {
                cout << "Case #" << testcase + 1 << ": RICHARD" << endl;
            }
            else if (X==4)
            {
                cout << "Case #" << testcase + 1 << ": GABRIEL" << endl;
            }

            //cases for X5
            else if(X==5 and (R==3 or C==3))
            {
                cout << "Case #" << testcase + 1 << ": RICHARD" << endl;
            }
            else if (X==5)
            {
                cout << "Case #" << testcase + 1 << ": GABRIEL" << endl;
            }

            else if(X==6 and (R==3 or C==3))
            {
                cout << "Case #" << testcase + 1 << ": RICHARD" << endl;
            }
            else if (X==6)
            {
                cout << "Case #" << testcase + 1 << ": GABRIEL" << endl;
            }

        }
    }
    //pre-processing or testing
    else
    {
        int missing = 0;
        int limit = 20;
        for(int X = 1;X<=limit;X++)
        {
            for(int R = 1;R<=limit;R++)
            {
                for(int C = 1;C<=limit;C++)
                {
                    if(X >= 7) //selecting a self cloding piece
                    {
                        // can pick
                    }
                    else if((R*C)%X != 0) //size does not allow any tiling
                    {
                        //can pick
                    }
                    else if(max(R,C) < X) //choosing an X by 1 will win here
                    {
                        //can pick
                    }
                    else if(min(R,C) < (X+1)/2 ) //can select a shape that cannot fit onto the grids dimensions
                    {
                        //can pick
                    }
                    else if(X == 1 or X == 2 or X == 3)
                    {
                        //no pick
                    }

                    //cases for X4
                    else if(X==4 and (R==2 or C==2))
                    {
                        //can pick
                    }
                    else if (X==4)
                    {
                        //no pick
                    }
                    //cases for X5
                    else if(X==5 and (R==3 or C==3))
                    {
                        //can pick
                    }
                    else if (X==5)
                    {
                        //no pick
                    }

                    else if(X==6 and (R==3 or C==3))
                    {
                        //can pick
                    }
                    else if (X==6)
                    {
                        //no pick
                    }

                    else
                    {
                        cout << X << " " << R << " " << C << " Has no solution" << endl;
                        missing++;
                    }
                }
            }
        }
        cout << "Missing cases: " << missing << endl;
    }

    return 0;
}
