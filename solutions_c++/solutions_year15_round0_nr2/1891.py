/*
 * B.cpp
 * Copyright (C) 2015 Chen Ran <crccw@moonux.org>
 *
 * Distributed under terms of the CC-BY-SA 4.0 license.
 */

#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <set>
#include <vector>
#include <list>
#include <map>
#include <queue>
#include <algorithm>
#define INF 0x3f3f3f3f
#define MAXN 100100
#define mp make_pair
#define pb push_back
const double EPS=1e-9;

using namespace std;
typedef long long LL;


int main(int argc, char *argv[])
{
  int t;
  cin>>t;
  int d,p[1100],ans,pmax;
  for(int cas=1;cas<=t;cas++){
    cin>>d;
    pmax=-1;
    for(int i=1;i<=d;i++){
      cin>>p[i];
      pmax=max(p[i],pmax);
    }
    ans=pmax;
    for(int i=1;i<=pmax;i++){
      int x=0;
      for(int j=1;j<=d;j++){
        x+=p[j]/i;
        if(p[j]%i==0) x--;
      }
      ans=min(ans,x+i);
    }
    cout<<"Case #"<<cas<<": "<<ans<<endl;
  }
  return 0;
}
