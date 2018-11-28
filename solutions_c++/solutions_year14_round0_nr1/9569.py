#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<math.h>
#include<cstdio>
#include<bits/stdc++.h>
using namespace std;
int ar[6][6];
int br[6][6];
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.out","w",stdout);
    int tc,r,c,r1,r2,i,j,k,f,cs=1;
    cin>>tc;
    while(tc--)
    {
        cin>>r1;
        r1--;

        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
               cin>>ar[i][j];
        }
        cin>>r2;
        r2--;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
               cin>>br[i][j];
        }

        int ans=0,cnt=0;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
              if(ar[r1][i]==br[r2][j])
              {
                  cnt++;
                  ans=ar[r1][i];
              }
            }
        }
        printf("Case #%d: ",cs++);
        if(cnt==1)
            cout<<ans<<endl;

        else if(cnt>1)
            printf("Bad magician!\n");

        else printf("Volunteer cheated!\n");

    }
    return 0;
}
