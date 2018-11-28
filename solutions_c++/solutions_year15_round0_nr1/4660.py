#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;
#define ll long long
#define LL long long

char str[1010];
int s;

int main()
{
    int tt;
    cin>>tt;
    int ii=1;
    while(tt--)
    {
        scanf("%d",&s);
        scanf("%s",str);
        int res=0;
        int sum=0;
        int i,j;
        for(i=0;i<=s;i++)
        {
            j=str[i]-'0';
            if(sum<i)
            {
                res+=(i-sum);
                sum=i;
            }
            sum+=j;
        }
        printf("Case #%d: %d\n",ii++,res);
    }
    return 0;
}
