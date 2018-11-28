#include <iostream>
#include <algorithm>
using namespace std;

struct H{
  int x;
  int sign;
};

char code[]={'0','1','i','j','k'};

int tbl[5][5]={
  {0,0,0,0,0},
  {0,1,2,3,4},
  {0,2,-1,4,-3},
  {0,3,-4,-1,2},
  {0,4,3,-2,-1}
};

H operator *(H a,H b){
  int y = tbl[a.x][b.x];
  y*=a.sign*b.sign;
  int s=1;
  if(y<0) s=-1,y*=-1;
  H ret={y,s};
  return ret;
}

string tostr(H a){
  string ret="";
  if(a.sign<0) ret+='-';
  ret+=code[a.x];
  return ret;
}

H gen(string s){
  int y=0,t=1;
  if(s[0]=='-') t=-1;
  char c = s[s.length()-1];
  if(c=='1') y=1;
  else if(c=='i') y=2;
  else if(c=='j') y=3;
  else if(c=='k') y=4;
  H ret={y,t};
  return ret;
}

H gen(char c){
  int y=0;
  if(c=='1') y=1;
  else if(c=='i') y=2;
  else if(c=='j') y=3;
  else if(c=='k') y=4;
  H ret={y,1};
  return ret;
}

H hd[10001];
int main(){
  int T; cin>>T;
  for(int u=1;u<=T;++u){
    string s;
    int n,x;
    cin >> n >> x;
    cin >> s;
    string t="";
    string ans = "NO";
    for(int j=0;j<x;++j) t+=s;
    n=t.length();
    hd[0]=gen(t[0]);
    for(int i=1;i<n;++i) hd[i]=hd[i-1]*gen(t[i]);
    int xi = -1;
    for(int i=0;i<n;++i){
      if(xi!=-1) break;
      if(hd[i].x==2 && hd[i].sign==1) xi=i;
    }
    int xj = -1;
    for(int j=xi+1;j<n;++j){
      if(xj!=-1) break;
      if(hd[j].x==4 && hd[j].sign==1) xj=j;
    }
    if(xi!=-1 && xj!=-1 && hd[n-1].x==1 && hd[n-1].sign==-1) ans="YES";
    cout << "Case #"<<u<<": "<<ans<<endl;
  }
  return 0;
}
