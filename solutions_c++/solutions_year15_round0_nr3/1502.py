#include<cstdio>
#include<iostream>
using namespace std;
struct quat {
  int val;
  int neg;
};
int lookup_val[4][4] = {
  {0,1,2,3},
  {1,0,3,2},
  {2,3,0,1},
  {3,2,1,0}
};
int lookup_neg[4][4] = {
  {0,0,0,0},
  {0,1,0,1},
  {0,1,1,0},
  {0,0,1,1}
};
quat multiply(quat a,quat b) {
  quat n;
  n.val=lookup_val[a.val][b.val];
  n.neg=lookup_neg[a.val][b.val];
  if (a.neg!=b.neg)
    n.neg=1-n.neg;
  return n;
}
quat parse(char c) {
  quat n;
  if (c=='i')
    n.val=1;
  if (c=='j')
    n.val=2;
  if (c=='k')
    n.val=3;
  n.neg=0;
  return n;
}
/*neg divide(neg a,neg b) {
  for(int i=0;i<4;i++) {
    for(int j=0;j<2;j++) {
      neg n;
      n.val=i;
      n.neg=j;
      if
    }
  }
}*/
int main() {
  int zzz;
  cin>>zzz;
  for(int zz=1;zz<=zzz;zz++) {
    string t,s="";
    int n,m;
    cin>>n>>m;
    cin>>t;
    bool g=true;
    while(m>0) {
      s+=t;
      m--;
    }
    quat z=parse(s[0]);
    for(int i=1;i<s.size();i++)
      z=multiply(z,parse(s[i]));
    if (z.val!=0 || z.neg!=1 || s.size()<3)
      g=false;
    if (g) {
      int lo=0;
      int hi=s.size()-1;
      quat z=parse(s[0]);
      while(1) {
        if (lo==hi) {
          g=false;
          break;
        }
        if (z.neg==0 && z.val==1)
          break;
        lo++;
        z=multiply(z,parse(s[lo]));
      }
      z=parse(s[s.size()-1]);
      while(1) {
        if (lo==hi) {
          g=false;
          break;
        }
        if (z.neg==0 && z.val==3)
          break;
        hi--;
        z=multiply(parse(s[hi]),z);
      }
    }
    printf("Case #%d: ",zz);
    cout<<(g?"YES":"NO")<<endl;
  }
  return 0;
}
