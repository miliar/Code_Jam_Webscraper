#include <stdio.h>
#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <stdlib.h>
#include <math.h>
#include <cstring>
#include <algorithm>
#include <map>
#include <set>
 
using namespace std;
 
#define fi first
#define sc second
#define ff first.first
#define fs first.second
#define sf second.first
#define ss second.second
#define pb push_back
#define mp make_pair
#define ll long long
#define dl double
#define ison(a,b) (a&(1<<b))
#define bitcnt __builtin_popcount
#define MOD 1000000007 
#define INF 1000000000
 
typedef pair<int,int> ii;
typedef pair<int,ii> iii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<iii> wadj;

char rev(char s)
{
  if(s=='+')
    return '-';
  else
    return '+';
}

int main(int argc, char const *argv[])
{
//freopen("inp.txt","r",stdin);
 //freopen("out.txt","w",stdout);
  int t;
  cin>>t;
  for(int x=1;x<=t;x++)
  {
    printf("Case #%d: ",x);
    string s;
    cin>>s;
    int cnt = 0;
    for(int i=0;i<s.size()-1;i++)
      if(s[i]!=s[i+1])
        cnt++;
    if(s[s.size()-1]=='-')
      cnt++;
  printf("%d\n",cnt);
}
 
    return 0;
}
 