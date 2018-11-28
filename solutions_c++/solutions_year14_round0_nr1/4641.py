/*
 * Author:  mybestwishes
 * Created Time:  2014/4/12 13:54:56
 * File Name: A.cpp
 */
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <time.h>
using namespace std;
const int maxint = -1u>>1;
int n;
int first[4];
int second[4];
int grid[4][4];
int f,s;
int main() {
freopen("in.txt","r",stdin); //输入重定向，输入数据将从in.txt文件中读取 
freopen("out.txt","w",stdout); //输出重定向，输出数据将保存在out.txt文件中 
    scanf("%d", &n);
    
    for(int i = 0; i < n; i ++)
    {
        scanf("%d", &f);
        for(int j = 0; j < 4;j ++)
        {
            for(int k = 0; k < 4; k ++)
            {
                int temp;
                scanf("%d", &temp);
                if(j == f - 1)
                    first[k] = temp;
            }
        }
        scanf("%d", &s);
        for(int j = 0; j < 4;j ++)
        {
            for(int k = 0; k < 4; k ++)
            {
                int temp;
                scanf("%d", &temp);
                if(j == s - 1)
                    second[k] = temp;
            }
        }
        int same[4];
        int idx = 0;
        for(int j = 0; j < 4; j ++)
        {
            for(int k = 0; k < 4; k ++)
            {
                if(second[j] == first[k])
                {
                    same[idx ++] = second[j];
                }
            }
        }
        if(idx > 1)
            printf("Case #%d: Bad magician!\n", i + 1);
        else if(idx == 0)
            printf("Case #%d: Volunteer cheated!\n", i + 1);
        else
            printf("Case #%d: %d\n", i + 1, same[idx - 1]);
    }
    return 0;
}

