/*
  with the help of god
*/
#include <algorithm>
#include <numeric>
#include <string>
#include <cstring>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <iterator>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <stack>

using namespace std;

int main(){
  long long int a[40]={1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404, 10000200001, 10221412201, 12102420121, 12345654321, 40000800004, 1000002000001, 1002003002001, 1004006004001, 1020304030201, 1022325232201, 1024348434201, 1210024200121, 1212225222121, 1214428244121, 1232346432321, 1234567654321, 4000008000004, 4004009004004, 100000020000001};
  int t;
  cin>>t;
  int cse=1;
  while(t--){
    long long int n,m;
    cin>>n>>m;
    int k=0;
    for(int i=0;i<40;i++){
      if(a[i]>=n&&a[i]<=m) k++;
    }
    cout<<"Case #"<<cse++<<": "<<k<<endl;
  }
  return 0;
}

