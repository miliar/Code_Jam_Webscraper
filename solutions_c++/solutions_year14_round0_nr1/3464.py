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

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    int n,t,x,i,cnt,com,a,j,b;
    int arr1[5],arr2[5];
    scanf("%d",&t);
    for(int tt=1;tt<=t;tt++)
    {
        scanf("%d",&a);
        x=1;
        switch(x)
        {
            case 1: if(a==1) {for(i=0;i<4;i++) scanf("%d",&arr1[i]); }
                    else for(i=0;i<4;i++) scanf("%d",&b);

            case 2: if(a==2) {for(i=0;i<4;i++) scanf("%d",&arr1[i]); }
                    else for(i=0;i<4;i++) scanf("%d",&b);

            case 3: if(a==3) {for(i=0;i<4;i++) scanf("%d",&arr1[i]); }
                    else for(i=0;i<4;i++) scanf("%d",&b);

            case 4: if(a==4) {for(i=0;i<4;i++) scanf("%d",&arr1[i]); }
                    else for(i=0;i<4;i++) scanf("%d",&b);
        }
        scanf("%d",&a);
        x=1;
        switch(x)
        {
            case 1: if(a==1) {for(i=0;i<4;i++) scanf("%d",&arr2[i]); }
                    else for(i=0;i<4;i++) scanf("%d",&b);

            case 2: if(a==2) {for(i=0;i<4;i++) scanf("%d",&arr2[i]); }
                    else for(i=0;i<4;i++) scanf("%d",&b);

            case 3: if(a==3) {for(i=0;i<4;i++) scanf("%d",&arr2[i]); }
                    else for(i=0;i<4;i++) scanf("%d",&b);

            case 4: if(a==4) {for(i=0;i<4;i++) scanf("%d",&arr2[i]); }
                    else for(i=0;i<4;i++) scanf("%d",&b);
        }
        cnt=0;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                if(arr1[i]==arr2[j])
                {
                    com=arr1[i]; cnt++;
                }
            }

        }
        if(cnt==0)  printf("Case #%d: Volunteer cheated!\n",tt);
        else if(cnt==1) printf("Case #%d: %d\n",tt,com);
        else printf("Case #%d: Bad magician!\n",tt);

    }
}
