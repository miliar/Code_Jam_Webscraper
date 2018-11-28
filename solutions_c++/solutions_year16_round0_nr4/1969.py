#include <bits/stdc++.h>

#define ll unsigned long long
using namespace std;

int main(int argc, const char * argv[]){
int T;cin >> T;
for(int casen=1;casen<=T;casen++){
ll K,C,S;
cin >> K >> C>>S;
cout << "Case #"<<casen<<": ";
if(S*C<K){
  cout <<"IMPOSSIBLE"<<endl;
  continue;
}
ll i=1;
ll count=1;
ll num=1;
while(i<=K){
  if(count==C || i==K)
    {cout <<num<<" ";num=++i;count=1;continue;}
    num--;
  num*=K;
  num+=++i;
  count++;
}

cout<<endl;
}
}
