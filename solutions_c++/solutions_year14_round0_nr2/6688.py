#include<iostream>
#include<algorithm>
#include<vector>
#include<cstdio>

using namespace std;

int main() {
  int T;
  cin>>T;

  for(int t=1;t<=T;++t) {
    double C,F,X;
    cin>>C>>F>>X;
    double p,s,tmp,d;
    d=2.0;
    p=X/d;
    s=tmp=0.0;
    while(true) {
      tmp+=(C/d);
      s=tmp+(X/(d+F));

      //      cout<<"p: "<<p<<" s: "<<s<<endl;

      if(p<=s)
	break;
      p=s;
      d+=F;
    }
    printf("Case #%d: %0.7f\n",t,p);
  }
  return 0;
}
