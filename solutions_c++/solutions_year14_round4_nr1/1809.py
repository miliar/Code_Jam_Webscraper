//Google Code Jam Round 2 2014 - Problem A.
//https://code.google.com/codejam

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<algorithm>
#include<iostream>
using namespace std;

int main()
{
    freopen ("a_output.txt","w",stdout);

    int T, N, X, s[10001], ans;

    scanf("%d", &T);

    for(int testCase = 1; testCase <= T; testCase++)
    {
        printf("Case #%d: ", testCase);

        scanf("%d %d", &N, &X);

        for(int i = 0; i < N; i++)
            scanf("%d", &s[i]);
        sort(s, s+N);
        /*
        for(int i = 0; i < N; i++)
            printf("%d ", s[i]);
        printf("\n");
        */
        int start = 0, end = N - 1;
        ans = 0;

        while(start <= end){
            if(start == end){
                ans ++;
                break;
            }

            if(s[start] + s[end] <= X){
                start ++;
                end --;
                ans ++;
            }
            else if(s[start] + s[end] > X){
                end --;
                ans ++;
            }

        }
        printf("%d\n", ans);

    }
    return 0;
}

