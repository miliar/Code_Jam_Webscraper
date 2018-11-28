#include<iostream>
#include<cstdio>
#include<cstring>
#include<math.h>
using namespace std;
int ctr=0;
int gcd (int a,int b)
{
    if(b==0) return a; gcd(b,a%b);
}

int temp2;
float temp1;


int main()
{
     freopen("ans1out.txt","w",stdout);
  freopen("A-small-attempt0.in","r",stdin);
   int t;
   scanf("%d",&t);
   for(int a=1;a<=t;a++)
   {
      int p,q,temp2,x;
      float temp1;
      scanf("%d/%d",&p,&q);
      //cout<<p<<q;
      x=gcd(p,q);
    //  cout<<x<<endl;
      p/=x;
      q/=x;

     ctr=0;

         int ans=0,flag=0;
          if(p==1 && q==1)
        ans=1;
           temp1=log2(q);
      temp2=(int)temp1;
      if(temp1!=temp2)
      {
              flag=1;
 printf("Case #%d: impossible\n",a);
 continue;
      }
    if((p==1) && (temp1==temp2))
    {
     ans= temp2;
    }
    else
    {
        q/=2;
        ctr++;
        if(p>q)
        ans=ctr;
        else
        {
           while((p<q)&&(ctr<41))
           {
            q/=2;
            ctr++;

            }
            ans=ctr;
        }
      }
  //    if(flag==1)
     // printf("Case #%d: impossible\n",a);
  //   else
printf("Case #%d: %d\n",a,ans);
    }
return 0;
}
