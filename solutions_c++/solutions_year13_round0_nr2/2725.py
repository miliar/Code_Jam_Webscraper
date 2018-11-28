/*
  with the help of god
*/
#include <algorithm>
#include <numeric>
#include <string>
#include <cstring>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <iterator>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <stack>

using namespace std;

int main(){
  int t;
  cin>>t;
  int cse=1;
  while(t--){
    int n,m;
    cin>>n>>m;
    int a[n][m];
    for(int i=0;i<n;i++) for(int j=0;j<m;j++) cin>>a[i][j];
    int flag=1;
    int dx[4]={1,-1,0,0};
    int dy[4]={0,0,1,-1};
    //cout<<n<<" "<<m<<endl;
    for(int i=0;i<n;i++){
      for(int j=0;j<m;j++){
	if(a[i][j]!=1) continue;
	int m1=100;
	int f1=0,f2=0;
	for(int i1=0;i1<m;i1++){
	  if(a[i][i1]!=1) f1=1;
	}
	for(int i1=0;i1<n;i1++){
	  if(a[i1][j]!=1) f2=1;
	}
	if(f1&f2){
	  flag=0;
	}
	//	cout<<i<<" "<<j<<" "<<f1<<" "<<f2<<" "<<flag<<endl;
      }
    }
    if(flag||n==1||m==1){
      cout<<"Case #"<<cse++<<": "<<"YES"<<endl;
    }
    else{
      cout<<"Case #"<<cse++<<": "<<"NO"<<endl;
    }
  }
  return 0;
}

