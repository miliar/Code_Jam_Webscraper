#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>


using namespace std;

int T,N;
string S;

bool isCons(char c){
  if(c=='a' || c=='e' || c=='i' || c=='o' || c=='u')
    return false;

  return true;
}

bool isGood(int p, int q){
  bool good = false;
  int start = -1;
  for(int i=p; i<=q; i++){
    if(isCons(S[i])){
      if(start==-1)
	start = i;
      
      if(i-start == N-1)
	good = true;
    }
    else{
      start = -1;
    }
  }
  return good;
}

int main(){
  cin>>T;
  
  long long int count;
  for(int i=0; i<T; i++){
    cin>>S>>N;
    int len = S.length();
    count = 0;
    for(int j=0; j<len; j++){
      for(int k=j; k<len; k++){
	if(isGood(j,k))
	  count++;
      }
    }

    printf("Case #%d: %lld\n",i+1,count);

    //cout<<count<<endl;
  }
  return 0;
}
