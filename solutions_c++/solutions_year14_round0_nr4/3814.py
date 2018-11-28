//
//  main.cpp
//  codejamProblemD
//
//  Created by Vena Jia Li on 4/12/14.
//  Copyright (c) 2014 Vena Jia Li. All rights reserved.
//


#include <iostream>
#include <string>
#include <cmath>
#include <climits>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <ctime>
#include <memory.h>
using namespace std;

const int maxn=1005;
double ken[maxn];
double mao[maxn];


int Partition (double a[], int p, int r)
{
    int i = p, j = r + 1;
    double x=a[p];
    // 将< x的元素交换到左边区域
    // 将> x的元素交换到右边区域
    while (true) {
        while (a[++i] <x);
        while (a[--j] >x);
        if(i>= j) break;
        double temp=a[i];
        a[i]=a[j];
        a[j]=temp;
    }
    a[p] = a[j];
    a[j] = x;
    return j;
}

void QuickSort (double a[], int p, int r)
{
    if (p<r){
        int q=Partition(a,p,r);
        QuickSort (a,p,q-1); //对左半段排序
        QuickSort (a,q+1,r); //对右半段排序
    }
}

int main()
{
    int t;
    int n;
  
  //  freopen("/Users/vena/Documents/vena/codejam/D.txt","r",stdin);
    freopen("/Users/vena/Documents/vena/codejam/D-large.in","r",stdin);
    freopen("/Users/vena/Documents/vena/codejam/D-large-output.txt","w",stdout);
    
    scanf("%d",&t);
    for(int i=0;i<t;i++)
    {
        scanf("%d",&n);
        for(int j=0;j<n;j++)
        {
            scanf("%lf",&mao[j]);
        }
        for(int j=0;j<n;j++)
        {
            scanf("%lf",&ken[j]);
        }
        
        QuickSort(mao, 0, n-1);
        QuickSort(ken, 0, n-1);
        
        /*
        for(int j=0;j<n;j++)
        {
            cout<<mao[j]<<endl;
        }
         */
        
        int result1=0;
        int result2=0;
        
        int j=0; int k=0;
        while(1)
        {
            if(k==n) break;
            if(mao[j]<ken[k])
            {
                j++;
                k++;
            }
            else
            {
                k++;
            }
        }
        
        result1=n-j;
        
        j=0;k=0;
        while(1)
        {
            if(j==n) break;
            if(mao[j]>ken[k])
            {
                j++;
                k++;
            }
            else
            {
                j++;
            }
        }
        
        result2=k;
        
        printf("Case #%d: %d %d\n",i+1,result2,result1);
        
    }
    
    return 0;
}
