#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
vector<int> Shyness;
int main() {
  int tt;
  scanf("%d", &tt);
  for (int qq=1;qq<=tt;qq++) {
    printf("Case #%d: ", qq);
    int Sm;
    cin>>Sm;
    Shyness.resize(Sm+1);
    string S;
    cin>>S;
    for(int i = 0;i <= Sm;i++){
        Shyness[i] = (int)(S[i] - '0');
    }
    int answer = 0;
    int total = Shyness[0]; //these many already standing
    for(int i = 1;i <= Sm;i++){
        if(i > total){// less people are standing
            answer += i-total;
            total += (i-total) + Shyness[i];
        }
        else{
            total += Shyness[i];
        }
    }
    printf("%d\n", answer);
  }
  return 0;
}
