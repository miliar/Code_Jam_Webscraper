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
#include <sstream>
using namespace std;
struct node{
  int c;
  node *child[30];
};
int n;
int best;
node* tree[2];
vector<string> a[100];
bool used[200];
node* insert(node *tree, string s) {
  if (tree==NULL) {
    tree=new node();
    tree->c=0;
    for(int i=0;i<30;i++)
      tree->child[i]=NULL;
  }
  if (s=="")
    tree->c++;
  else {
    tree->child[s[0]-'a']=insert(tree->child[s[0]-'a'],s.substr(1));
  }
  return tree;
}
int query(node *tree, string s) {
  if (tree==NULL)
    return 0;
  if (s=="")
    return (tree->c?1:0);
  else
    return query(tree->child[s[0]-'a'],s.substr(1));
}
node* remove(node *tree, string s) {
  //if (tree==NULL)
  //  cerr<<"WHAT\n";
  if (s=="")
    tree->c--;
  else
    tree->child[s[0]-'a']=remove(tree->child[s[0]-'a'],s.substr(1));
  return tree;
}
void f(int p,int c) {
  if (c>best)
    return;
  if (p==n) {
    best=min(best,c);
  }
  else {
    int z=0;
    memset(used,0,sizeof(used));
    for (int i=0;i<a[p].size();i++) {
      if (query(tree[0],a[p][i])==0) {
        z+=query(tree[1],a[p][i]);
      }
      used[i]=true;
      tree[0]=insert(tree[0],a[p][i]);
    }
    f(p+1,c+z);
    for (int i=0;i<a[p].size();i++) {
      //if (used[i]) {
      tree[0]=remove(tree[0],a[p][i]);
      //}
    }
    z=0;
    memset(used,0,sizeof(used));
    for (int i=0;i<a[p].size();i++) {
      if (query(tree[1],a[p][i])==0) {
        z+=query(tree[0],a[p][i]);
      }
      used[i]=true;
      tree[1]=insert(tree[1],a[p][i]);
    }
    f(p+1,c+z);
    for (int i=0;i<a[p].size();i++) {
      //if (used[i]) {
      tree[1]=remove(tree[1],a[p][i]);
      //}
    }
  }
}
int main() {
  int zzz;
  cin>>zzz;
  for (int zz=1;zz<=zzz;zz++) {
    tree[0]=NULL;
    tree[1]=NULL;
    best=1000000000;
    string t;
    cin>>n;
    getline(cin,t);
    for(int i=0;i<n;i++) {
      a[i].clear();
      getline(cin,t);
      stringstream ss(t);
      while(ss>>t) {
        a[i].push_back(t);
      }
    }
    int z=0;
    for (int i=0;i<a[0].size();i++) {
      //if (query(tree[0],a[0][i])==0) {
      tree[0]=insert(tree[0],a[0][i]);
      //}
    }
    for (int i=0;i<a[1].size();i++) {
      if (query(tree[1],a[1][i])==0) {
        z+=query(tree[0],a[1][i]);
      }
      tree[1]=insert(tree[1],a[1][i]);
    }
    f(2,z);
    printf("Case #%d: %d\n",zz,best);
  }
  return 0;
}
