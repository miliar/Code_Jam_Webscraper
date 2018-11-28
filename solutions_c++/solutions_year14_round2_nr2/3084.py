#include<cstdio>
#include<iostream>
#include<cstring>
#include<string>
#include<cmath>
#include<vector>
#include<set>
#include<map>
#include<stack>
#include<queue>
#include<deque>
#include<list>
#include<iomanip>
#include<sstream>
#include<algorithm>
using namespace std;


int main()
{
    int test, T;

    scanf("%d", &test);
    for(T = 1; T <= test; T++)
    {
        int A, B, K;
        scanf("%d %d %d", &A, &B, &K);
        int count = 0;
        for(int I = 0; I < A; I++)
            for(int J = 0; J < B; J++)
                if((I&J) < K)
                {
                    count++;
                    //cout << I << " " << J << endl;
                }

        printf("Case #%d: %d\n", T, count);
    }

    return 0;
}
