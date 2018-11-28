#include<cstdio>
#include<cstring>
#include<vector>
using namespace std;

int main()
{
int t,ptr,vptr;
freopen("A-large.in","r",stdin);freopen("abc.out","w",stdout);
scanf("%d",&t);
int tt=t;
char ch[1000];
  while(t--)
  {
     scanf("%s",ch);
  
     vector<char> out;
     vector<char>::iterator it;
     out.push_back(ch[0]);
      vptr=0;
     ptr=1;
     
     while(ch[ptr]!='\0')
     {
      
       if(ch[ptr]>=out[vptr])
       {
         it=out.begin();
         out.insert(it,ch[ptr]);
         
       }
      else
       {
          out.push_back(ch[ptr]);

       }
       ptr++;
     }
   printf("Case #%d: ",tt-t);
   for(it=out.begin();it!=out.end();it++)
   printf("%c",*it);
  
    printf("\n");
  }

return 0;
}

