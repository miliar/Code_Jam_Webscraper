#include <iostream>
#include <string>
#include <algorithm>
#include <cstdlib>
#include <vector>

using namespace std;

const int mul[4][4]={{0,1,2,3},
                     {1,-4,3,-2},
                     {2,-3,-4,1},
                     {3,2,-1,-4}};

int Mul(int a, int b){
  int ax,ay,bx,by;
  if (a>=0)
    ax=1, ay=a;
  else
    ax=-1, ay=-a;
  if (ay==4) ay=0;
  if (b>=0)
    bx=1, by=b;
  else
    bx=-1, by=-b;
  if (by==4) by=0;
  return ax*bx*mul[ay][by];
}

int A[10000+10];
int F[10000+10];
int L,X;
string S;

int main(){
  freopen("c.in","r",stdin);
  freopen("c.out","w",stdout);

  int T;
  cin>>T;
  for(int tt=1; tt<=T; tt++){
    printf("Case #%d: ",tt);
    cin>>L>>X;
    cin>>S;
    for(int i=0; i<L*X; i++)
      A[i]=S[i%L]-'i'+1;
    F[L*X]=0;
    for(int i=L*X-1; i>=0; i--)
      F[i]=Mul(A[i], F[i+1]);
    bool found=0;
    for(int i=0, I=0; i<L*X && !found; i++){
      I=Mul(I,A[i]);
      for(int j=i+1, J=0; j<L*X && !found; j++){
        J=Mul(J,A[j]);
        if (I==1 && J==2 && F[j+1]==3)
          found=1;
      }
    }
    if (found) cout<<"YES\n"; else cout<<"NO\n";
  }

  return 0;
}
