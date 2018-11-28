#include<stdio.h>
int res[1000],t;
void output()
{int i;
 for(i=0;i<t;i++)
 {if(res[i]==0)
  printf("case #%d: GABRIEL\n",i+1);
  else
  printf("case #%d: RICHARD\n",i+1);
}
}
int main()
{int x,r,c,i,j;
 scanf("%d",&t);
 for(i=0;i<t;i++)
{scanf("%d%d%d",&x,&r,&c);
 if((r*c)%x!=0)
 res[i]=1;
 else if(r<x && c<x)
 res[i]=1;
 else if(r<x-1 || c<x-1)
 res[i]=1;
 else if(x>7)
 res[i]=1;
 else
 res[i]=0;
}
output();
}

