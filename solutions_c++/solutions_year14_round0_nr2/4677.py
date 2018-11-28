/*
 * Author:  mybestwishes
 * Created Time:  2014/4/12 14:12:12
 * File Name: B.cpp
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
int t;
double X, C, F;
double min;
double dfs(double cur_left, double fit)
{
    double first = X / fit;
    double second = C / fit;
    if(first <= second)
        return first;
    if(cur_left == 0.0)
    {
        cur_left = first - second;
        double left = dfs(cur_left, fit + F);
        if(left + second <= first)
            return left + second;
        else
            return first;
    }
    else
    {
        if(first <= cur_left && second <= cur_left)
        {
            if(first <= second)
                return first;
            else
            {
                double third = dfs(first - second, fit + F);
                if(third + second <= first)
                    return third + second;
                else
                    return first;
            }
        }
        else
        {
            if(first > cur_left && second > cur_left)
            {
                return cur_left;
            }
            else
            {
                if(first <= second)
                    return first;
                else
                {
                   if(first < cur_left)
                   { 
                    double third = dfs(first - second, fit + F);
                    if(third + second <= first)
                        return third + second;
                    else
                        return first;
                   }
                   else
                   {
                       double third = dfs(cur_left - second, fit + F);
                       if(third + second <= first)
                           return third + second;
                       else
                           return first;
                   }
                }
            }
        }
    }
   
}

int main() {
    freopen("B-small-attempt0.in","r",stdin); //输入重定向，输入数据将从in.txt文件中读取 
freopen("out.txt","w",stdout); //输出重定向，输出数据将保存在out.txt文件中 
 
    scanf("%d", &t);
    for(int i = 0; i < t; i ++)
    {
        scanf("%lf %lf %lf", &C, &F, &X);
        double ans = dfs(0.0, 2.0);
        printf("Case #%d: %.7lf\n", i+1, ans);
    }
    return 0;
}

