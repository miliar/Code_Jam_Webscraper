#include <algorithm>
#include <iostream>
#include <cstdio>

using namespace std;

int T; int N, X;

int disc[20000];
int file[20000];

int Ans;

int main()
{
     freopen("A-large.in", "r", stdin);
     freopen("A-large.out", "w", stdout);
     scanf("%d", &T);

    for(int Ti = 1; Ti <= T; Ti++)
    {
        scanf("%d %d", &N, &X);

        for(int Ni = 0; Ni < N; Ni++)
            scanf("%d", &file[Ni]);

        sort(file, file+N);

        int l = 0, r = N-1; Ans = 0;

        while( l <= r )
        {
            while( l < r && file[l]+file[r] > X ) Ans++, r--;
            l++; Ans++; r--;
        }

        printf("Case #%d: %d\n", Ti, Ans);
    }
}
