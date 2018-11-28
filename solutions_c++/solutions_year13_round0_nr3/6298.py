#include <string>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <iterator>
#include <cstdio>
#include <vector>
#include <cmath>

using namespace std;

vector<int> m(1001,0);

bool palin(string s)
{
  int i,j,k=s.length();
  if(k==1)return true;
  else if(k==2) return s[0]==s[1];
  else return s[0]==s[2];
}

int main()
{
  int i,j,k,t,c=1,d=0;
  int a,b;
  scanf("%d", &t);
  for(i=1;i<=sqrt(1000);i++){
    stringstream ss,cc;ss<<i*i;cc<<i;
    if(!palin(cc.str()) or !palin(ss.str()))continue;
    m[i*i]=1;
  }

  while(t--){
    scanf("%d %d", &a, &b);
    d=0;
    for(i=a;i<=b;i++)if(m[i]==1){++d;}
    printf("Case #%d: %d\n", c++, d);
  }

  return 0;
}
