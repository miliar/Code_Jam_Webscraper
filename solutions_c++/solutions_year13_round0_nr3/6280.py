#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
#include <map>
using namespace std;
int u[101],pn=0;
void init()
{
      char ch[10];
      for(int i=1;i<=35;++i)
      {
            int temp = i*i;
            sprintf(ch,"%d",temp);
              // printf("%s\n",ch);
             int l=0,r=strlen(ch)-1;
             while(l<r)
             {
                   if(ch[l]!=ch[r])break;
                   l++;r--;
             }
             if(l>=r)
             {
                   u[pn++]=temp;
                  // cout<<temp<<endl;
             }

      }
}
int main()
{
     freopen("C-small-attempt0.in","r",stdin);
     freopen("c.out","w",stdout);
      init();
      pn--;
      int T,A,B;
      cin>>T;
      for(int cas = 1 ;cas<=T;++cas)
      {
           cin>>A>>B;
           int ans = 0;
           for(int j=0;j<pn;++j)
                  if(u[j]>=A && u[j]<=B)
                       ans++;
           printf("Case #%d: %d\n",cas,ans);
      }
      return 0;
}
