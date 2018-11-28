#include <stdio.h>
#include <math.h>
#include <iostream>
#include <algorithm>
using namespace std;


double nPoints[1007] , kPoints[1007];
int vis[1007] , True;
int n;

int main()
{
    freopen("D.in","rt",stdin);
    freopen("D.out","wt",stdout);

    int tst,cas;
    scanf("%d",&tst);
    for(cas=1;cas<=tst;cas++)
    {
        scanf("%d",&n);
        for(int i=0;i<n;i++)    scanf("%lf",&nPoints[i]);
        for(int i=0;i<n;i++)    scanf("%lf",&kPoints[i]);
        True++;
        sort( nPoints , nPoints+n);
        sort( kPoints , kPoints+n);

        int dScore = 0 , wScore = 0;

        for(int i=0;i<n;i++) {
            bool fn = false;
            for(int j=0;j<n;j++) {
                if(vis[j]!=True && nPoints[i] < kPoints[j]) fn = true;
            }
            if(fn) {
                for(int j=0;j<n;j++) {
                    if(vis[j]!=True && nPoints[i] < kPoints[j])
                    {
                        vis[j] = True;
                        break;
                    }
                }
            }
            else {
                wScore++;
                for(int j=0;j<n;j++) {
                    if(vis[j]!=True)
                    {
                        vis[j] = True;
                        break;
                    }
                }
            }

        }


        True++;

        for(int i=0;i<n;i++) {
            bool fn = false;
            for(int j=0;j<n;j++) {
                if(vis[j]!=True && nPoints[i] > kPoints[j]) fn = true;
            }
            if(fn) {
                dScore++;
                for(int j=0;j<n;j++) {
                    if(vis[j]!=True && nPoints[i] > kPoints[j]) {
                        vis[j] = True;
                        break;
                    }
                }
            }
            else {
                for(int j=n-1;j>=0;j--) {
                    if(vis[j]!=True) {
                        vis[j] = True;
                        break;
                    }
                }
            }

        }


        printf("Case #%d: %d %d\n",cas,dScore , wScore);




    }


    return 0;
}
