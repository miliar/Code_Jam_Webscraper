#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <string.h>
#include <stdio.h>
#include <math.h>

using namespace std;

//#define MY_DEBUG

int main(void)
{
    int T=0, loop=0;

    cin >> T;
    
#ifdef MY_DEBUG
    printf("=> T=%d\n", T);
#endif

    while (++loop <= T)
    {
        long long A = 0;
        int N = 0;
        int pre_op = 0;
        int op = 0;
        vector<long long> mote;

        cin >> A;
        cin >> N;
#ifdef MY_DEBUG
    printf("=> A=%d, N=%d\n", (int)A, N);
#endif

        for (int i=0; i<N; i++)
        {
            long long data;
            cin >> data;
            mote.push_back(data);
        }
        std::sort(mote.begin(), mote.end());
#ifdef MY_DEBUG
        for (int i=0; i<N; i++)
            printf("=> mote[%d]=%d\n", i, (int)mote[i]);
#endif

        for (int i=0; i<N;)
        {
#ifdef MY_DEBUG
printf("=> step %d\n", i);
#endif
            if (A > mote[i])
            {
                A += mote[i];
                pre_op = op;
                i++;
#ifdef MY_DEBUG
printf("=>   i=%d, A=%d\n", i, (int)A);
#endif
                continue;
            }
            
            if (1)//((A + (A-1)) > mote[i])
            {
#ifdef MY_DEBUG
printf("=>   A=%d, mote[i]=%d\n", (int)A, (int)mote[i]);
#endif
                A += (A-1);
                op++;
#ifdef MY_DEBUG
printf("=>   i=%d, A=%d, op=%d\n", i, (int)A, op);
#endif
                if ( (op-pre_op) >= (N-i) )
                {
#ifdef MY_DEBUG
printf("=>   pre_op=%d, op=%d\n", pre_op, op);
#endif
                    break;
                }
                continue;
            }
            // remote mote[i]
            op++;
            i++;
            pre_op = op;
#ifdef MY_DEBUG
printf("=> i=%d, op=%d, remove mote[%d]=%d\n", i, (int)A, op, i, (int)mote[i]);
#endif
        }

        printf("Case #%d: %d\n", loop, op);
    }

    return 0;
}
