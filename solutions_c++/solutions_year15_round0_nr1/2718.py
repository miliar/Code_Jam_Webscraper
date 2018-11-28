#include <cstdlib>
#include<cstdio>
#include<iostream>
#include<math.h>
#include<vector>
#include<map>
#include<string.h>
#include<queue>
#include<algorithm>
#include<string.h>
#include <stack>
using namespace std;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> ii;
typedef unsigned long long ulint;
typedef long long lint;

int main()
{
  int T;
  cin>>T;
  for(int i=1;i<=T;i++) {
    int sMax;
    cin>>sMax;
    string s;
    cin>>s;
    int count = s[0]-'0';
    int additional = 0;
    for(int i=1;i<=sMax;i++) {
      if(i<=count) {
        count+=s[i]-'0';
      } else if(s[i]>'0'){
        additional+=i-count;
        count=i+(s[i]-'0');
      }
    }
    cout<<"Case #"<<i<<": "<<additional<<endl;
  }
}
