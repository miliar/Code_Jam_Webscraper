#include<cstdio>
using namespace std;
int main()
{
  int t;
  scanf("%d",&t);
  int total=t,len,i,dev,curr;
  char ch[100];
  for(int j=1;j<=t;j++)
  {
    
    scanf("%s",ch);

    
    i=1;dev=0;
    curr=ch[0];
    while(ch[i]!='\0')
    {
      if(curr!=ch[i]){dev++;curr=ch[i];}
       i++;
    }    
   if(ch[i-1]=='-') 
   dev++;
 
   printf("Case #%d: %d\n",j,dev);

  }
return 0;
}
