#include <iostream>
#include <cstdio>
#include <vector>
#include <list>
#include <cmath>
#include <fstream>
#include <algorithm>
#include <string>
#include <queue>
#include <set>
#include <map>
#include <complex>
#include <iterator>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <stack>
#include <climits>
#include <deque>
#include <bitset>
#include <cassert>
#include <ctime>
using namespace std;

typedef long long ll;
typedef pair<int,int> pii;
// adjust problem by problem
const double EPS=1e-8;
const double PI=acos(-1.0);
// rep macro
#define REP(i,x,n) for(int i=x;i<(int)(n);++i)
#define rep(i,n) REP(i,0,n)
#define RREP(i,x,n) for(int i=x;i>=(int)(n);--i)
#define rrep(i,n) RREP(i,n,0)
#ifdef __GNUC__
#define FOR(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
int popcount(int n){return __builtin_popcount(n);}
int popcount(ll n){return __builtin_popcountll(n);}
#endif
#ifndef __GNUC__
int popcount(unsigned int n){int cnt=0;for(int i=0;i<32;i++)if((n>>i)&1)cnt++;return cnt;}
int popcountll(unsigned ll n){int cnt=0;for(int i=0;i<64;i++)if((n>>i)&1)cnt++;return cnt;}
#endif
template<class T>int SIZE(T a){return a.size();}
template<class T>string IntToString(T num){string res;stringstream ss;ss<<num;return ss.str();}
template<class T>T gcd(T a,T b){if(b==0)return a;return gcd(b,a%b);}
template<class T>T lcm(T a,T b){return a/gcd(a,b)*b;}
ll getTen(int a){return (a<=0)?1:(getTen(a-1)*10);}
bool EQ(double a,double b){return abs(a-b)<EPS;}
void fastStream(){cin.tie(0);std::ios_base::sync_with_stdio(0);}
vector<string> split(string str,char del){
  vector<string> res;
  for(int i=0,s=0;i<SIZE(str);i++){
    if(str[i]==del){if(i-s!=0)res.push_back(str.substr(s,i-s));s=i+1;}
    else if(i==SIZE(str)-1){res.push_back(str.substr(s));}
  }
  return res;
}
struct TimeWatch{
  clock_t start_,end_;
  void start(){start_=clock();}
  double stop(){return (double)(clock()-start_)/CLOCKS_PER_SEC;}
};

int N,M;
string strs[1100];
void input(){
  cin>>M>>N;
  for(int i=0;i<M;i++)cin>>strs[i];
}

/*
  Trieを管理するクラス
  現在の実装では、小文字のみ含む文字列にだけ対応している
  大文字や、他のアスキー文字に対応させたい場合は、
  childrenの配列サイズを大きくとれば良い
  機能:
  addで文字列をtrieに追加していく
  各文字ノードの個数や、各ノードの子孫のノードの数をO(1)で数え上げることができる
  また、ある文字列が存在するかをfindで検索することができる
  デストラクタでメモリが自動的に解法される
 */
class Trie{
public:
  // Trieのノード
  // self_char:自身のchar(-1の場合、root)
  // children:次の文字ノードへのポインタ
  // sum_of_descendant_and_self:現在のノードの子孫の合計ノード数
  struct node_t{
    char self_char;
    int sum_of_descendant;
    node_t *children[26];
    node_t(char node_char){
      self_char=node_char;
      sum_of_descendant=0;
      for(int i=0;i<26;i++)children[i]=NULL;
    }
    node_t(){
      self_char=-1;
      sum_of_descendant=0;
      for(int i=0;i<26;i++)children[i]=NULL;
    }
  };
  Trie(){
    root=new node_t();
    for(int i=0;i<(int)(sizeof(nodes_sum)/sizeof(nodes_sum[0]));i++)
      nodes_sum[i]=0;
    node_cnt=0;
  }
  // trieを消去
  ~Trie(){
    _del(root);
  }
  // trieにstringを追加
  void add(const string &str){
    _add(str,0,root);
  }
  // 文字列がtrie中に存在するか検索
  // 末尾まで辿れなくても発見したものとみなす
  bool find(const string &str){
    return _find(str,0,root);
  }
  int node_cnt;
private:
  bool _find(const string &str,int str_pos,node_t *cur){
    if(str_pos==(int)str.size())return true;
    else{
      node_t *nxt=cur->children[str[str_pos]-'A'];
      if(nxt==NULL)return false;
      else return _find(str,str_pos+1,nxt);
    }
  }
  void _del(node_t *cur){
    if(cur==NULL)return;
    for(int i=0;i<26;i++)
      _del(cur->children[i]);
    delete cur;
  }
  // trieにstringを追加
  int _add(const string &str,int str_pos,node_t *cur){
    if(str_pos==(int)str.size())return cur->sum_of_descendant+1;
    else{
      int prv_sum=0;
      if(cur->children[str[str_pos]-'A']==NULL){
        cur->children[str[str_pos]-'A']=new node_t(str[str_pos]);
        node_cnt++;
        nodes_sum[str[str_pos]-'A']++;
      }
      else
        prv_sum=cur->children[str[str_pos]-'A']->sum_of_descendant+1;
      cur->sum_of_descendant-=prv_sum;
      int cur_sum=_add(str,str_pos+1,cur->children[str[str_pos]-'A']);
      cur->sum_of_descendant+=cur_sum;
      return cur->sum_of_descendant+1;
    }
  }
public:
  // Trieのroot
  node_t *root;
  // 文字ごとのノード数
  int nodes_sum[26];
};


bool is_used[1010];
int ary[1010];
int max_node;
int max_node_match_cnt;


void dfs2(int pos,vector<int> vecs[]){
  if(pos==M){
    for(int i=0;i<N;i++){
      if(vecs[i].size()==0)return;
    }
    // それぞれでtrieを作成
    // ノード数を計算する
    int sum=0;
    //cout<<"####"<<endl;
    for(int i=0;i<N;i++){
      Trie trie;
      for(int j=0;j<(int)vecs[i].size();j++){
        int idx=vecs[i][j];
        trie.add(strs[idx]);
        //cout<<i<<" "<<vecs[i][j]<<endl;
      }
      sum+=trie.node_cnt+1;
    }
    //cout<<sum<<endl;
    if(sum>max_node){
      max_node=sum;
      max_node_match_cnt=1;
    }
    else if(sum==max_node)
      max_node_match_cnt++;
  }
  else{
    for(int i=0;i<N;i++){
      vecs[i].push_back(pos);
      dfs2(pos+1,vecs);
      vecs[i].pop_back();
    }
  }
}

// void dfs1(int pos,int sz){
//   if(pos==M){
//     // のこっている要素を割り振る
//     vector<int> vecs[N];
//     for(int i=0;i<sz;i++){
//       vecs[i].push_back(ary[i]);
//       //cout<<ary[i]<<" ";
//     }//cout<<endl;
//     dfs2(0,vecs);
//   }
//   else{
//     if(sz<N){
//       ary[sz]=pos;
//       is_used[pos]=true;
//       dfs1(pos+1,sz+1);
//       is_used[pos]=false;
//     }
//     if(M-pos>N-sz){
//       dfs1(pos+1,sz);
//     }
//   }
// }


void solve_small(){
  input();
  max_node=0;
  max_node_match_cnt=0;
  // 再帰的に集合を分割
  vector<int> vecs[N];
  dfs2(0,vecs);
  cout<<max_node<<" "<<max_node_match_cnt<<endl;
}

int main(){
  fastStream();
  int T;
  cin>>T;
  for(int t=1;t<=T;t++){
    cout<<"Case #"<<t<<": ";
    solve_small();
  }
  
  
  return 0;
}
