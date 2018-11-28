#include <stdio.h>


int fun(char a,char b)
{
    if(a=='.'||b=='.')
    return 4;
    if(a=='T')
    a=b;
    if(b=='T')
    b=a;
    if(a!=b)
    return 1;
    if(a==b&&a=='O')
    return 2;
    if(a==b&&a=='X')
    return 3;
}

int main()
{
    char a[5][5];
    int i,j,k;
    int t;
    int m1,m2,m;
    int dc;
    int done=0;
    
    scanf("%d",&t);
    int test[1000]={0};
    int c=0;
    while(t--)
    {
  
     done=0;         
    dc=0;
    for(i=0;i<4;i++)
    {
    scanf("%s",&a[i]);
     for(j=0;j<4&&dc==0;j++)
     {       
             if(a[i][j]=='.')
             dc=1;
     }
    }
    m=0;
    m1=fun(a[0][3],a[1][2]);
    m2=fun(a[2][1],a[3][0]);
    if(m2==m1)
    {
       if(m1==2)
       {
       m=2;
       done=1;
       }
       if(m1==3)
       {
       m=3;
       done=1;
       }
    }
    if(done==0)
    {
    m1=fun(a[0][0],a[1][1]);
    m2=fun(a[2][2],a[3][3]);
    if(m2==m1)
    {
       if(m1==2)
       {
       m=2;
       done=1;
       }
       if(m1==3)
       {
       m=3;
       done=1;
       }
    }
    }           
    for(i=0;i<4;i++)
    {
    if(done==1)
    break;
    m1=fun(a[i][0],a[i][1]);
    m2=fun(a[i][2],a[i][3]);
    if(m2==m1)
    {
       if(m1==2)
       {
       m=2;
       done=1;
       }
       if(m1==3)
       {
       m=3;
       done=1;
       }
    }       
    }  
    for(i=0;i<4;i++)
    {
    if(done==1)
    break;
    m1=fun(a[0][i],a[1][i]);
    m2=fun(a[2][i],a[3][i]);
    if(m2==m1)
    {
       if(m1==2)
       {
       m=2;
       done=1;
       }
       if(m1==3)
       {
       m=3;
       done=1;
       }
    }       
    }           
if(m==2||m==3)
{
if(m==2)
    test[c]=2;
else
    test[c]=1;
}
else
{
    if(dc==1)
    test[c]=4;
    else
    test[c]=3;
}
 c++;
  printf("\n");    
}

for(i=0;i<c;i++)
 {
  if(test[i]==1)
  {
   printf("Case #%d: X won\n",i+1);
  }
  else if(test[i]==2)
  {
   printf("Case #%d: O won\n",i+1);
  }
  else if(test[i]==3)
  {
   printf("Case #%d: Draw\n",i+1);
  } 
  else if(test[i]==4)
  {
   printf("Case #%d: Game has not completed\n",i+1);
  } 
} 
  
    
    return 0;
    
}
