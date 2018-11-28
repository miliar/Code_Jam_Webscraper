#include<iostream>
#include<cstring>
#include<cstdio>
#include<string>
#include<vector>
#include<algorithm>
#include<map>
#include<string.h>
#include<cstdlib>
#include<cmath>
using namespace std;

char   a[4][6];
/*#define dot  '.'
#define  x    'X'
#define o   'o'
#define  t  'T'
*/
int main()
{
    char ch[100];
int       z,x,n,i,j,k,w,ans,x1,t1,o1,d1 ,x2,t2,o2,d2,d,flag;
cin>>z;
//cout<<"z is   "<<z<<"\n";
w=1;

while(z--)
{
    d=0;
for(i=0;i<4;i++)
{
          scanf("%s",a[i]);
          //cin>>a[i][j];
}


/*for(i=0;i<4;i++){
for(j=0;j<4;j++)
    {printf("%c  ",a[i][j]);}
    cout<<"\n";}
*/
ans=0;
flag=0;
d=0;
for( i=0; i<4; i++)
  {

x1=0;t1=0;d1=0;o1=0;
  x2=0;t2=0;d2=0;o2=0;

      for(j=0;j<4;j++)
      {
      switch(a[i][j])
      {
        case 'X': {   x1++; break;}
        case 'O': {   o1++; break;}
        case 'T': {   t1++; break;}
        case '.': {   d1++; break;}
      }
       switch(a[j][i])
      {
        case 'X': {   x2++; break;}
        case 'O': {   o2++; break;}
        case 'T': {   t2++; break;}
        case '.': {   d2++; break;}
      }
      }
     // cout<<"x1 = "<<x1<<"\n";
      //cout<<"x2  = "<<x2<<"\n";
      if(x1==4 || (x1==3 && t1==1))
      {
          ans='X';
          flag = 1;
          break;
      }
      if(o1==4 || (o1==3 && t1==1))
      {
          ans='O';
          flag = 1;
          break;
      }

      if(d1>0 ||d2>0)
      d=1;

      if(x2==4 || (x2==3 && t2==1))
      {  //cout<<"x2 =  "<<x2<<"\n";
          ans='X';
          flag = 1;
          break;
      }
      if(o2==4 || (o2==3 && t2==1))
      {
          ans='O';
          flag = 1;
         break;
      }

  }

if(flag == 0)
{   int  f1,f2,f3,f4,f5,f6,f7,f8;
  f1=f2=f3=f4=f5=f6=f7=f8=0;
    for(i=0;i<4;i++)
        {
            switch(a[i][i])
       {case 'X': {   f1++; break;}
        case 'O': {   f2++; break;}
        case 'T': {   f3++; break;}
        case '.': {   f4++; break;}
        }
          switch(a[i][3-i])
          {
              case 'X': {   f5++; break;}
        case 'O': {   f6++; break;}
        case 'T': {   f7++; break;}
        case '.': {   f8++; break;}
          }
        }

         if ((f1==4 || (f1==3 && f3==1)) || (f5==4 || (f5==3 && f7==1)))
      {  ans='X';
          flag = 1;

      }
        if( (f2==4 || (f2==3 && f3==1)) || ( f6==4 || (f6==3 && f7==1)))
      {  ans='O';
          flag = 1;

      }
}

if(flag)
{
    printf("Case #%d: %c won\n",w++,ans);
}
if(flag==0)
{
    if(d==0 )
 printf("Case #%d: Draw\n",w++);
else
printf("Case #%d: Game has not completed\n",w++);
  }
}
return 0;
}
