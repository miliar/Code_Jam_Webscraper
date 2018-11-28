#include<stdio.h>

using namespace std;

int main()
{
 freopen( "B-large.in", "r", stdin );
 freopen( "outputBLarge2.out", "w", stdout );

 int i,t,j,cn;
 char ch[101];

 scanf("%d",&t);
 i=0;
 while(i<t)
 {
  scanf("%s",&ch);

  j=0;
  cn=0;
  for(j=0;ch[j+1]!='\0';j++)
  {
   if(ch[j]=='+'&&ch[j]!=ch[j+1])
     cn+=2;
  }
  if(ch[0]=='-')
   cn+=1;

  printf("Case #%d: %d\n",i+1,cn);

  i++;
 }
}
