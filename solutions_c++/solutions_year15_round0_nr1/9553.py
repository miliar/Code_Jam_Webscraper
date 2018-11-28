#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;


int main(){
  int T,N;
  char s[10000];
  cin>>T;
  for(int t=1;t<=T;t++)
    {
      cin>>N>>s;
      int toadd=0, standing=0;
      for(int i=0;i<=N;i++){
	s[i]-='0';
	if(s[i]>0 && standing<i){
	  toadd+=i-standing;
	  standing=i;}
	standing+=s[i];
      }
      printf("Case #%d: %d\n",t,toadd);
    }
  return 0;
}
