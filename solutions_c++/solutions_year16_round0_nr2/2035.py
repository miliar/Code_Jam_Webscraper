#include <bits/stdc++.h>

#define ll long long
using namespace std;

int main(int argc, const char * argv[]){
int T;cin >> T;
for(int casen=0;casen<T;casen++){
string s;cin >> s;
int ans=0;
for(int i=0;i<s.size()-1;i++){
  if(s[i]!=s[i+1])ans++;
}
if(s[s.size()-1]=='-')ans++;
cout << "Case #"<<casen+1<<": "<<ans<<endl;
}
}
