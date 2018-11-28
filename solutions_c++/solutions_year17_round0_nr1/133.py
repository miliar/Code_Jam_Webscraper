#include<iostream>
#include<vector>



using namespace std;


int main(){
  int T; cin>>T;
  for (int tc=1; tc<=T; ++tc){
    string s; cin>>s;
    int k; cin>>k;
    int ans=0;
    for (int i=0; i+k<=s.size(); ++i){
      if (s[i]=='-'){
	++ans;
	for (int j=0; j<k; ++j){
	  if (s[i+j]=='-')
	    s[i+j]='+';
	  else
	    s[i+j]='-';
	}
      }
    }
    bool ja=1;
    for (int i=0; i<s.size(); ++i)
      if (s[i]=='-')
	ja=0;
    cout<<"Case #"<<tc<<": ";
    if (ja)
      cout<<ans<<endl;
    else
      cout<<"IMPOSSIBLE\n";

  }
  return 0;
}
