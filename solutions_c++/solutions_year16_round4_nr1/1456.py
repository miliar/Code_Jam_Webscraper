#include <bits/stdc++.h>
using namespace std;

#define dbg(x) cerr<<#x<<"="<<x<<endl
typedef long long ll;
typedef pair<int,int> pii;

char str[1000000];
int N,R,P,S;	

char winner(char a, char b){
  if((a=='R' && b=='S') || (a=='S' && b=='P') || (a=='P' && b=='R'))
    return a;
  return b;
}

bool check(){
  vector<char> v1,v2;
  for(int i=0;i<N;i++)
    v1.push_back(str[i]);
  while(v1.size()>1){
    v2.clear();
    for(int i=0;i<v1.size();i+=2){
      if(v1[i]==v1[i+1])
	return false;
      v2.push_back(winner(v1[i],v1[i+1]));
    }
    v1 = v2;
  }
  return true;
}

bool f(int p,int r,int s, int i =0){
  if(i==N){
    if(check()){
      str[N]=0;
      cout<<str;
      return true;
    }
    return false;
  }
  if(p){
    str[i]='P';
    if(f(p-1,r,s,i+1))
      return true;
  }
  if(r){
    str[i]='R';
    if(f(p,r-1,s,i+1))
      return true;
  }
  if(s){
    str[i]='S';
    if(f(p,r,s-1,i+1))
      return true;
  }
  return false;
}

void run(){

  cin>>N>>R>>P>>S;
  N = 1<<N;
  if(!f(P,R,S)){
    cout<<"IMPOSSIBLE";
  }
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
