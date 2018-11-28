#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <vector>
using namespace std;
#define EPS 1e-10
int n;
double v;
double x;
double r[10][3];
double o;
double r1,r2;
int main() {
  int zz;
  cin>>zz;
  for (int zzz=1;zzz<=zz;zzz++) {
    cin>>n>>v>>x;
    printf("Case #%d: ", zzz);
    for (int i=0;i<n;i++) {
      cin>>r[i][0]>>r[i][1];
    }
    bool g=true;
    if (n==1 && fabs(r[0][1]-x)>EPS)
      g=false;
    if (n==2 && r[0][1]+EPS<x && r[1][1]+EPS<x)
      g=false;
    if (n==2 && r[0][1]>x+EPS && r[1][1]>x+EPS)
      g=false;
    if (n==1) {
      o=v/r[0][0];
    }
    else {
      if (fabs(r[0][1]-x)<EPS || fabs(r[1][1]-x)<EPS) {
        if (fabs(r[0][1]-x)<EPS && fabs(r[1][1]-x)<EPS) {
          o=v/(r[0][0]+r[1][0]);
        } else if (fabs(r[0][1]-x)<EPS) {
          o=v/r[0][0];
        } else {
          o=v/r[1][0];
        }
      }
      else {
        r1=(x-r[1][1])/(r[0][1]-r[1][1]);
        r2=1-r1;
        o=max(r1*v/r[0][0],r2*v/r[1][0]);
      }
    }
    if (g) {
      printf("%.9f\n",o);
    }
    else
      cout<<"IMPOSSIBLE"<<endl;
  }
  return 0;
}
