#include <bits/stdc++.h>
using namespace std;

#define dbg(x) cerr<<#x<<"="<<x<<endl
typedef long long ll;
typedef pair<int,int> pii;

int bit_cnt(int x){
  return __builtin_popcount(x);
}

int N;
char opch[10][10];
int op[10];
int cost[1<<5];

int newop[10];

bool check(vector<int> &order, int i=0, int used=0){
  if(i==N)
    return true;
  int w = order[i];
  int mach = newop[w];
  if((used&mach) == mach)
    return false;
  for(int m=0;m<N;m++){
    if((1<<m)&mach)
      if(!((1<<m)&used)){
	if(check(order, i+1, used|(1<<m))==false)
	  return false;
      }
  }
  return true;
}

int f(int w){
  if(w==N){
    vector<int> v;
    for(int i=0;i<N;i++)
      v.push_back(i);
    do{
      if(check(v)==false)
	return 100;
    }while(next_permutation(v.begin(),v.end()));
    return 0;
  }
  int res = 100;
  for(int m=1;m<(1<<N);m++){
    if((m&op[w])==op[w]){
      newop[w] = m;
      res = min(res, bit_cnt(m-op[w]) + f(w+1));
    }
  }
  return res;
}

void run(){
  cin>>N;
  for(int i=0;i<N;i++){
    cin>>opch[i];
    op[i]=0;
    for(int j=0;j<N;j++){
      if(opch[i][j]=='1')
	op[i] |= (1<<j);
    }
  }
  
  cout<<f(0);
}


int main(){
  int T;
  cin>>T;
  for(int t=1;t<=T;t++){
    cout<<"Case #"<<t<<": ";
    run();
    cout<<endl;
  }
  return 0;
}
