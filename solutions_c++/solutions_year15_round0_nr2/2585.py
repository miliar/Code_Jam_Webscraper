#include <iostream>
#include <fstream>
#include <algorithm>
#include <math.h>
#include <queue>
#include <string>
#include <vector>
#include <unordered_map>


const int SIZE = 10;
int table[SIZE];


int main()
{
    //freopen("/Users/guanxiong/Documents/documents/google_code_jam/2015qualification/infinite_house_of_pancakes/B-small-attempt1.in","r",stdin);
    //freopen("/Users/guanxiong/Documents/documents/google_code_jam/2015qualification/infinite_house_of_pancakes/B-small-attempt1.out","w",stdout);
    int cases;
    scanf("%d", &cases);
    int nums, max_value;
    for(int case_num = 1; case_num <= cases; case_num ++)
    {
        scanf("%d", &nums);
        memset(table, 0, sizeof(table));
        max_value = 0;
        for(int i=1; i<=nums; i++)
        {
            int num;
            scanf("%d", &num);
            table[num] ++;
            max_value = std::max(max_value, num);
        }
        int min_time = max_value;
        int split_time = 0;
        while(table[4] || table[5] || table[6] || table[7] || table[8] || table[9])
        {
            if(table[9] == 1 && !table[4] && !table[5] && !table[7] && !table[8])
            {
                table[3] ++;
                table[6] ++;
                table[9] --;
            }
            else
            {
                table[max_value/2] ++;
                table[(max_value+1)/2] ++;
                table[max_value] --;
            }
            split_time ++;
            while(!table[max_value])
            {
                max_value --;
            }
            min_time = std::min(min_time, max_value + split_time);
            //printf("max_value is %d, min_time is %d, split_time is %d\n", max_value, min_time, split_time);
        }
        printf("Case #%d: %d\n", case_num, min_time);
    }
    return 0;
}

