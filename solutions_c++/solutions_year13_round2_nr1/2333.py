#include <algorithm>
#include <iostream>
#include <cstdio>

const int maxn = 100;

int T;
int N;
int A;
int motes[maxn];

int
solve()
{
    int retval(0);
    
    std::sort(motes, motes + N);
    for (int n = 0; n < N; ++n)
    {
        //printf("A:%d motes[n]:%d\n", A, motes[n]);
        
        if (A > motes[n])
        {
            A += motes[n];
        }   // if
        else
        {
            int left(N - n);
            if (left == 1)
            {
                return retval + 1;
            }
            
            //printf("%d (%d): zbyva: %d\n", n, motes[n], left);
            int tmpA = A;
            int preadded(0);
            for (int i = 0; i < left; ++i)
            {
                if (tmpA > motes[n])
                {
                    preadded = i;
                    break;
                }   // if
                tmpA += tmpA - 1;
            }   // for
            
            if (preadded == 0)
            {
                //printf("preadedzero\n");
                return retval + left;
            }   // if
            
            if (preadded >= left)
            {
                if (left + retval > N)
                {
                    //printf("N\n");
                    return N;
                }
                //printf("left\n");
                return left;
            }   // if
            else
            {
                //printf("pricitam k A preadded: %d\n", preadded);
                A = tmpA + motes[n];
                retval += preadded;
            }
        }
    }   // for
    //printf("natural\n");
    return retval;
}   // solve

int
main(
    int argc,
    char *argv[]
)
{
    std::cin >> T;
    for (int t = 1; t <= T; ++t)
    {
        std::cin >> A >> N;
        for (int n = 0; n < N; ++n)
        {
            std::cin >> motes[n];
        }   // for
        
        printf("Case #%d: %d\n", t, solve());
    }   // for
    return 0;
}   // main
