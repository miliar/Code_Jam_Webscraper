#include <iostream>
#include <string>
#include <vector>
using namespace std;

int n,m,t,mat[110][110];

int main(){
  cin>>t;
  for(int test=1;test<=t;test++){
    cin>>n>>m;
    for(int i=0;i<n;i++)
      for(int j=0;j<m;j++)
	cin>>mat[i][j];
    bool doable = 1;
    for(int i=0;i<n;i++)
      for(int j=0;j<m;j++){
	bool hor = 1, ver = 1;
	for(int q=-101;q<=101;q++) {
	  if(q+i>=0 && q+i<n && mat[q+i][j]>mat[i][j]) hor = 0;
	  if(q+j>=0 && q+j<m && mat[i][q+j]>mat[i][j]) ver = 0;
	}
	if(!hor && !ver)  doable = 0;
      }
    if(doable)
      cout<<"Case #"<<test<<": YES\n";
    else
      cout<<"Case #"<<test<<": NO\n";
  }
  return 0;
}
