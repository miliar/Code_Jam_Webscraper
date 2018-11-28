#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <string>
#include <cstring>
typedef long long ll;
using namespace std;
int T;
int main(){
  cin>>T;
  for(int t=0;t<T;t++){
    string s;
    cin>>s;
    ll ans=0;
    int st=0,en=s.size()-1;
    if(st==en){
      ans=(s[0]=='-');
    }
    while(en!=st){
      //for(int i=st;i<=en;i++)
      //cerr<<s[i];
      //cerr<<endl;
      while(s[en]=='+')
	en--;
      if(en==-1){
	//ans=0;
	en=0;
	break;
      }
      if(s[st]=='-'){
	ans++;
	for(int i=st;i<=en/2;i++){
	  char tmp=s[i];
	  s[i]=s[en-i];
	  s[en-i]=tmp;
	}
	for(int i=st;i<=en;i++){
	  if(s[i]=='-')
	    s[i]='+';
	  else
	    s[i]='-';
	}
	
      }
      else if(s[st]=='+'){
	int stt=st;
	while(s[stt]=='+')
	  stt++;
	stt--;
	ans++;
	for(int i=st;i<=stt/2;i++){
	  char tmp=s[i];
	  s[i]=s[stt-i];
	  s[stt-i]=tmp;
	}
	for(int i=st;i<=stt;i++){
	  if(s[i]=='-')
	    s[i]='+';
	  else
	    s[i]='-';
	}
        
      }
    }
    cout<<"Case #"<<t+1<<": "<<ans<<endl;
  }
  return 0;
}
