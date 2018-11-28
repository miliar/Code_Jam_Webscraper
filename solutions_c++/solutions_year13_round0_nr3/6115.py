#include<stdio.h>
#include<math.h>
using namespace std;
int main()
{
 int paldr(int a),count;
int a,b,c,t,case_r=1;
scanf("%d",&t);
while(case_r<=t && t!=0)
{ 
  count=0;
  scanf("%d",&a);
  scanf("%d",&b);
  for(int i=a;i<=b;i++)
  {  c=sqrt(i);

     if(pow(c,2)==i)
     {
       if(paldr(i))
    { if(paldr(sqrt(i)))
        count++;
    }
     }
  }
  printf("Case #%d: %d\n",case_r,count);
case_r++;
}

  return 0;
}

int paldr(int num)
{ int temp,rev=0,save=num;
  while(num)
  { temp=num%10;
    num=num/10;
    rev=rev*10+temp;
  }
  if(save==rev)
  {
   return 1;
   }
  return 0;
}