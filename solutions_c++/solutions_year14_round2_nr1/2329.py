//Google Code Jam Round 1B 2014 - Problem A.
//https://code.google.com/codejam

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<iostream>
using namespace std;

int findAns(char* str1, char* str2, int len1, int len2)
{
    char tmpCh;
    int now = 0, ans = 0, k = 0;

    for(int i = 0; i < len1;)
    {
        tmpCh = str1[i];

        //printf("sta: %d %c   %d %c\n", i, str1[i], k , str2[k]);

        if(str1[i] != str2[k])
            return -1;

        int tmp1 = 0, tmp2 = 0;

        for(int j = i; j < len1;j++)
        {
            if(str1[j] == tmpCh)
                tmp1++;
            else
            {
                i = j;
                break;
            }
            i = j;
        }

        for(int j = k; j < len2; j++)
        {
            if(str2[j] == tmpCh)
                tmp2++;
            else
            {
                k = j;
                break;
            }
            k = j;
        }
        int sub;
        sub = tmp1 > tmp2? (tmp1-tmp2):(tmp2-tmp1);
        ans += sub;

        //printf("end: %d %c   %d %c\n", i, str1[i], k , str2[k]);
        if(i == (len1-1) && k == (len2-1))
        {
            if(str1[i] == str2[k])
                break;
            else
                return -1;
        }

    }
    return ans;
}

int main()
{
    freopen ("a_output.txt","w",stdout);

    int T, N, ans;
    char str[2][105];

    scanf("%d", &T);

    for(int testCase = 1; testCase <= T; testCase++)
    {
        scanf("%d", &N);

        //the small case only have N = 2
        scanf("%s", &str[0]);
        scanf("%s", &str[1]);

        int len1 = strlen(str[0]);
        int len2 = strlen(str[1]);

        //change longer one to smaller one
        if(len1 < len2)
            ans = findAns(str[0], str[1], len1, len2);
        else
            ans = findAns(str[1], str[0], len2, len1);

        printf("Case #%d: ", testCase);
        if(ans == -1)
            printf("Fegla Won\n");
        else
            printf("%d\n", ans);
    }
    return 0;
}
