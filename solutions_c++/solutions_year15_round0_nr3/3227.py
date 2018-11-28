#include <iostream>
#include <string>
#include <map>

using namespace std;

string mul(string a,char bb, map<string,string> &tab) {
  string b(1,bb);
  string sign;
  if (a[0] == '-') {sign="-";a=a.substr(1);}
  if (b[0] == '-') {
    if (sign == "-") sign=""; else sign="-";
    b=b.substr(1);
  }
  string temp=tab[a+b];
  if (temp[0]=='-') {
    if (sign=="-") sign=""; else sign="-";
    temp=temp.substr(1);
  }
  return sign+temp;
}

int main() {
  map<string,string> tab;
  tab["11"]="1";tab["1i"]="i";tab["1j"]="j";tab["1k"]="k";
  tab["i1"]="i";tab["ii"]="-1";tab["ij"]="k";tab["ik"]="-j";
  tab["j1"]="j";tab["ji"]="-k";tab["jj"]="-1";tab["jk"]="i";
  tab["k1"]="k";tab["ki"]="j";tab["kj"]="-i";tab["kk"]="-1";

  int T;cin>>T;
  for(int t=1;t<=T;++t){
    cout<<"Case #"<<t<<": ";
    long long L,X;cin>>L>>X;
    string s,ss;
    cin>>s;
    for (long long i=0;i<X;++i) ss+=s;
    string prod="1";
    for (int i=0;i<ss.size();++i) prod=mul(prod,ss[i],tab);
    if (prod!="-1") {
      cout<<"NO"<<endl;
      continue;
    }
    string ans="NO";
    string left="1",mid="1",right="1";
    for (int i=0;i<ss.size()&&ans!="YES";++i) {
      left = mul(left,ss[i],tab);
      if (left!="i") continue;
      for (int j=i+1;j<ss.size();++j) {
        mid = mul(mid,ss[j],tab);
        if (mid=="j") {ans="YES";break;;}
      }
    }
    cout<<ans<<endl;
  }
  return 0;
}
