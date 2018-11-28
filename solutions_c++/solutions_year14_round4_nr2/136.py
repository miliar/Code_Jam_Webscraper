#include<cassert>
#include<cstdio>
#include<algorithm>
#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<numeric>
#include<cmath>
using namespace std;

#define ALL(t) t.begin(),t.end()
#define FOR(i,n) for (int i=0;i<(int)(n);i++)
#define FOREACH(i,t) for (typeof(t.begin())i=t.begin();i!=t.end();i++)
typedef vector<int> vi;
typedef long long int64;

int n,t[101000],s[101000];
int main(){
  int c;
  scanf("%d",&c);
  for(int cc=1;cc<=c;cc++){
    scanf("%d",&n);
    for(int i=0;i<n;i++)scanf("%d",&t[i]);
    FOR(i,n)s[i]=t[i];
    sort(s,s+n);
    int ans=0;
    for(int i=n-1;i>=0;i--){
      int pos=0;
      while(t[pos]!=s[i])++pos;
      int x=0,y=0;
      FOR(j,n)if(t[j]>s[i]){
        x+=j>pos;
        y+=j<pos;
      }
      //cout<<s[i]<<" "<<x<<","<<y<<endl;
      ans+=min(x,y);
    }
    printf("Case #%d: %d\n",cc,ans);
  }
}
