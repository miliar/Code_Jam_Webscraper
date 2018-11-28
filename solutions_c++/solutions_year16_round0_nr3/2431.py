#include<iostream>
#include <map>
#include <vector>
#include <stack>
#include <cassert>
using namespace std;
#define lint unsigned long long int

vector<int> divi;
int N,J;
lint P[11][32];

lint isPrime(lint V){
  if(V%2==0)
    return 2;
  for(lint i=3;i*i<=V;i+=2){
    if(V%i==0)
      return i;
  }
  return 0;
}

void printbin(lint val){
  stack<int> s;
  while(val>0){
    s.push(val%2);
    val/=2;
  }
  while(!s.empty()){
    cout<<s.top();
    s.pop();
  }
}
void preproc(){
  for(int i=2;i<11;i++)
    P[i][0]=1;
  for(int i=2;i<11;i++)
    for(int j=1;j<32;j++)
      P[i][j]=P[i][j-1]*i;
}

void solve(int N,int J){
  int found = 0;
  vector<lint> cur(11,1);
  for(int i=1;i<N;i++)
    for(int j=2;j<=10;j++)
      cur[j]*=j;
  for(int j=2;j<=10;j++)
    cur[j]++;
  vector<bool> bin(N-2,false);
  while(found<J){
    //    printbin(cur[2]);cout<<endl;
    vector<lint> s;
    for(int j=2;j<=10;j++){
      lint res = isPrime(cur[j]);
      if(res==0)
	break;
      assert(cur[j]%res==0);
      s.push_back(res);
    }
    if(s.size()==9){
      found++;
      printbin(cur[2]);
      for(lint div:s)
	cout<<" "<<div;
      cout<<endl;
    }
    int i= 0;
    while(true){
      if(bin[i]==false){
	bin[i]=true;
	for(int j=2;j<=10;j++)
	  cur[j]+=P[j][i+1];
	break;
      }else{
	bin[i]=false;
	for(int j=2;j<=10;j++)
	  cur[j]-=P[j][i+1];
      }
      i++;
    }
  }
  
  
}

int main(){
  int t;
  cout<<"Case #1:"<<endl;
  cin>>t;
  cin>>N>>J;
  preproc();
  solve(N,J);
  return 0;
}
