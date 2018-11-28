#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

typedef vector<int>::iterator viitr;

vector<int> denom;

bool canForm(int, int);

int main(){
  int numTC, TC = 1, C, D, V, coin, ans;
  scanf("%d", &numTC);
  while(numTC--){
    denom.clear(); ans = 0;
    scanf("%d %d %d", &C, &D, &V);
    for(int i=0; i<D; i++){ scanf("%d", &coin); denom.push_back(coin); }
    sort(denom.begin(), denom.end());
    for(int i=1; i<=V; i++){
      if(!canForm(i, 0)){
	viitr itr = lower_bound(denom.begin(), denom.end(), i);
	denom.insert(itr, i); ans++;
      }
    }
    printf("case #%d: %d\n", TC++, ans);
  }
  return 0;
}

bool canForm(int v, int cur){
  if(cur==denom.size()) return false;
  if(denom[cur]==v) return true;
  return canForm(v-denom[cur], cur+1) || canForm(v, cur+1);
}
