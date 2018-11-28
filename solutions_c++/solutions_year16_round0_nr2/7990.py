#include<bits/stdc++.h>
using namespace std;
int T;
string str;
map<string,int> d;

int solve(){
  d.clear();
  queue<string> Q;
  Q.push(str);
  d[str]=0;
  while(!Q.empty()){
    string s=Q.front();Q.pop();
    int cnt=0;
    for(int i=0;i<(int)s.size();i++)
      if(s[i]=='+')cnt++;
    if(cnt==(int)s.size())return d[s];
    for(int i=0;i<(int)s.size();i++){
      string next=s;
      for(int j=0;j<=i;j++){
        if(next[j]=='+')next[j]='-';
        else if(next[j]=='-')next[j]='+';
      }
      reverse(next.begin(),next.begin()+i+1);
      if(d.count(next))continue;
      d[next]=d[s]+1;
      Q.push(next);
    }

  }
  return -1;
}

int main(){
  cin>>T;
  for(int tc=1;tc<=T;tc++){
    cin>>str;
    cout<<"Case #"<<tc<<": ";
    cout<<solve()<<endl;
  }
  return 0;
}
