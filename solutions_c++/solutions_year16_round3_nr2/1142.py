#include<bits/stdc++.h>
using namespace std;
int N,M;
int adj[10][10];
vector< pair<int,int> >Enum;
int Edges;

int pathcount(int node)
{
      int i,res=0;
      if(node==N-1)  return 1;

      for(i=1; i<N; i++){
           if(i==node)  continue;
           if(adj[node][i]) res+=pathcount(i);
      }
      return res;
}

bool doit(int mask)
{
      int i,j;
      for(i=0; i<=N; i++)
          for(j=0; j<=N; j++)  adj[i][j]=0;

      for(i=0; i<Edges; i++){
           if(mask&(1<<i)){
               adj[Enum[i].first][Enum[i].second]=1;
               //printf("%d %d\n",Enum[i].first,Enum[i].second);
           }
      }

      int cnt = pathcount(0);
      return (cnt==M);
}

int main()
{
      int T,it,mask,i,j;
      freopen("B-small-attempt0.in","r",stdin);
      freopen("B.out","w",stdout);
      scanf("%d",&T);
      for(it=1; it<=T; it++)
      {
            scanf("%d",&N);
            scanf("%d",&M);

            Edges = (N*(N-1))/2;
            Enum.clear();

            for(i=0; i<N; i++)
            {
                  for(j=i+1; j<N; j++){
                      Enum.push_back(make_pair(i,j));
                      //printf("i:%d j:%d\n",i,j);
                  }
            }


            //doit((1<<Edges)-1);
            bool f=0;
            for(mask=1; mask<(1<<Edges); mask++)
            {
                  if(doit(mask)){
                        f=1;
                        break;
                  }
            }

            printf("Case #%d: ",it);
            if(!f)  printf("IMPOSSIBLE\n");
            else{
                printf("POSSIBLE\n");
                for(i=0; i<N; i++){
                    for(j=0; j<N; j++)  printf("%d",adj[i][j]);
                    puts("");
                }
            }
      }
      return 0;
}
