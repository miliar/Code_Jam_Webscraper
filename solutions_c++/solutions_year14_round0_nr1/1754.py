#include<stdio.h>
#include<iostream>
using namespace std;

#include<math.h>
#include<algorithm>
#include<string.h>
#include<stdlib.h>
#include<vector>
#include<set>
#include<map>
#include<stack>
#include<string>
#include<queue>

#define repA(p,q,i)  for( int (i)=(p); (i)!=(q); ++(i) )
#define repAE(p,q,i)  for( int (i)=(p); (i)<=(q); ++(i) )
#define repD(p,q,i)  for( int (i)=(p); (i)!=(q); --(i) )
#define repDE(p,q,i)  for( int (i)=(p); (i)>=(q); --(i) )

#define range 110

bool mp[range][range];

int it[range];  // i的point为it[i] 
int dp[range];  //记录dp后的point 
int f[range];  //节点i的父节点f[i] 
bool th[range];  //是否能到达th[i] 


void MAIN();

int mp1[5][5];
int mp2[5][5];

int main()
{
    freopen("0000.in", "r", stdin);
    freopen("0000.out", "w", stdout);
    MAIN();
    fclose(stdout);
    
    return 0;
}



void MAIN()
{
     int test; scanf("%d", &test);
     int a,b,all,dot;
     repAE(1,test,rd)
     {
         scanf("%d", &a);
         repA(0,4,i)
           repA(0,4,j)
           scanf("%d", &mp1[i][j]);
           
         scanf("%d", &b);
         repA(0,4,i)
           repA(0,4,j)
           scanf("%d", &mp2[i][j]);  
           
           
         all = 0;
         --a; --b;
         repA(0,4,i)
           repA(0,4,j)
           if(mp1[a][i] == mp2[b][j])
           {
               ++all;
               dot = mp1[a][i];             
           }
           
         printf("Case #%d: ", rd);
         if(all == 0)  printf("Volunteer cheated!\n");
         else if(all == 1)  printf("%d\n", dot);
         else printf("Bad magician!\n");    
     }
     
     return;
}

