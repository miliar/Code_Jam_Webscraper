#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
#include <map>
using namespace std;
const int MN = 15;
int Map[MN][MN],Map0[MN][MN];
int main()
{

     freopen("B-small-attempt0.in","r",stdin);
     freopen("b.out","w",stdout);
      int T,N,M;
      bool flag ;
      cin>>T;
      for(int cas = 1 ;cas <= T;++cas)
      {
           cin>>N>>M;
           flag = true;
           for(int i=1;i<=N;++i)
           {
             for(int j=1;j<=M;++j)
            {
               cin>>Map[i][j];
               Map0[i][j]=2;
            }
           }
           for(int i=1;i<=N;++i)
           {
                 for(int j=1;j<=M;++j)

                   if(Map[i][j]==1)
                 {
                       bool hen=true,shu=true;
                       for(int k = 1; k<= N;++k)
                         if(Map[k][j]==2)
                       {
                             shu= false;
                             break;
                       }
                       for(int k=1;k<=M;++k)
                        if(Map[i][k]==2)
                       {
                             hen = false;
                             break;
                       }

                  if(!hen && !shu )
                      {
                            flag = false;
                            break;
                      }
                 }
                    if(!flag)break;
           }
          if(flag) printf("Case #%d: %s\n",cas,"YES");
          else printf("Case #%d: %s\n",cas,"NO");
      }
      return 0;
}
