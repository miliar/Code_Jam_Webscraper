#include<cstdio>
#include<algorithm>
#include<vector>
#include<map>
using namespace std;


vector< pair<double, int> > lista;

int solve_war(){
  int saldo = 0;
  int ret = 0;
  for(auto p : lista) {
    if (p.second == 0) saldo++;
    else  if (p.second==1 && saldo != 0) {
      saldo--;
      ret ++;
    }
  }
  return ret;
}

int solve_dec(){
  int saldo = 0;
  int ret = 0;
  for( auto p: lista) {
    if (p.second==1)saldo++;
    else if(p.second==0 && saldo!=0){
      saldo--;
      ret++;
    }
  }

  return ret;
}

int main () {
  int tt;
  scanf("%d",&tt);
  for(int pp=1;pp<=tt;pp++){
    int n;
    scanf("%d",&n);
    lista.clear();
    for(int k=0;k<2;k++)
      for(int i=0;i<n;i++){
	double d;
	scanf("%lf",&d);
	lista.push_back(make_pair(d,k));
      }
    sort(lista.begin(), lista.end());

    int r2 = solve_war();
    int r1 = solve_dec();
    
    printf("Case #%d: %d %d\n",pp,r1,n-r2);
  }
  return 0;
}
