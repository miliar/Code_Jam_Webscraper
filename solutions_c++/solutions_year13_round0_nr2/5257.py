#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
#include <map>
using namespace std;

int main()
{

     freopen("B-large.in","r",stdin);
     freopen("B.out","w",stdout);
      int T,N,M;
      bool flag,row,col;
	  vector<vector<int> > lawn;
      cin>>T;
      for(int cas = 1 ;cas <= T;++cas)
      {
		  flag=true;
		  cin>>N>>M;
		  lawn.resize(N);
		  for(int i=0;i<N;i++){
			  lawn[i].resize(M);
		  }
		  for(int i=0;i<N;i++){
			  for(int j=0;j<M;j++){
				  cin>>lawn[i][j];
			  }
		  }
		  for(int i=0;i<N;i++){
			  for(int j=0;j<M;j++){
				  row=true;
				  col=true;
				  for(int k=0;k<M;k++){
					  if(lawn[i][j]<lawn[i][k]){
						  row=false;
						  break;
					  }
				  }
				  for(int k=0;k<N;k++){
					  if(lawn[i][j]<lawn[k][j]){
						  col=false;
						  break;
					  }
				  }
				  if(!row && !col){
					  flag=false;
					  break;
				  }
			  }
			  if(!flag) break;
		  }
		  if(flag) cout<<"Case #"<<cas<<": YES"<<endl;
		  else cout<<"Case #"<<cas<<": NO"<<endl;
      }
      return 0;
}
