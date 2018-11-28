#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <algorithm>
#include <iostream>
#include <string.h>

using namespace std;

typedef pair<int, int> ii;

int a,n;
int t;
vector <int> mote;
int dp[102][205];
int minx;


ii hitung(int a, int b)
{
     int htg=0;
     
     while (a<=b)
     {
         a=(a*2)-1;
         htg+=1;
     }
     
     ii hsl;
     hsl.first=a;
     hsl.second=htg;
     
     return hsl;
     
}

void cari(int ps, int bilx, int turn)
{
     if (ps==n)
     {
         if (minx==-1) minx=turn;
         else
         if (minx > turn) minx=turn;
     }
     else
     if (dp[ps][bilx] ==-1)
     {
         dp[ps][bilx]=turn;
         
         ii nxt=hitung(bilx, mote[ps]);
         
//         cout << ps << " " << nxt.first << " " << nxt.second << endl;
         
         cari(ps+1,nxt.first+mote[ps],turn+nxt.second);
         cari(ps+1,bilx,turn+1);
         
     }
     else
     if (dp[ps][bilx] !=-1)
     {
         if (dp[ps][bilx] > turn)
         {
             dp[ps][bilx]=turn;
         
             ii nxt=hitung(bilx, mote[ps]);
         
         
             cari(ps+1,nxt.first+mote[ps],turn+nxt.second);
             cari(ps+1,bilx,turn+1);
         
         }
     }
}


int main ()
{
    scanf("%d",&t);
    for (int z=1; z<=t; z++)
    {
        scanf("%d%d",&a,&n);
        
        mote.clear();
        memset(dp,-1,sizeof(dp));
        minx=-1;
        
        
        int bil;
        for (int i=0; i<n; i++)
        {
            scanf("%d",&bil);
            mote.push_back(bil);
        }
        
        sort(mote.begin(), mote.end());
        
        /*
        for (int i=0; i<n; i++) printf("%d ",mote[i]);
        printf("\n");
        */
        mote.push_back(0);
        
        
        if (a==1) printf("Case #%d: %d\n",z,n);
        else
        {
        
        cari(0,a,0);
        
        printf("Case #%d: %d\n",z,minx);
        }
    }
    
//    system("pause");
    return 0;
}
