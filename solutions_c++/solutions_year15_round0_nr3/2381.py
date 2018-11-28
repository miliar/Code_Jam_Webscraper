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

map<char,int> mp;
char res[3][3] = 
{
  {'r','k','J'},
  {'K','r','i'},
  {'j','I','r'}
};

char result(char a,char b) {
  int sign = 1;
  if(a=='1') return b;
  if(a=='r') {
    return b + 'A' - 'a';
  }
  if(a>='A'&&a<='Z') {a -= 'A'-'a';sign*=-1;}
  a = res[mp[a]][mp[b]];
  if(a=='r') {
    if(sign == -1) return '1';
    else return 'r';
  }
  if(a>='A'&&a<='Z') {a -= 'A'-'a';sign*=-1;}
  if(sign == -1) return a + 'A' - 'a';
  else return a;
}

int main()
{
  mp['i'] = 0;
  mp['j'] = 1;
  mp['k'] = 2;
  int T;
  cin>>T;
  for(int I=1;I<=T;I++) {
    int l,x;
    cin>>l>>x;
    string s;
    cin>>s;
    char cur = '1';
    bool found_i = false;
    bool found_k = false;
    for(int i=0;i<l*x;i++) {
      cur = result(cur,s[i%l]);
      if(cur == 'i') found_i = 1;
      if(cur == 'k' && found_i) found_k = 1;
    }
    if(found_i && found_k && cur=='r') cout<<"Case #"<<I<<": YES"<<endl;
    else cout<<"Case #"<<I<<": NO"<<endl;
  }
}
