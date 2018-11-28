#include <iostream>
#include <fstream>
#include <algorithm>
#include <math.h>
#include <queue>
#include <string>
#include <vector>
#include <unordered_map>


const int SIZE = 1002;
//char line[SIZE];
int arr[SIZE];


int main()
{
    //freopen("/Users/guanxiong/Documents/documents/google_code_jam/2015qualification/standing_ovation/A-small-attempt1.in","r",stdin);
    //freopen("/Users/guanxiong/Documents/documents/google_code_jam/2015qualification/standing_ovation/A-small-attempt1.out","w",stdout);
    int cases;
    scanf("%d", &cases);
    int level, len;
    for(int case_num = 1; case_num <= cases; case_num ++)
    {
        scanf("%d", &level);
        getchar();
        for(int i=0; i<=level; i++)
        {
            char c;
            scanf("%c", &c);
            arr[i] = c - '0';
        }
        int sum = 0;
        for(int i=0; i<level; i++)
        {
            if(i > 0)
            {
                arr[i] += arr[i-1];
            }
            if(arr[i] < i+1)
            {
                sum += i+1-arr[i];
                arr[i] = i+1;
            }
        }
        printf("Case #%d: %d\n", case_num, sum);
    }
    return 0;
}

