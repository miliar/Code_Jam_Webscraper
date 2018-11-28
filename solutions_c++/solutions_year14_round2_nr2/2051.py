#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <string.h>


#include <set>
#include <algorithm>

using namespace std;

typedef set<int> IntSet;
typedef IntSet::iterator iit;




void processCase(int n)
{
    
    int A, B, K;
    int R = 0;
    cin >> A;
    cin >> B;
    cin >> K;
    IntSet win;
    for (int i = 0; i < K; i++)
        win.insert(i);

    for (int i = 0; i < A; i++)
    {
        for (int j = 0; j < B; j++)
        {
            int C = i & j;
            if (win.find(C) != win.end())
            {
                R++;
//                printf("%d - %d = %d OK\n", i, j, C);
            }
        }
    }
            
    printf("Case #%d: %d\n", n, R);
}            


int main(int argc, char **argv)
{
   int N = 0;
    cin >> N;
    for (int i = 0; i < N; i++)
        processCase(i + 1);

    return 0;
}