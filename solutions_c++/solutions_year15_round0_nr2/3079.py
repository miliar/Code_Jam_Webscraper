#include <iostream>
#include <stdlib.h>
#include <algorithm>
#include <fstream>
#include <cmath>
#include <stdio.h>
#define maxd 1005
#define maxp 1005
using namespace std;
int t,n,a[maxd];
int main()
{
    fstream in("B-large.in");
    FILE* out=fopen("1.out","w");
    int iCase=0,d,ans;
    //cin>>t;
    in>>t;
    while(t--)
    {
        //cin>>d;
        in>>d;
        for (int i=1;i<=d;i++)
        {
            //cin>>a[i];
            in>>a[i];
        }
        sort(a+1,a+d+1);
        ans=a[d];
        for (int i=1;i<=a[d]-1;i++)
        {
            int c=0;
            for (int j=1;j<=d;j++)
            if (a[j]>i)
            {
                c+=a[j]/i+(int)(a[j]%i>0)-1;
            }
            ans=min(ans,c+i);
        }
        fprintf(out,"Case #%d: %d\n",++iCase,ans);
    }
    return 0;
}
