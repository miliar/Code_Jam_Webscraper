#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <ctype.h>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <iostream>
#include <string>
#include <queue>
#include <stack>

#define sqr(x) (x*x)
#define cube(x) (x*x*x)

using namespace std;

double block1[1001],block2[1001];
bool check[1001];

bool comp(double a,double b) { return a>b; }

int main()
{
    freopen("D-large.in","r",stdin);
    freopen("D-large.out","w",stdout);
    int t,n;
    cin>>t;
    for (int i=1; i<=t; i++)
    {
        cin>>n;
        for (int j=0; j<n; j++)
            cin>>block1[j];
        for (int j=0; j<n; j++)
            cin>>block2[j];
        int war=0,dwar=0;

        sort(block1,block1+n);
        sort(block2,block2+n);
        memset(check,false,sizeof(check));
        for (int j=0; j<n; j++)
            for (int k=0; k<n; k++)
                if (!check[k] && block1[k]>block2[j])
                {
                    check[k]=true;
                    dwar++;
                    break;
                }

        sort(block1,block1+n,comp);
        sort(block2,block2+n,comp);
        memset(check,false,sizeof(check));
        for (int j=0; j<n; j++)
            for (int k=0; k<n; k++)
                if (!check[k] && block2[j]>block1[k])
                {
                    check[k]=true;
                    war++;
                    break;
                }
        war=n-war;

        printf("Case #%d: ",i);
        cout<<dwar<<" "<<war<<endl;
    }

    return 0;
}
