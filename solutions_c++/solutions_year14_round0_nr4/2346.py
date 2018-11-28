#include <iostream>
#include <algorithm>
#include <map>
#include <vector>
#include <set>
#include <stdio.h>
#include <string>
#include <queue>
#include <iterator>

using namespace std;


int main()
{
    freopen ("input.txt","r",stdin);
    freopen ("output.txt","w",stdout);

    int T;

    cin >> T;

    for(int t = 0; t < T; ++t)
    {

        int N, W = 0, DW = 0;

        cin >> N;

        vector<double> Naomi(N), Ken(N);

        for(int i = 0; i < N; ++i)
        {
            cin >> Naomi[i];
        }

        for(int i = 0; i < N; ++i)
        {
            cin >> Ken[i];
        }

        sort(Naomi.begin(), Naomi.end());
        sort(Ken.begin(), Ken.end());

        int count = -1;

        for(int i = 0; i < N; ++i)
        {
            if(Naomi[i] > Ken[count + 1])
            {
                ++DW;
                ++count;
            }
        }

        count = -1;

        for(int i = 0; i < N; ++i)
        {
            if(Ken[i] > Naomi[count + 1])
            {
                ++W;
                ++count;
            }
        }

        printf("Case #%d: %d %d\n", t + 1, DW, N - W);

    }

    return 0;
}

//int main()
//{
//    freopen ("input.txt","r",stdin);
//    freopen ("output.txt","w",stdout);
//
//    int T;
//
//    cin >> T;
//
//    for(int t = 0; t < T; ++t)
//    {
//        int N, M, K;
//
//        cin >> N >> M >> K;
//
//        printf("Case #%d:\n", t + 1);
//
//        vector< vector<char> > Answer(N, vector<char>(M));
//
//        for(int i = 0; i < N; ++i)
//        {
//            for(int j = 0; j < M; ++j)
//            {
//                Answer[i][j] = '.';
//            }
//        }
//
//        if(N * M - K == 1)
//        {
//            for(int i = 0; i < N; ++i)
//            {
//                for(int j = 0; j < M; ++j)
//                {
//                    Answer[i][j] = '*';
//                }
//            }
//            
//            Answer[0][0] = 'c';
//            
//            for(int i = 0; i < N; ++i)
//            {
//                for(int j = 0; j < M; ++j)
//                {
//                    printf("%c", Answer[i][j]);
//                }
//                printf("\n");
//            }
//            continue;
//        }
//
//
//
//
//
//        for(int i = 0; i < N; ++i)
//        {
//            for(int j = 0; j < M; ++j)
//            {
//                printf("%c", Answer[i][j]);
//            }
//            printf("\n");
//        }
//
//
//    }
//
//    return 0;
//}