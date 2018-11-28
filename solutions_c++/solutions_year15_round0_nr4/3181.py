#include<stdio.h>
int main()
{
  // freopen("input.cpp","r",stdin);
// freopen("output.txt","w",stdout);

  int k,t;
scanf("%d",&k);
t=k;
while(k--)
{
int x,r,c;
scanf("%d %d %d",&x,&r,&c);
int sum =0,n=0,flag=0;
sum =r*c;
int y=x;
while(y>=1)
{
    if(sum%x!=0)
        break;
if(sum%y!=0)
  {
      if(c<=r)
      { c=c-1;
      if(c==0)
      flag=0;
        while(c)
        {
            n=c*r;
            if(n%y!=0)
            flag=0;
            else
            flag=1;
             if(flag==1)
                break;
                c--;
        }
      }
      if(r<c)
      { r=r-1;
      if(r==0)
        flag=0;
        while(r)
        {
            n=c*r;
            if(n%y!=0)
            flag=0;
            else
                flag=1;
                if(flag==1)
                    break;
                r--;
        }
      }
  }
  else
  flag=1;
  if(flag==0)
    break;
  y--;
}
if(flag==1)
printf("Case #%d: GABRIEL\n",t-k);
else
printf("Case #%d: RICHARD\n",t-k);
}
return 0;
}

