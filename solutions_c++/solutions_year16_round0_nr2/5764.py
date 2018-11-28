#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <list>
#include <stack>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <set>
#include <cmath>
#include <sstream>
using namespace std;

int getMinimum(string &data){
   int len = data.size();
   if (len == 0)
      return 0;
   vector<int> dp_plus(len, 0);
   vector<int> dp_minus(len, 0);
   if (data[0] == '+'){
      dp_plus[0] = 0;
      dp_minus[0] = 1;
   }
   else{
      dp_plus[0] = 1;
      dp_minus[0] = 0;
   }
   
   for(int i = 1; i < len; i++){
     if(data[i] == '+'){
      dp_plus[i] = dp_plus[i-1];
      dp_minus[i] = min(dp_minus[i-1] + 2, dp_plus[i-1] + 1);
     } 
     else{
      dp_minus[i] = dp_minus[i-1];
      dp_plus[i] = min(dp_plus[i-1] + 2, dp_minus[i-1] + 1);
     }
   }
   return dp_plus[len-1];
}

int main() {
    freopen("p2.input","r",stdin);//redirects standard input
    int n, ret=0;
    string data;
    scanf("%d\n", &n);
    for(int i=0;i<n;i++){
        cin >> data;
        cout << "Case #" << i+1 << ": " << getMinimum(data) << endl;
    }
    return 0;
}
