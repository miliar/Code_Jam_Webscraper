#include <cstdio>
#include <cstdlib>
#include <vector>
#include <map>
#include <set>
#include <iostream>
#include <algorithm>
using namespace std;



int main(int argc, char* args[])
{
    size_t T;
    cin >> T;
    for(size_t t = 0; t != T; ++t)
    {
        //cout << "t: " << t << endl;
        int A;
        cin >> A;
        int N;
        cin >> N;
        vector<int> Ms(N);
        vector<size_t> supposedInsertionsCount(N);

        //cout << "A: " << A <<"  N: "<< N << endl;
        for(size_t i = 0; i != N; ++i)
        {
            cin >> Ms[i];
            //cout << "  Ms[" << i <<"]:" << Ms[i];
        }
        //cout << endl;
        sort(Ms.begin(), Ms.end());

        size_t additions = 0;
        if(A == 1)
        {
            additions = N;
        }
        else
        {
            for(size_t i = 0; i != N; ++i)
            {
                if(A > Ms[i])
                {
                    A += Ms[i];
                }
                else
                {
                    supposedInsertionsCount[i] = 0;
                    while(A <= Ms[i])
                    {
                        ++supposedInsertionsCount[i];
                        //cout << "Need to insert " << A-1 << " brfore absorbing " << Ms[i] << endl; 
                        A += A-1;
                    }
                    A += Ms[i];
                }
            }
            vector<size_t> cummulativeRemainingSupposedInsertionsCount(N);
            for(int i = N-1; i >= 0; --i)
            {
                cummulativeRemainingSupposedInsertionsCount[i] = ((i < (N-1)) ? cummulativeRemainingSupposedInsertionsCount[i+1] : 0) + supposedInsertionsCount[i];
            }
            vector<size_t> cummulativeNeededSupposedInsertionsCount(N);
            for(size_t i = 0; i != N; ++i)
            {
                cummulativeNeededSupposedInsertionsCount[i] = ((i > 0) ? cummulativeNeededSupposedInsertionsCount[i-1] : 0) + supposedInsertionsCount[i];
            }

            int lastIndex = -1;
            for(size_t i = 0; (i != N); ++i)
            {
                if(supposedInsertionsCount[i] == 0)
                {
                    lastIndex = i;
                    continue;
                }

                if(cummulativeRemainingSupposedInsertionsCount[i] > (N-i))
                {
                    break;
                }
                lastIndex = i;
            }
                // int lastIndex = N-1;
                // size_t savedDeletions = 0;
                // for(int i = N-1; i != -1; --i)
                // {
                //     if(supposedInsertionsCount[i] == 0)
                //     {
                //         lastIndex = i;
                //         continue;
                //     }
                //     if(!(cummulativeRemainingSupposedInsertionsCount[i] <= (N-i)))
                //     {
                //         break;
                //     }
                //     else
                //     {
                //         lastIndex = i;
                //     }
                // }

            additions = (lastIndex >= 0 ?  cummulativeNeededSupposedInsertionsCount[lastIndex] : 0) + (N - 1 - lastIndex);
        }
        cout << "Case #" << t+1 << ": " << additions << endl;
    }

    return 0;
}