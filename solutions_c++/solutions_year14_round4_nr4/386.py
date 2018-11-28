#include <vector>
#include <cstdio>
#include <set>
#include <map>
#include <algorithm>
#include <cstdlib>
#include <sstream>
#include <numeric>
#include <queue>
#include <iostream>
#include <string>
#include <cstring>
#include <utility>
#define sz(a) ((int)(a).size())
#define pb push_back
#define mk make_pair
#define fi first
#define se second
#define Rep(i,j,k) for (int i=(j); i<=(k); i++)
#define Repd(i,j,k) for (int i=(j); i>=(k); i--)
#define ALL(c) (c).begin(),(c).end()
#define TR(c,i) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define SUM(a) accumulate(all(a),string())
#define online1
#define RAND ((rand()<<15)+rand())
using namespace std;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int,int> II;
typedef long long LL;
#include <cmath>

int m, n, ans, num_of_ans;
string a[1000];
vector<string> f[10];

class TrieNode{
public:
  TrieNode *go[26];
  TrieNode(){
    memset(go,0,sizeof go);
  }
};

int count(int fi){
  TrieNode *root=new TrieNode;
  if (!f[fi].size())
    return 0;
  int ret=1;
  for(const auto &s: f[fi]){
    TrieNode *now=root;
    for(auto c: s){
      if (!now->go[c-'A']){
        now->go[c-'A']=new TrieNode;
        ret++;
      }
      now=now->go[c-'A'];
    }
  }
  return ret;
}

void doit(int id){
  if (id==m+1){
    int cnt=0;
    Rep(i,1,n)
      cnt+=count(i);
    if (cnt>ans)
      ans=cnt, num_of_ans=0;
    if (cnt==ans){
      num_of_ans++;
      if (0){
        cout<<"----"<<endl;
        Rep(i,1,n){
          for(auto s: f[i])
            cout<<s<<" ";
          cout<<endl;
        }
      }
    }
    return; 
  }
  Rep(i,1,n){
    f[i].push_back(a[id]);
    doit(id+1);
    f[i].pop_back();
  }
}

int main(){
  freopen("d.in","r",stdin);
  freopen("d.out","w",stdout);
  int T;
  cin>>T;
  
  Rep(tt,1,T){
    cout<<"Case #"<<tt<<": ";
    
    cin>>m>>n;
    Rep(i,1,m)
      cin>>a[i];
    
    ans=0;

    doit(1);

    cout<<ans<<" "<<num_of_ans<<endl;
  }

  return 0;
}
