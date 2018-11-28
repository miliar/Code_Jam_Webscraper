#include<stdio.h>
#include<algorithm>
#include<math.h>
#include<stdlib.h>
using namespace std;
double ans[1500];
int sum[1500];
int in[20],r[20],last,col,tt[20];
double dec[15];
void checkk(double x)
{
     double y;
     y = sqrt(x);
     if(floor(y) != y) return;
     
     long long a;
     a = (long long)(floor(y));
     int r = 0,l;
     while(a > 0)
        {
         tt[r++] = a%10;
         a /= 10;
        }
     int c = 1;
     for(r--,l = 0;r >= l;r--,l++)
        {
         if(tt[r] != tt[l]) return ;
        }
     //printf("%.0lf\n",x);
     ans[last++] = x;
}
void DFS(int a)
{
     if(a == 0)
        {
         int i,j;
         for(i=col,j = col-1;j>=0;i++,j--)
            {
             r[i] = r[j];
            }
         double temp = 0;
         for(i--,j=0;i>=0;i--,j++)
            {
             temp += r[i]*dec[j];
            }
         checkk(temp);
        // printf("%.0f\n",temp);
         return ;
        }
     col++;
     for(int i=0;i<=9;i++)
        {
         r[col-1] = i;
         DFS(a-1);
        }
     col--;
}
void DFS2(int a)
{
     if(a == 0)
        {
         int i,j;
         for(i=col+1,j = col-1;j>=0;i++,j--)
            {
             r[i] = r[j];
            }
         int x = i-1;
         for(int k=0;k<10;k++)
            {
             r[col] = k;
             double temp = 0;
             for(i = x,j=0;i>=0;i--,j++)
                {
                 temp += r[i]*dec[j];
                }
             checkk(temp);
             //printf("%.0f\n",temp);
            }

         return ;
        }
     col++;
     for(int i=0;i<=9;i++)
        {
         r[col-1] = i;
         DFS2(a-1);
        }
     col--;
}
int main(){
    
    int n,m,i,j,k,t,x,check;
    long long a,b;
    double temp;
    
    freopen("C-large-1.in","r",stdin);
    freopen("C-large-1.out","w",stdout);
    
    last = 1;
    /*for(i=1;i<10;i++)
       ans[last++] = i;*/
    ans[1] = 1;
    ans[2] = 4;
    ans[3] = 9;
    last = 4;
    
    dec[0] = 1;
    for(i=1;i<15;i++)
       {
        dec[i] = dec[i-1]*10;
       }
    
    for(i=1;i<=7;i++)
       {
        col = 0;
        for(j=1;j<=9;j++)
           {
            r[0] = j;
            col = 1;
            DFS(i-1);
           }
        
        if(i==7) break;
        for(j=1;j<=9;j++)
           {
            r[0] = j;
            col = 1;
            DFS2(i-1);
           }
        
       }
    //printf(".....");
    /*for(i=1;i<40;i++)
       printf("%.0lf\n",ans[i]);
    printf("last = %d\n",last);*/
    scanf("%d",&t);
    int sm,l,r;
    for(k=1;k<=t;k++)
       {
        sm = 0;
        scanf("%I64d%I64d",&a,&b);
        
        for(i=1;i<40;i++)
           {
            if(ans[i] >= a) break;
           }
        l = i-1;
        
        for(i=39;i>=0;i--)
           {
            if(ans[i] <= b) break;
           }
        r = i;
        printf("Case #%d: %d\n",k,r-l);
        
       }
    
    
 scanf(" ");
 return 0;
}
