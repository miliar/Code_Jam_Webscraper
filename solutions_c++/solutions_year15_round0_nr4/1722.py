#include <cstdlib>
#include<cstdio>
#include<iostream>
#include<math.h>
#include<vector>
#include<map>
#include<string.h>
#include<queue>
#include<algorithm>
#include<string.h>
#include <stack>
using namespace std;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> ii;
typedef unsigned long long ulint;
typedef long long lint;

int main()
{
  int T;
  cin>>T;
  for(int I=1;I<=T;I++) {
    int x,r,c;
    cin>>x>>r>>c;
    bool gabriel = false;
    if(x==1) {
      gabriel = true;
    } else if(x==2) {
      if(r*c%2==0) gabriel = true;
    } else if(x==3) {
      if(r*c%3==0 && r>1 && c>1) gabriel = true;
    } else if(x==4) {
      if(r*c%4==0 && r>2 && c>2) gabriel = true;
    }
    cout<<"Case #"<<I<<": "<<(gabriel ? "GABRIEL" : "RICHARD")<<endl;
  }
}
