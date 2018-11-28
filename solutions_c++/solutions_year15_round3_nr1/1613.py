#include <vector>
#include <cstdlib>
#include <iostream>
#include <iomanip>
#include <string>
#include <ctime>
#include <string>
#include <stdio.h>
#include <math.h>
#include <algorithm>
//#include <bits/stdc++.h>
#define MAXN 100050
#define pb push_back
#define rep(i,a,b) for(int i=(a);i<(b);i++)
#define re(i,b) for(int i=(0);i<(b);i++)
#define MOD 1000000007
typedef long long int lli;
using namespace std;
int solve(int r,int c,int w)
{
  if(w==c)
    return c;
  else
  {
    return (ceil((c*1.0)/w) -1 + w);
  }
}
int main()
{
  int t;
  scanf("%d",&t);
  rep(i,1,t+1)
  {
    int result=0,N,r,c,w;
    scanf("%d %d %d",&r,&c,&w);
    result = solve(r,c,w);
    printf("Case #%d: %d\n",t,result);
 
  }
  return 0;
}