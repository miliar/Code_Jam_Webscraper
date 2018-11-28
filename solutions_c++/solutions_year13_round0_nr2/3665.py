#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
#include<string>
#include<iostream>
#include<stack>
#include<queue>
#include<map>
#include<set>
using namespace std;
#define INF (1<<29)
int T;
int fie[101][101];
int minn[101];
int minm[101];
int main()
{
  cin >> T;
  for(int loop=0;loop<T;loop++)
    {
      /*      for(int i=0;i<=100;i++){
	minn[i]=INF;
	minm[i]=INF;
      }
      */
      memset(minn,0,sizeof(minn));
      memset(minm,0,sizeof(minm));
      int N,M;
      cin >> N >> M;
      for(int i=0;i<N;i++){
	for(int j=0;j<M;j++){
	  cin >> fie[j][i];
	}
      }

      for(int i=0;i<N;i++){
	for(int j=0;j<M;j++){
	  minn[i] = max(fie[j][i],minn[i]);
	  minm[j] = max(fie[j][i],minm[j]);
	}
      }

      bool f=true;
      for(int i=0;i<N;i++){
	for(int j=0;j<M;j++){
	  if(fie[j][i]<minn[i] && fie[j][i]<minm[j]){ f=false; break; }
	}
	if(!f) break;
      }
      
      if(f) printf("Case #%d: YES\n",loop+1);
      else printf("Case #%d: NO\n",loop+1);

    }
}
