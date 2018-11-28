#include <iostream>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <ctype.h>
#include <algorithm>
#include <vector>

using namespace std;

double a[1001],b[1001];
int n;

bool cmp(double a,double b)
{
    return a > b;
}

void deal1()
{
    int al=0,bl=0,ah=n-1,bh=n-1;
    int ans=0;
    for(int i=0; i<n; i++)
    {
        if(a[al]>b[bl])
        {
            ans++;
            al++;
            bl++;
        }
        else if(a[al]<b[bl])
        {
            ah--;
            bl++;
        }
        else
        {
            if(a[ah]>b[bh])
            {
                ans++;
                ah--;
                bh--;
            }
            else if(a[ah]<b[bh])
            {
                ah--;
                bl++;
            }
            else
            {
                if(a[al]==a[ah])
                {
                    al++;
                    bl++;
                }
                else
                {
                    ah--;
                    bl++;
                }
            }
        }
    }
    cout<<ans<<" ";
}

void deal2()
{
    int al=0,bl=0,ah=n-1,bh=n-1;
    int ans=0;
    for(int i=0; i<n; i++)
    {
        if(b[bl]>a[al])
        {
            bl++;
            al++;
        }
        else if(b[bl]<a[al])
        {
            bh--;
            al++;
            ans++;
        }
        else
        {
            al++;
            bh--;
        }
    }
    cout<<ans<<endl;
}

int main()
{
    freopen("1.in","r",stdin);
    freopen("2.txt","w",stdout);
    int T;
    cin>>T;
    for(int l=1; l<=T; l++)
    {
        memset(a,0,sizeof(a));
        memset(b,0,sizeof(b));
        cin>>n;
        for(int i=0; i<n; i++)
            cin>>a[i];
        for(int i=0; i<n; i++)
            cin>>b[i];
        sort(a,a+n,cmp);
        sort(b,b+n,cmp);
        printf("Case #%d: ",l);
        deal1();
        deal2();
    }
    return 0;
}
