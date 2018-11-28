#include <bits/stdc++.h>
#define f first
#define s second
using namespace std;
typedef pair<int,int> P;

int main(){
  int N;
  cin>>N;
  for(int q=1;q<=N;q++){
    int n;
    cin>>n;
    priority_queue<P> Q;
    for(int i=0,a;i<n;i++) cin>>a,Q.push(P(a,i));
    
    cout <<"Case #"<<q<<":";
    int f=1;
    while(1){
      if(Q.size()==2&&Q.top().f==1)break;
      P a=Q.top();Q.pop();
      if(a.f!=1)Q.push(P(a.f-1,a.s));
      if(f)cout <<" ";
      cout <<char(a.s+'A');
      f=!f;
    }
    
    cout <<" "<<"BA"<<endl;

  }
}
