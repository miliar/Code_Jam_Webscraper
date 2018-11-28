/*
Author:BobLee
Email:BobLee0717@gmail.com
*/

#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<cmath>
#include<map>
#include<string>
#include<vector>
using namespace std;

const int maxn = 1000+20;

int n;

double a[maxn],b[maxn];

int main()
{
    freopen("D-large.in","r",stdin);
    freopen("D-large.out","w",stdout);
    int t;
    cin>>t;
    int ca=1;
    while(t--)
    {
        cin>>n;
        for(int i=1;i<=n;i++)
            cin>>a[i];
        for(int i=1;i<=n;i++)
            cin>>b[i];

        sort(a+1,a+1+n);
        sort(b+1,b+1+n);

        int ans1 = 0;

        int i1,j1,i2,j2;
        i1=i2=1;
        j1=j2=n;

        while(i1<=j1 && i2<=j2)
        {
            if(a[j1]>b[j2])
            {
                ans1++;
                j1--,j2--;
            }
            else
            {
                i1++,j2--;
            }
        }

        int ans2=n;
        i1=i2=1;
        j1=j2=n;

        while(i1<=j1 && i2<=j2)
        {
            if(b[j2]>=a[j1])
            {
                ans2--;
                j1--,j2--;
            }
            else
            {
                i2++,j1--;
            }
        }

        printf("Case #%d: %d %d\n",ca++,ans1,ans2);


    }
    return 0;
}
