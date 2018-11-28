#include<bits/stdc++.h>
using namespace std;

int main()
{
  int t,n;
  set<int> s;

  cin>>t;
  for(int i=1;i<=t;i++){
    cin>>n;
    s.clear();

    if(n==0){
      printf("Case #%d: INSOMNIA\n",i);
      continue;
    }
    for(int k=1;;k++){
      int m=k*n,a=10,b;
      while(1){
	b=m%a;
	s.insert(b);
	m/=a;
	if(m==0)break;
      }
      if(s.size()==10){
	printf("Case #%d: %d\n",i,k*n);
	break;
      }
    }
  }
  return 0;
}
