/*
 * A.cpp
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
  string smax,s;
  cin>>t;
  for(int cas=1;cas<=t;cas++){
    cin>>smax>>s;
    int now=0,ans=0;
    for(int i=0;i<s.size();i++){
      if(now<i) ans+=i-now,now=i;
      now+=s[i]-'0';
    }
    cout<<"Case #"<<cas<<": "<<ans<<endl;
  }
  return 0;
}
