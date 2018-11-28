#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<numeric>
#include<cstring>
#include<iterator>
#include<set>

using namespace std;

bool b[130];

bool isValid(string s) {
  memset(b,0,sizeof(bool)*130);
  //  copy(b,b+130,ostream_iterator<bool>(cerr,"\n"));
  //  cerr<<"s: "<<s<<endl;
  b[s[0]]=true;
  for(int i=1;i<s.length();++i) {
    if(s[i]!=s[i-1] && b[s[i]])
      return false;
    b[s[i]]=true;
  }

  //  cerr<<"returning true\n";
  return true;
}

int main() {
  freopen("data.txt","r",stdin);
  freopen("output.txt","w",stdout);

  int T;
  cin>>T;
  for(int t=1;t<=T;++t) {
    int n;

    cin>>n;
    vector<string> v(n);
    for(int i=0;i<n;++i) {
      cin>>v[i];
    }
    sort(v.begin(),v.end());
    set<string> se(v.begin(),v.end());
    long a=v.size()-se.size();
    a*=2;
    long ans=0;
    do {
      string tt="";
      for(int j=0;j<v.size();++j)
	tt+=v[j];

      if(isValid(tt))
	ans++;
    } while(next_permutation(v.begin(),v.end()));
    if(a)
      ans*=a;
    printf("Case #%d: %ld\n",t,ans);
  }
  return 0;
}
