#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<iostream>
#include<string>
#include<set>
#include<queue>
#include<map>
#include<vector>
#include<algorithm>
using namespace std;

#define pb push_back
#define mp make_pair
#define x first
#define y second
#define FOR(it,c) for(typeof(c) it = ((c).begin()); it != ((c).end()) ; ++it)

int flag;
int rd[20];
int n,m,K;
vector<int > arr;
int ans[20];

int dfs(int now, int dep){
  rd[dep] = now;
  if(dep==n-1){
    //printf("Gogo:");
    //for(int i=0;i<n;i++)printf("%d",rd[i]);
    long long total = 1;
    for(int i=0;i<=dep;i++){
      total *= rd[i];
    }
    //printf("total %lld\n",total);
    arr.clear();
    for(long long i=1;i*i<=total;i++){
      if(total%i==0){
        arr.pb(i);
        arr.pb(total/i);
      }
    }
    sort(arr.begin(),arr.end());
    //for(int i=0;i<int(arr.size());i++) cout << arr[i] << " ";
    //cout << endl;
    for(int i=0;i<K;i++){
      if(total%ans[i]!=0)return 0;
    }
    //for(int i=0;i<K;i++)
      //cout << ans[i] << " ";
    //cout << endl;
    flag = 1;
    for(int i=0;i<n;i++) cout << rd[i];
    cout << endl;
    return 0;
  }
  for(int i=2;flag==0 &&i<=m;i++){
    dfs(i,dep+1);
  }
  return 0;
}

int main()
{
  int tn;
  int z;
  int R;
  cin >> tn;
  for(z=1;z<=tn;z++){
    printf("Case #%d:\n",z);
    cin >> R >> n >> m >> K;
    while(R--){
      flag = 0;
      for(int i=0;i<K;i++){
        cin >> ans[i];
      }
      for(int i=2;i<=m;i++){
        if(dfs(i,0))break;
      }
      //printf("end\n");
      if(!flag){
        for(int i=0;i<n;i++)cout << '2';
        cout << endl;
      }
    }
  }
  return 0;
}
