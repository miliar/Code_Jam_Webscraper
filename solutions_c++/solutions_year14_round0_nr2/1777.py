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

int it[range];  // i��pointΪit[i] 
int dp[range];  //��¼dp���point 
int f[range];  //�ڵ�i�ĸ��ڵ�f[i] 
bool th[range];  //�Ƿ��ܵ���th[i] 


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
     double c,f,x,tall,cf,rc,t1,t2;
     repAE(1,test,rd)
     {
         tall = rc = 0;
         cf = 2;
         
         scanf("%lf%lf%lf",&c, &f, &x);
         
         while(1)
         {
              if(x <= c)  { tall = x/cf;  break; }
              if(rc < c)  { tall += (c-rc)/cf;  rc = c; }
              
              t1 = (x-rc)/cf;  //������ 
              t2 = (x-rc+c)/(cf+f);  //����
              
              if(t1 <= t2) { tall += t1;  break; }
              else { cf += f;  rc -= c; } 
         }
         
         printf("Case #%d: ", rd);
         printf("%.7f\n", tall);
         
     }
     
     return;
}

