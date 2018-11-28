#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
int R,C;

string M[100];

int I[4]={-1,0,1,0};
int J[4]={0,1,0,-1};

int dir(char c){
  switch(c){
  case '^':
    return 0;
  case '>':
    return 1;
  case 'v':
    return 2;
  case '<':
    return 3;
  }

}

bool cadi(int i,int j, int d){
  if(i<0 || j<0)
    return true;
  if(i>=R || j>=C)
    return true;
  if(M[i][j]!='.')
    return false;
  return cadi(i+I[d],j+J[d],d);
}

int flip(int i,int j){
  char el=M[i][j];
  int d=dir(el);
  bool c=cadi(i+I[d],j+J[d],d);
  if(!c)
    return 0;
  for(int dd=0;dd<4;dd++)
    if(dd!=d){
    if(!cadi(i+I[dd],j+J[dd],dd)){
	return 1;
      }
    }
  return -1;
}



void solve(){
  cin>>R>>C;
  for(int i=0;i<R;i++){
    cin>>M[i];
  }
  int c=0;
  for(int i=0;i<R;i++)
    for(int j=0;j<C;j++){
      if(M[i][j]!='.'){
	int res=flip(i,j);
	if(res==-1){
	  cout<<"IMPOSSIBLE";
	  return;
	}
	c+=res;
      }
    }
  cout<<c;
  return;
}

int main(){
  int cases;
  cin>>cases;
  for(int i=0;i<cases;i++){
    cout<<"Case #"<<i+1<<": ";
    solve();
    cout<<endl;
  }
  return 0;
}
