#include <iostream>
#include <string>
#include <algorithm>
#include <cstdlib>
#include <vector>

using namespace std;

int n;
int ans;
bool build;
int f[10];

void dfs(vector<int> a, int dep){
  int est=dep;
  if (a.size() && build) est+=f[*max_element(a.begin(), a.end())];
  if (est>=ans)
    return;    
  if (a.size()==0){
    ans=min(ans, dep);
    return;
  }

  vector<int> b,c;
  for(auto x: a)
    if (x>1)
      b.push_back(x-1);
  dfs(b,dep+1);

  for(int i=0, n=a.size(); i<n; i++)
    if (a[i]>1){
      c.clear();
      for(int j=0; j<n; j++)
        if (j!=i)
          c.push_back(a[j]);
      for(int k=1; k<=a[i]/2; k++){
        c.push_back(k);
        c.push_back(a[i]-k);
        dfs(c,dep+1);
        c.pop_back();
        c.pop_back();
      }
    }
}

int main(){
  freopen("b.in","r",stdin);

  build=0;
  for(int i=1; i<=9; i++){
    vector<int> a;
    a.push_back(i);
    ans=10;
    dfs(a,0);
    f[i]=ans;
    cout<<i<<": "<<f[i]<<endl;
  }
  freopen("b.out","w",stdout);
  
  build=1;
  int T;
  cin>>T;
  for(int tt=1; tt<=T; tt++){
    printf("Case #%d: ",tt);
    vector<int> a;
    cin>>n;
    for(int i=0, x; i<n; i++){
      cin>>x;
      a.push_back(x);
    }
    ans=10;
    dfs(a, 0);
    cout<<ans<<endl;
  }

  return 0;
}
