#include<stdio.h>
#include<conio.h>
int main()
{
FILE *f1,*f2;
int n,m,k,i,j,z1,z2;
int a[10][10];
f1=fopen("input2.txt","r");
f2=fopen("output2.txt","w");
fscanf(f1,"%d",&k);
printf("%d\n",k);
for(i=1;i<=k;i++)
{
                 int b[10]={0};
                 int c[10]={0};
                 fscanf(f1,"%d",&n);
                 fscanf(f1,"%d",&m);
                 
                 for(z1=0;z1<n;z1++)
                 {for(z2=0;z2<m;z2++)
                 fscanf(f1,"%d",&a[z1][z2]);
                 }
                 
                 for(z1=0;z1<n;z1++)
                 {for(z2=0;z2<m;z2++)
                 if(a[z1][z2]==1)
                 b[z1]++;
                                  
                 }
                  for(z1=0;z1<m;z1++)
                 {
                 for(z2=0;z2<n;z2++)
                 if(a[z2][z1]==1)
                 c[z1]++;
                                 
                 }
                 
                 j=0;
                 
                 
                 /*for(j=0;j<m+n;j++)
                 printf("%d  ",b[j]);
                 printf("\n");
                 */
                 
                 for(z1=0;z1<n;z1++)
                 {for(z2=0;z2<m;z2++)
                 
                 if(a[z1][z2]==1)
                 {
                                
                 if(b[z1]!=m && c[z2]!=n)
                 j=1;
                 }
                 }
                 if(j==0)
                 fprintf(f2,"Case #%d: YES\n",i);
                 else
                  fprintf(f2,"Case #%d: NO\n",i);
                 }

getch();
}
