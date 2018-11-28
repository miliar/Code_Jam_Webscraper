
#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <iostream>
#include <vector>
#include <set>
#include <map>

using namespace std;

vector<double> Naomi;
vector<double> Ken;

int generalWar(const vector<double>& Ken, const vector<double>& Naomi){
  int j = Naomi.size()-1;
  int WP = 0;
  for(int i=Ken.size()-1;i>=0 && j>=0;--i){
    while(j>=0 && Ken[i]<=Naomi[j])
      --j;
    if(j>=0)
      WP++;
    j--;
  }
  return Ken.size()-WP;
}

int deceitfulWar(const vector<double>& Naomi, const vector<double>& Ken){
  int n_f = 0, n_r = Naomi.size()-1;
  int k_f = 0, k_r = Ken.size()-1;
  int DP = 0;
  while(n_f<=n_r){
    if(Naomi[n_r] > Ken[k_r]){
      DP++;
      n_r--;
      k_r--;
    }
    else if( Naomi[n_f]>Ken[k_f]){
      DP++;
      n_f++;
      k_f++;
    }
    else{
      if( Naomi[n_f] > Ken[k_r] )
	DP++;
      n_f++;
      k_r--;
    }
  }
  return DP;
}

int main(){
  int T,n;
  double wei;
  int caseNum = 1;

  scanf("%d",&T);
  while(T--){
    scanf("%d",&n);
    Naomi.resize(0);
    Ken.resize(0);

    for(int i=0;i<n;++i){
      scanf("%lf",&wei);
      Naomi.push_back(wei);
    }
    for(int i=0;i<n;++i){
      scanf("%lf",&wei);
      Ken.push_back(wei);
    }
    sort(Naomi.begin(),Naomi.end());
    sort(Ken.begin(),Ken.end());
    printf("Case #%d: %d %d\n",caseNum++,deceitfulWar(Naomi,Ken),generalWar(Ken,Naomi));
  }
  return 0;
}
