#include <iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<queue>
#include<map>

using namespace std;
int main(int argc, char **argv) {
  int T = 0;
  //freopen("testcaseC.in", "r", stdin);
  cin >> T;
  
  for (int t = 0; t < T; t++)
  {
    cout<<"Case #"<<t +1 <<": ";
    int A=0,B=0,K=0,count=0;
    cin>>A>>B>>K;
    for(int i=0;i<A;i++)
    {
      for(int j=0;j<B;j++)
      {
	if((i&j)<K)
	  count++;
      }
    }
    cout<<count<<endl;
    
  }
  return 0;
}
