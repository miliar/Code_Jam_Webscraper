#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cassert>
#include<cmath>
#include<vector>
#include<set>
#include<map>
#include<list>
#include<deque>
#include<queue>
#include<stack>
#include<functional>
#include<sstream>
#include<iostream>
#include<ctime>
#include<algorithm>
using namespace std;

#define DEBUG(x...) printf(x)
#define allv(v) (v).begin(),(v).end()
#define rall(v) (v).begin(),(v).rend()
#define _foreach(it,b,e) for(__typeof__(b); it!=(e);++it)
#define foreach(x...) _foreach(x)

typedef long long int huge;

const int inf = 0x3f3f3f3f;
const huge hugeinf = 0x3f3f3f3f3f3f3f3fll;//dois L's
const double eps = 1e-9;
const int maxn = 10010;
int n,m;
huge perde = 0;
int qte = 0;
int lista[maxn][2];
int main ()
{
  int tt;
  scanf("%d",&tt);
  for(int pp=1;pp<=tt;pp++)
    {
      qte=0;
      perde = 0;
      scanf("%d %d",&n,&m);
      for(int i=0;i<m;i++){
	int a,b,c;
	scanf("%d %d %d", &a,&b,&c);
	for(int j=0;j<c;j++){
	  lista[qte][0]=a,lista[qte][1]=b;
	  qte++;
	}
      }
      bool ok = true;
      while(ok){
	ok = false;
	for(int i=0;i<qte;i++){
	  for(int j=0;j<qte;j++){
	    if(lista[j][0]>lista[i][0] && lista[j][0]<=lista[i][1] && lista[j][1]>lista[i][1]){
	      huge a = lista[i][1]-lista[i][0];
	      huge b = lista[j][1]-lista[j][0];
	      huge c = lista[i][1]-lista[j][0];
	      perde += a*b+c*c -a*c-b*c;
	      swap(lista[i][0],lista[j][0]);
	      ok = true;
	    }
	  }
	}
      }
      printf("Case #%d: %lld\n",pp,perde);
    }
  return 0;
}
