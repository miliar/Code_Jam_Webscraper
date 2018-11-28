#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;
#define MAX 10000
double mass1[1005];
double mass2[1005];
int count2[1005];
int main()
{
    FILE *fp = fopen("D-large.in", "r");
    FILE *fo = fopen("output.out", "w");
    //FILE *fp = stdin;
    //FILE *fo = stdout;
    int t;
    int n;
    fscanf(fp, "%d", &t);
    for (int i = 1; i <= t; i++)
    {
        memset(mass1, 0, sizeof(mass1));
        memset(mass2, 0, sizeof(mass2));
        memset(count2, 0, sizeof(count2));
        fscanf(fp, "%d", &n);
        for (int j = 0; j < n; j++)
        {
            fscanf(fp, "%lf", mass1+j);
        }
        for (int j = 0; j < n; j++)
        {
            fscanf(fp, "%lf", mass2+j);
        }
        sort(mass1, mass1+n);
        sort(mass2, mass2+n);
        mass2[n] = MAX;
        int ans1 = 0;
        int ans2 = 0;
        int k = 0;
        for (int j = 0; j < n && k <= n; )
        {
            if (mass1[j] < mass2[k])
            {
                count2[k]++;
                j++;
            }
            else
            {
                k++;
            }
        }
        k = n-1;
        int sum2 = 1;
        int sum1 = 0;
        while (1)
        {
            if (k == 0)
                break;
            if (count2[k] >= 2 && count2[k]+sum1 > sum2)
            {
                ans1 += count2[k]+sum1 - sum2;
                sum1 = 0;
                sum2 = 1;
                k--;
            }
            else
            {
                sum1 += count2[k];
                sum2++;
                k--;
            }
        }
        ans1 += count2[n];
        int p1, p2;
        p1 = 0;
        p2 = 0;
        k = n-1;
        while (1)
        {
            if (p2 > k)
                break;
            if (mass1[p1] > mass2[p2])
            {
                ans2 += 1;
                p1++;
                p2++;
            }
            else
            {
                p1++;
                k--;
            }
        }
//        for (k++; k <= n; k++)
//        {
//            ans2 += count2[k];
//        }
        fprintf(fo, "Case #%d: %d %d\n", i, ans2, ans1);
    }
    return 0;
}
