#include <iostream>
#include <string>
#include <vector>
using namespace std;
int cas, T;
int B;
int M;
int p;
int arr[16][16];

int sol1() {
  p = 1;
  for (int i=2; i<B; ++i)
    p*=2;
  return (M>p);
}

void permutex(int add) {
  while (1) {
    int id1=rand()%B;
    int id2=rand()%B;
    if (id1>=id2) continue;
    if (add && !arr[id1][id2]) {arr[id1][id2]=1; return;}
    if (!add && arr[id1][id2]) {arr[id1][id2]=0; return;}
  }
}

int countpath() {
  int ret=0;
  for (int mask=0; mask<p; ++mask) {
    vector<int> nodes;
    int tmp = mask, id=1;
    nodes.push_back(0);
    while (tmp) {
      if (tmp%2) nodes.push_back(id);
      tmp=tmp>>1;
      ++id;
    }
    nodes.push_back(B-1);

    int flag=1;
    for (int i=1; i<nodes.size(); ++i)
      if (arr[nodes[i-1]][nodes[i]]==0)
        {flag=0; break;}
    ret+=flag;
  }
  return ret;
}

void shows() {
  for (int i=0; i<B; ++i) {
    for (int j=0; j<B; ++j)
      cout<<arr[i][j];
    cout<<endl;
  }
}

void sol() {
  int cur;

  while (1) {
    cur = countpath();
    if (cur==M) return;
    if (cur==M-1 && !arr[0][B-1]) {
      arr[0][B-1]=1; return;
    }
    if (cur==M+1 && arr[0][B-1]) {
      arr[0][B-1]=0; return;
    }
    permutex(M>cur);
  }
}

int main() {
  cin>>T;
  for (cas=1; cas<=T; ++cas) {
    cin>>B>>M;
    
    if (sol1()) {
      cout<<"Case #"<<cas<<": IMPOSSIBLE\n";
      continue;
    }
    cout<<"Case #"<<cas<<": POSSIBLE\n";
    for (int i=0; i<B; ++i)
    for (int j=0; j<B; ++j)
      arr[i][j]=0;
    sol();
    shows();
  }
  return 0;
}
