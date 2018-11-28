#include<stdio.h>
int res[100000],t,ele;
void output()
{int i;
 for(i=0;i<t;i++)
 printf("case #%d: %d\n",i+1,res[i]);
}
int max(int a[],int n)
{
 int max,i;
 max=0;
 for(i=0;i<n;i++)
 { if(max<a[i]){ max=a[i];ele=i;}
 }
return max;
}
int min(int a[],int n)
{
 int min,i;
 min=9999;
 for(i=0;i<n;i++)
 { if(min>a[i]){ min=a[i];}
 }
return min;
}
int main()
{
 int a[10000],b[10000],c[10000],i,j,k,m,maxi,n,count;
 scanf("%d",&t);
 for(i=0;i<t;i++)
{
 scanf("%d",&n);
 for(j=0;j<n;j++)
{scanf("%d",&a[j]);
 c[j]=a[j];
}

maxi=max(a,n);
b[0]=maxi;
m=1;
count=0;
k=n;
while(maxi>3)
{a[k]=maxi-3;
 k++;
 count++;
 a[ele]=3;
 maxi=max(a,k);
 b[m]=maxi+count;
 m++;
}
maxi=max(c,n);
b[m]=maxi;
count=0;
k=n;
while(maxi>3)
{c[k]=maxi/2;
 k++;
 count++;
 c[ele]=maxi-(maxi/2);
 maxi=max(c,k);
 b[m]=maxi+count;
 m++;
}

res[i]=min(b,m);
}
output();
}
 

