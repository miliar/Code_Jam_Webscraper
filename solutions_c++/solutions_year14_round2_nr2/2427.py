# include <cstdio>
# include <cstring>
# include <cmath>
# include <cstdlib>
# include <iostream>
# include <vector>
# include <algorithm>
# include <queue>
# include <set>
# include <map>

using namespace std;

int main()
{
  int T;
  scanf("%d",&T);
  for(int t=1;t<=T;t++)
  {
	int A,B,K;
	int count = 0;
	cin>>A>>B>>K;
	for(int i=0;i<A;i++){
	 for(int j=0;j<B;j++){
	  
		int result = i&j;
		if(result < K) {count++; //cout<<"i = "<<i<<" j = "<<j<<endl;
		}
	  
	 }
	}
	cout<<"Case #"<<t<<": ";
  	cout<<count<<endl;
  }
  return 0;
}

