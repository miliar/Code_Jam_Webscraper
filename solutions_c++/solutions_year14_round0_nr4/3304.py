#include<cstdio>
#include <iostream>
#include <cstring>
#include<fstream>
#include <cstdlib>
#include <sstream>
#include <string>
#include <algorithm>
#include <cmath>
#include <vector>
#include <limits>
#define gc getchar_unlocked
#define NMAX 1561252

using namespace std;
double nm[1001], ken[1001];
int main()
{
    freopen("D-large.in","r",stdin);
    freopen("out_war.txt","w",stdout);
    int t,n,i,j,nwindw,kwinw;
    scanf("%d",&t);
    for(int tt=1; tt<=t; tt++)
    {
        scanf("%d",&n);
        for(i=0;i<n;i++)    scanf("%lf",&nm[i]);
        for(i=0;i<n;i++)    scanf("%lf",&ken[i]);
        sort(nm, nm+n);
        sort(ken, ken+n);
        //DWAR
        i=n-1, j=n-1, nwindw=0;
        while(j>-1)
        {
            if(nm[i]>ken[j]) {nwindw++; i--;j--;}
            else j--;
        }

        //WAR
         i=0, j=0; kwinw=0;
         while(j<n)
         {
             if(nm[i]<ken[j]) {kwinw++; i++; j++;}
             else j++;
         }

         printf("Case #%d: %d %d\n",tt,nwindw,(n-kwinw));
    }
    return 0;
}
