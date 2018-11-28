#include<iostream>
#include<vector>

using namespace std;

int main() {
  int T;
  cin>>T;
  for (int t=1;t<=T;t++){
    int n,r,p,s;
    cin>>n>>r>>p>>s;
    int pr, rs, sp;
    int N=1<<n;
    int ok=1;
    while(ok && N>1) {
      pr = N/2-s;
      rs = N/2-p;
      sp = N/2-r;
      if (pr<0 || rs<0 || sp<0){
	ok=0;
	break;
      }
      r = rs;
      p = pr;
      s = sp;
      N = N/2;
    }
    if (N!=1) {
      cout<<"Case #"<<t<<": IMPOSSIBLE"<<endl;
      continue;
    }
    string res ="";
    string res2;
    if (r==1) res = "R";
    if (p==1) res = "P";
    if (s==1) res = "S";
    for (int i=0;i<n;i++) {
      //      cout<<res<<endl;
      string res2="";
      for (int j=0;j<res.length();j++) {
	if (res[j]=='R')
	  if (i==n-1) {
	    res2+="RS";
	  } else {
	    res2+="SR";
	  }
	if (res[j]=='P') {
	  if (i==n-1) {
	    res2+="PR";
	  } else {
	    res2+="PR";
	  }
	}
	if (res[j]=='S') {
	  res2+="PS";
	}
      }
      res=res2;
    }
    for (int i=0;i<n;i++){
      res2="";
      int M = 1<<i;
      int ant = 1<<(n-i-1);
      for (int j=0;j<ant;j++) {
	int id1=j*2*M;
	int id2=id1+M;
	string a = res.substr(id1,M);
	string b = res.substr(id2,M);

	//	cout<<a<<' ' <<b<<endl;
	if (a<b) {
	  res2+=a;
	  res2+=b;
	} else {
	  res2+=b;
	  res2+=a;
	}
      }
      res=res2;
    }
    cout<<"Case #"<<t<<": "<<res<<endl;
  }
}
