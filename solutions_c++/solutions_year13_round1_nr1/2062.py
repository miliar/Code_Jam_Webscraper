#include<stdio.h>
#include<stdlib.h>
int T;
int t,r,n;

int searchroot()
{int right=100000,mid,left=0;
  printf("r=%d t=%d\n",r,t);
 while(left<right-1)
  {int k;
   mid=(right+left)/2;
   k=2*mid*mid+(r*2-3/2)*mid-t;
   if(k>0)
   {right=mid;
   }
   else if(k<0)
   {left=mid;
   }
   else
   {left=mid;
    break;
   }
   printf("k=%d l=%d m=%d r=%d\n",k,left,mid,right);
  }
 return (left);
}

int main()
{FILE *p1,*p2;
 p1=fopen("A-small-attempt0.in","r");
 p2=fopen("out.txt","w");
 fscanf(p1,"%d",&T);
 int i,j;
 j=0;
 while(j<T)
 {j++;
  fscanf(p1,"%d%d",&r,&t);
  n=searchroot();
  fprintf(p2,"Case #%d: %d\n",j,n);
 }
 fclose(p1);
 fclose(p2);
 system("pause");
}
