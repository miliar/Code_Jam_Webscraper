#include <bits/stdc++.h>
using namespace std;
typedef long long ll;


int main(int argc, const char * argv[]){
  int TT;cin >> TT;
  for(int ii=0;ii<TT;ii++){
string s;
cin >> s;
//cout << s;
deque<char> q;
for(int i=0;i<s.size();i++){
  if(i==0){q.push_back(s[i]);continue;}
  if(s[i]>=q[0])
    q.push_front(s[i]);
  else
    q.push_back(s[i]);
    //cout << s[i];
}
cout << "Case #"<<ii+1<<": ";
for(auto i:q)
  cout << i;
cout << endl;

}
}
