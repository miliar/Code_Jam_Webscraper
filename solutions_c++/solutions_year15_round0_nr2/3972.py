#include<cstdio>
#include<cmath>
#include<iostream>
using namespace std;

bool cmp(int a, int b)
{
    return a < b;
}
int min(int a, int b)
{
    return a < b ? a : b;
}

int main()
{
    freopen("infinite_house_of_pancakes.txt", "r", stdin);
    freopen("question_22.txt", "w", stdout);

//    int some[9][9] = {{0, 0, 0, 0, 0, 0, 0, 0, 0},
//                      {0, 0, 0, 0, 0, 0, 0, 0, 0},
//                      {0, 0, 0, 0, 0, 0, 0, 0, 0},
//                      {0, 0, 0, 0, 0, 0, 0, 0, 0},
//                      {0, 0, 0, 0, 0, 0, 0, 0, 0},
//                      {0, 0, 0, 0, 0, 0, 0, 0, 0},
//                      {0, 0, 0, 0, 0, 0, 0, 0, 0},
//                      {0, 0, 0, 0, 0, 0, 0, 0, 0},
//                      {8, 4, 2, 2, 1, 1, 1, 1, 0}};

    int t;
    scanf("%d", &t);
    for(int k = 1; k <= t; k++)
    {
        int d;
        scanf("%d", &d);
        int sum = 0, arr[d];
        int max = 0;
        for(int i = 0; i < d; i++)
        {
            scanf("%d", &arr[i]);
            if(max < arr[i])
                max = arr[i];
        }
        int minm = 20000000;
        for(int i = 1; i <= max; i++)
        {
            int temp_sum = 0;
            for(int j = 0; j < d; j++)
            {
                double temp_div = (arr[j] * 1.0) / i;
                if(fmod(temp_div, 1) == 0)
                    temp_div--;
                int ans = temp_div;
                temp_sum += ans;
            }
            temp_sum += i;
            if(temp_sum < minm)
                minm = temp_sum;
        }

        printf("Case #%d: %d\n", k, minm);
    }
    return 0;
}
