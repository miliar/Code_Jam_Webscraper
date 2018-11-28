#include <iostream>
#include <fstream>
#include <cstdio>
#include <algorithm>
using namespace std;

void Solve(int t)
{
    int d,i;
    int answer = 1;
    int maxim = -1;
    int a[1002];
    int iter;
    cin>>d;
    for(i = 1; i <= d; i++)
    {
        cin>>a[i];
        maxim = max(maxim,a[i]);
    }
     answer = maxim;
    for(iter = 2; iter < answer ; iter++)
    {
        int sum = 0;
            for(i = 1; i <= d; i++)
            {
                sum+=(a[i]-1)/iter;
            }
        answer= min(answer,sum + iter);
    }
    printf("Case #%d: %d\n",t,answer);
}
int main()
{

    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    int t;
    cin>>t;
    for(int i = 1; i <= t; i++)
    {
        Solve(i);
    }

}
