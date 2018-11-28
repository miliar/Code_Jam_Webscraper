#include<iostream>
#include<stdio.h>
#include<string.h>
#include<map>
#include<set>
#include<algorithm>
#include<cmath>
#include<cstring>
#include<stack>
#define MAXN 10005
using namespace std;  
int a[5][5]={{0},
             {0,1,2,3,4},
             {0,2,-1,4,-3},
             {0,3,-4,-1,2},
             {0,4,3,-2,-1}};
char st[MAXN]; 
string s; 
int O[2][MAXN],sum[MAXN];
int Turn(char c)
{
      if (c=='i') return 2;
      if (c=='j') return 3;
      return 4;
}
int G(int l,int r)
{
      int h1=sum[l-1],h2=sum[r],x; 
      if (h1<0) 
      {
           h1=-h1;
           for (x=1;x<=4;x++)
             if (a[h1][x]==h2 || a[h1][x]==-h2) break;  
           if (a[h1][x]==h2) x=-x;           
      }else
      {
           for (x=1;x<=4;x++)
             if (a[h1][x]==h2 || a[h1][x]==-h2) break;   
           if (a[h1][x]==-h2) x=-x;     
      }
      return x;      
} 
int main()
{
      int cases,T,L,X,num0,num1,len;
      bool f;
      freopen("C-small-attempt2.in","r",stdin);
      freopen("output.txt","w",stdout);
      scanf("%d",&T);
      for (cases=1;cases<=T;cases++)
      {
              scanf("%d%d%s",&L,&X,st),s="";
              while (X--) s+=st; 
              len=s.length(),f=false; 
              int p1,p2,h,p,i;
              num0=num1=0;
              h=1;
              for (i=0;i<len;i++)
              {
                     p=Turn(s[i]);
                     if (h<0) h=-a[-h][p];
                     else  h=a[h][p];
                     if (h==2) O[0][++num0]=i;  
                     sum[i]=h; 
              }
              h=1;
              for (i=len-1;i>=0;i--)
              {
                     p=Turn(s[i]);
                     if (h<0) h=-a[p][-h];
                        else  h=a[p][h];
                     if (h==4) O[1][++num1]=i;  
              }
              for (p1=1;p1<=num0;p1++)
                 for (p2=1;p2<=num1;p2++)
                  {
                        if (O[1][p2]-1<O[0][p1]+1) continue;                   
                        if (G(O[0][p1]+1,O[1][p2]-1)!=3) continue; 
                        f=true;
                        goto A;
                  } 
              A: ;
              printf("Case #%d: ",cases);
              if (f) puts("YES");
                else puts("NO"); 
            //  printf("###%d###\n",G(4,6));
      } 
      return 0;
}
