#include <stdio.h>
#include <math.h>

int check(int i);
int len(int i);
int poe(int i);
int main()
{
    
    //----------------------
    FILE *fp1, *fp2;
    freopen("C-small-attempt0.in","r",stdin);
    freopen("result_3.txt","w",stdout);
    //----------------------
        
    
    int ii,nn;
    scanf("%d\n", &nn);
    for (ii=1;ii<=nn;ii++)
    {
        int a,b;
        int tot=0;
        scanf("%d%d\n", &a, &b);
        int i;
        for (i=a;i<=b;i++)
            if (check(i)==0){
                              tot++;
                              /*printf("%d\n", i); */
                              }
        printf("Case #%d: %d\n", ii, tot);
    }
    return 0;
}
int len(int x)
{
    int i=0;
    while (x!=0)
    {
          i++;
          x=x/10;
    }
    return i;
}
int pow(int x)
{
    int i,ans;
    ans=1;
    for (i=1;i<=x-1;i++)
        ans*=10;
    return ans;
}
int check(int x)
{
    int l,p,i,x0;
    l=len(x);
    p=pow(l);
    x0=x;
    int f=0;
    for (i=1;i<=l/2;i++)
        {
                        int a=0,b=0;
                        a=x/p; b=x%10;
                        if (a!=b){
                                  f=1;
                                  break;
                                  }
                        x=x/10;
                        p/=100;
        }
    x=x0;
    if (f==0) 
    {
              int k=0,ff=0;
              k=sqrt(x);
              l=len(k);
              p=pow(l);
              x0=k;
              int f=0;
              for (i=1;i<=l/2;i++)
                 {
                                 int a=0,b=0;
                                  a=k/p; b=k%10;
                                  if (a!=b){
                                            ff=1;
                                            break;
                                            }
                                  k=k/10;
                                  p/=100;
                  }
              k=x0;
              if (((k*k)==x)&&(ff==0)) return 0;
                 else return 1;
    }
    return 1;
}
