#include<stdio.h>
#include<stdlib.h>

int mx1[4][4];
int mx2[4][4];

int main()
{
 freopen("A-small-attempt1.in","r",stdin);
 freopen("A-small-attempt1.out","w",stdout);   

 int t;
 scanf("%d",&t);
 int ans1=0,ans2=0;
 for(int x=1;x<=t;++x)
 {//每组数据，有两个answer 
  scanf("%d",&ans1);
  for(int i=0;i<4;++i)
   for(int j=0;j<4;++j)
   {
    scanf("%d",&mx1[i][j]);       
   }            
   
  scanf("%d",&ans2);
  for(int i=0;i<4;++i)
   for(int j=0;j<4;++j)
   {
    scanf("%d",&mx2[i][j]);       
   }     
  
  int flag=0,num=0;
  for(int i=0;i<4;++i)
  {
   for(int j=0;j<4;++j)
   {
    if(mx1[ans1-1][i]==mx2[ans2-1][j])
    {
     if(num==0) {num=mx1[ans1-1][i];}
     else flag=1;//flag标记找到多于一组值 
    }       
   }       
  }
  
  printf("Case #%d: ",x);
  if(flag) printf("Bad magician!\n");
  else if(num) printf("%d\n",num);
  else printf("Volunteer cheated!\n");
 }
 //system("pause");
 return 0;   
}
