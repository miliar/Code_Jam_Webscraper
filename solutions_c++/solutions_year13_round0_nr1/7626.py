#include<iostream>
using namespace std;
string s[4];
int a;
char c;
bool p = 0;
string spr(){
  string w;
  for(int t = 0; t<2; ++t){
    if(t == 0){w="X ";c='X';}
    else {w="O ";c='O';}
    for(int i = 0; i<4; ++i){ //wiersze
      int l = 0;
      for(int j = 0; j<4; ++j)if(s[i][j]==c || s[i][j]=='T')++l;
      if(l==4){w+="won\n";return w;}
    }
    for(int i = 0; i<4; ++i){ //kolumny
      int l = 0;
      for(int j = 0; j<4; ++j)if(s[j][i]==c || s[j][i]=='T')++l;
      if(l==4){w+="won\n";return w;}
    }
    for(int i = 0; i<4; ++i){ //skosy
      if(s[i][i]!=c && s[i][i]!='T')break;
      if(i==3){w+="won\n";return w;}
    }
    for(int i = 0; i<4; ++i){ //skosy
      if(s[i][3-i]!=c && s[i][3-i]!='T')break;
      if(i==3){w+="won\n";return w;}
    }        
  }
  for(int i = 0; i<4; ++i)
    for(int j = 0; j<4; ++j)
      if(s[i][j]=='.')return "Game has not completed\n";
  return "Draw\n";
}
int main(){
  ios_base::sync_with_stdio(0);
  cin >> a;
  for(int j =1; j<=a; ++j){
  for(int i =0; i<4;++i)cin>>s[i];
    cout <<"Case #"<<j<<": "<< spr();
  }
  return 0;
}