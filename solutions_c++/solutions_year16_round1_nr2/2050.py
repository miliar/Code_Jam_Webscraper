#include <iostream>
#include <vector>
#include <string>
#include <utility>
#include <algorithm>
#include "math.h"
#include "stdio.h"
#include "stdlib.h"

using namespace::std;

typedef pair<int,int> ii;
typedef pair<float,int> fi;
typedef vector<ii> vii;
typedef vector<int> vi;

int main (){
int t,i,j,n,k,cont=1;
int max =0;
vi v[105];
//vi resp(2500,0);
cin >> t;
while (t--) {
  max=0;
  vi resp(2500,0);
  cin >> n;
  for (size_t j = 0; j < 2*n-1; j++) {
    v[j].clear();
  }

  for (size_t j = 0; j < 2*n-1; j++) {
  for (size_t i = 0; i < n; i++) {
    cin >> k;
    v[j].push_back(k);
    resp[k]++;
    if(k>max)
      max=k;
  }
  }
  std::cout << "Case #"<<cont << ": ";
  for (size_t i = 0; i <= max; i++) {
    //std::cout <<i << " "<< resp[i] << "if" <<resp[i]%2 <<std::endl;
    if(resp[i]%2 != 0){
      std::cout <<i << " ";
    }
  }
std::cout << std::endl;
/*
  for (size_t j = 0; j < 2*n-1; j++) {
  for (size_t i = 0; i < n; i++) {

    cout << v[j][i] << " ";
  }
  std::cout << "" << std::endl;
  }
*/

  cont++;
}

return 0;
}
