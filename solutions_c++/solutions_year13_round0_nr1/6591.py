#include <iostream>
#include <string>
#include <vector>

#include <cstring>

using namespace std;

int main(void) {
  char b[4][4]={0};
  char c=0;
  string input;
  int n=0,nn=0;
  int t=false;
  int tx=0;
  int ty=0;
  int x=0;
  int o=0;
  int d=0;
  int w=0;
  cin>>n;
  nn=n;
  while (n--) {
    memset(b,0,sizeof(char)*16);
    w=t=tx=ty=x=o=d=0;
    cout<<"Case #"<<nn-n<<": ";
    for (int i=0;i<4;i++) {
      cin>>input;
      for (int j=0;j<4;j++) {
        switch (input[j]) {
        case'.':
          d++;
          break;
        case'X':
          x++;
          break;
        case'O':
          o++;
          break;
        case'T':
          t=true;
          tx=j;
          ty=i;
          break;
        }
        b[i][j]=input[j];
      }
    }
    if (d>11 || (d>9&&!t)) {
      cout<<"Game has not completed"<<endl;
      continue;
    }
    if (t) {
      //cout<<"T case && Column Check"<<endl;
      if (b[3-ty][tx]!='.') {
        b[ty][tx]=b[3-ty][tx];
        for (int i=1;i<4;i++)
          if (b[i][tx]!=b[0][tx]) {
            w=true;
            break;
          }
        if (!w) {
          cout<<b[ty][tx]<<" won"<<endl;
          continue;
        }
      }
      w=false;
      //cout<<"T case && Row Check"<<endl;
      if (b[ty][3-tx]!='.') {
        b[ty][tx]=b[ty][3-tx];
        for (int i=1;i<4;i++)
          if (b[ty][i]!=b[ty][0]) {
            w=true;
            break;
          }
        if (!w) {
          cout<<b[ty][tx]<<" won"<<endl;
          continue;
        }
      }
      w=false;
      //cout<<"T case && Diagonal Check"<<endl;
      if (tx==ty && b[3-ty][3-tx]!='.') {
        b[ty][tx]=b[3-ty][3-tx];
        for (int i=1;i<4;i++)
          if (b[i][i]!=b[0][0]) {
            w=true;
            break;
          }
        if (!w) {
          cout<<b[ty][tx]<<" won"<<endl;
          continue;
        }
      }
      w=false;
      //cout<<"T case && Anti-Diagonal Check"<<endl;
      if (tx==3-ty && b[3-ty][3-tx]!='.') {
        b[ty][tx]=b[3-ty][3-tx];
        for (int i=1;i<4;i++)
          if (b[i][3-i]!=b[0][3]) {
            w=true;
            break;
          }
        if (!w) {
          cout<<b[ty][tx]<<" won"<<endl;
          continue;
        }
      }
      w=false;
      b[ty][tx]='T';
    }
    //cout<<"Normal Case && Row Check"<<endl;
    for (int i=0;i<4;i++) {
      w=false;
      if (b[i][0]=='.') {
        w=true;
        continue;
      }
      for (int j=1;j<4;j++) {
        if (b[i][0]!=b[i][j]) {
          w=true;
          break;
        }
      }
      if (!w) {
        cout<<b[i][0]<<" won"<<endl;
        break;
      }
    }
    if (w) w=false;
    else continue;
    //cout<<"Normal Case && Column Check"<<endl;
    for (int i=0;i<4;i++) {
      w=false;
      if (b[0][i]=='.') {
        w=true;
        continue;
      }
      for (int j=1;j<4;j++) {
        if (b[0][i]!=b[j][i]) {
          w=true;
          break;
        }
      }
      if (!w) {
        cout<<b[0][i]<<" won"<<endl;
        break;
      }
    }
    if (w) w=false;
    else continue;

    //cout<<"Normal Case && Diagonal Check"<<endl;
    if (b[0][0]!='.') {
      for (int i=1;i<4;i++) {
        if (b[i][i]!=b[0][0]) {
          w=true;
          break;
        }
      }
      if (!w) {
        cout<<b[0][0]<<" won"<<endl;
        continue;
      }
      w=false;
    }
    //cout<<"Normal Case && Anti-Diagonal Check"<<endl;
    if (b[0][3]!='.') {
      for (int i=1;i<4;i++) {
        if (b[i][3-i]!=b[0][3]) {
          w=true;
          break;
        }
      }
      if (!w) {
        cout<<b[0][3]<<" won"<<endl;
        continue;
      }
      w=false;
    }

    //cout<<"Otherwise"<<endl;
    //cout<<"Dot Exist"<<endl;
    if (d>0) cout<<"Game has not completed"<<endl;
    //cout<<"No one wins"<<endl;
    else cout<<"Draw"<<endl;
    continue;
    cout<<endl<<x<<' '<<o<<' '<<d<<' '<<w<<t<<' '<<tx<<' '<<ty<<endl;

    for (int i=0;i<4;i++) {
      for (int j=0;j<4;j++)
        cout<<b[i][j];
      cout<<endl;
    }
    cout<<endl;
  }
  return 0;
}
