#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <vector>
#include <list>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <functional>
#include <numeric>
#include <cstdlib>
#include <stack>
#include <cstdio>
#include <fstream>
#include <ctime>
#include <cassert>

using namespace std;

int main(){
  int t,m;
  cin >> t;
  m=t;
  while(t--){
    long long int n,n1;
    cin >> n;
    n1=n;
    if(n!=0){
    int a[10];
    for(int i=0;i<10;++i)
      a[i]=0;
    int count=1;
    while(1){
      long long int temp=n1;
      while(temp!=0){
        a[temp%10]=1;
        temp=temp/10;
      }
      bool flag=false;
      for(int i=0;i<10;++i){
        if(a[i]!=1){
          flag=true;
          break;
        }
      }
      if(!flag){
          cout << "Case #" << m-t << ": " << n1 << endl;
          break;
      }
      n1=n * ++count;
    }
  }
  else{
    cout << "Case #" << m-t << ": " << "INSOMNIA" << endl;
  }
  }
}
