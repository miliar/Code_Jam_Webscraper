#include<iostream>
#include"stdlib.h"
#include<cmath>
using namespace std;
int CountPair(long start,long end);
bool CheckPair(long len);

int main()
{
    int case_num = 0;
    cin >> case_num;
    int * results = new int[case_num];
    for (int case_index = 0; case_index < case_num; ++case_index)
    {
        long start, end;
        cin >> start >> end;
        results[case_index] = CountPair(start, end);
    }

    for (int i = 0; i < case_num; ++i)
    {
        printf("Case #%d: %d\n", i + 1, results[i]);
    }
    return 0;
}

int CountPair(long start, long end)
{
    int count = 0;
    for (long i = start; i <= end; ++i)
    {
        int s = sqrt(i);
        if(s * s == i && CheckPair(s) && CheckPair(i))
            count ++;
    }
    return count;
}

bool CheckPair(long i)
{
    char str[128];
    sprintf(str, "%ld", i);
    for ( int i = 0; i < strlen(str) / 2; i ++)
    {
        if(str[i] != str[strlen(str) - i - 1])
            return false;
    }
    return true;
}
