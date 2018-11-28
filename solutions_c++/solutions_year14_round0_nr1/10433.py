#include<stdio.h>
int main()
{
 int t,n=0;
// freopen("D://in.txt","r",stdin);
  //freopen("D://out.txt","w",stdout);
 scanf("%d",&t);
 while(t--)
 {
  
  n++;
  int a1,b1,x1,x2,x3,x4;
  int a[4],b[4],i,j;
  scanf("%d",&a1);
  for(i=0;i<4;i++)
  {
   if(a1-1==i)
   scanf("%d %d %d %d",&a[0],&a[1],&a[2],&a[3]);
   else
   scanf("%d %d %d %d",&x1,&x2,&x3,&x4);
  }
  scanf("%d",&b1);
  for(i=0;i<4;i++)
  {
   if(b1-1==i)
   scanf("%d %d %d %d",&b[0],&b[1],&b[2],&b[3]);
   else
   scanf("%d %d %d %d",&x1,&x2,&x3,&x4);
  }
  int bit=0,key,l=0;
  for(i=0;i<4;i++)
  {
   bit=a[i];
   for(j=0;j<4;j++)
   {
    if(bit==b[j]) { key=bit; l++;}
   }
  }
  printf("Case #%d: ",n);
  if(l==1)
  printf("%d\n",key);
  else if(l>1)
  printf("Bad magician!\n");
  else if(l==0)
  printf("Volunteer cheated!\n");
 }
 return 0;
}
