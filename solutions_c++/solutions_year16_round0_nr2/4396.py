#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<set>
#include<map>
#include<queue>

using namespace std;

typedef long long in;

int main(){
  ios::sync_with_stdio(false);
  int t;
  cin >> t;
  for(int test=1;test<=t;test++){
    string s;
    cin >> s;
    int ctx=0;
    int cty=0;
    if(s[0]=='-')
      cty=1;
    for(int i=0;i<s.size()-1;i++){
      if(s[i]=='+'&&s[i+1]=='-')
	ctx++;
    }
    cout << "Case #" << test << ": " << 2*ctx+cty << endl;
  }
  return 0;
}
  