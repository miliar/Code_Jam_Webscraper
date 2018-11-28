/*
 * Author:  mybestwishes
 * Created Time:  2014/4/12 15:54:21
 * File Name: D.cpp
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
bool cmp(int a, int b)
{
    return a < b;
}
int main() {
    freopen("D-large.in","r",stdin); //输入重定向，输入数据将从in.txt文件中读取 
    freopen("out.txt","w",stdout); //输出重定向，输出数据将保存在out.txt文件中 
 
   
    int t, n;
    double first[1001], second[1001];
    scanf("%d", &t);
    for(int i = 0; i < t; i ++)
    {
        scanf("%d", &n);
        for(int j = 0; j < n; j ++)
            scanf("%lf", &first[j]);
        for(int j = 0; j < n; j ++)
            scanf("%lf", &second[j]);
        sort(first ,first + n);
        sort(second, second + n);
        int j = n - 1, k = n-1;
        int tt = 0;
        int ss = 0;
        while(j > -1 && k > -1)
        {
            if(first[j] > second[k])
            
            {
                tt ++;
                j --;k--;    
            }
            else
            {
                k --;
            }
        }
        j = n - 1; k = n-1;
        while(j > -1 && k > -1)
        {
            if(first[j] < second[k])
            {
                ss ++;
                j --;
                k --;
            }
            else
                j --;
        }
        printf("Case #%d: %d %d\n", i + 1, tt, n - ss);
    }
    return 0;
}

