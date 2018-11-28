#include<bits/stdc++.h>
#include <stdio.h>
#include <algorithm>
#include <iostream>

using namespace std;

int main() {
  freopen("in", "r", stdin);
  freopen("out", "w", stdout);
    int t,a[4][4],b[4][4],c,e,f,i,j,k,p=0;
    scanf("%d",&t);
    while(t--)

    {
        p++;   c=0;
        scanf("%d",&e);
        for(i=0;i<4;++i)
            for(j=0;j<4;++j)
            scanf("%d",&a[i][j]);
        scanf("%d",&f);
        for(i=0;i<4;++i)
            for(j=0;j<4;++j)
            scanf("%d",&b[i][j]);
        for(i=0;i<4;i++)
            for(j=0;j<4;++j)
        {
            if(a[e-1][i]==b[f-1][j]){
                c++;
                k=a[e-1][i];}
        }
        if(c==0)
            printf("Case #%d: Volunteer cheated!\n",p);
        else if(c==1)
            printf("Case #%d: %d\n",p,k);
        else
            printf("Case #%d: Bad magician!\n",p);



    }

        return 0;

  }
