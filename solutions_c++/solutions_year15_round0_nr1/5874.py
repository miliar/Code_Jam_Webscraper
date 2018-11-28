/*
Shamim Ehsan
SUST CSE 12
*/
#include<stdio.h>
#include<string.h>
#include<ctype.h>
#include<math.h>
#include<stdlib.h>
#include<limits.h>
#include<iostream>
#include<string>
#include<vector>
#include<stack>
#include<queue>
#include<map>
#include<set>
#include<deque>
#include<algorithm>
#include<sstream>
#define PI (2* acos(0))
#define pb push_back
#define ll long long
using namespace std;
//int X[]= {0,0,1,-1};
//int Y[]= {-1,1,0,0};
//int X[]= {0,0,1,1,1,-1,-1,-1};
//int Y[]= {-1,1,0,1,-1,0,1,-1};
int main()
{
    int t,n;
    char  arr[1500];
    int ans =0;
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);

    scanf("%d",&t);
    for(int cs=1;cs<=t;cs++)
    {
        scanf("%d %s",&n,&arr);
        int current=arr[0]-'0',ans=0;
        for(int i=1;i<=n;i++)
        {
//            cout<<current<<endl;
            if(current<i)
            {
                ans+=(i-current);
                current+=(i-current);

            }
            current+=(arr[i]-'0');

        }
        printf("Case #%d: %d\n",cs,ans);
    }

    return 0;
}


