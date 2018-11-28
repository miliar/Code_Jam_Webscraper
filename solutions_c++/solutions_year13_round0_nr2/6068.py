#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
     freopen("abc.txt","r",stdin);
      int t,mat[10][10],row[10]={0},col[10]={0},test=1,i,m,n,j;
      cin>>t;
      while(t--)
      {
            for(i=0;i<10;++i)
            row[i]=col[i]=0;
            int p=1;
            scanf("%d%d",&m,&n);
            for(i=0;i<m;++i)
                  for(j=0;j<n;++j)
                  {
                  scanf("%d",&mat[i][j]);
                  if(mat[i][j]==1)
                  {
                        row[i]++;
                        col[j]++;
                  }

                  }
            for(i=0;i<m;++i)
            {
                  for(j=0;j<n;++j)
                  {

                        if(mat[i][j]==1&&row[i]!=n&&col[j]!=m)
                  {
                        p=0;
                        break;
                  }
                  else
                        continue;
                  }
                  if(p==0)
                        break;
            }
                  if(p==0)
                        printf("Case #%d: NO\n",test);
                  else printf("Case #%d: YES\n",test);
            ++test;
      }
      getchar();
}
