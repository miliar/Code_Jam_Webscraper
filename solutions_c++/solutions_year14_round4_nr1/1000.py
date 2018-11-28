#include<iostream>
#include<deque>
#include<algorithm>

using namespace std;

int main(){
  int T;
  cin>>T;
  for(int i=1;i<=T;i++){
    int N,X;
    cin>>N>>X;
    deque<int> deq(N);
    for(int i=0;i<N;i++){
      cin>>deq[i];
    }
    sort(deq.rbegin(),deq.rend());
    int c=0;
    while(!deq.empty()){
      c++;
      if(deq.size()==1){
	deq.pop_back();
      }else{
	if(deq[0]+deq.back()<=X){
	  deq.pop_front();
	  deq.pop_back();
	}else{
	  deq.pop_front();
	}
      }
    }
    cout<<"Case #"<<i<<": "<<c<<endl;
  }
}
