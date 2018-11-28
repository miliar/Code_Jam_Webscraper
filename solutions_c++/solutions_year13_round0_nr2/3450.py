#include<iostream>
using namespace std;

int main(){
  int t;
  cin>>t;
  int n,m;
  int des[109][109];
  int cur[109][109];
  for(int z=1;z<=t;z++){
    cin>>n>>m;
    for(int i=0;i<n;i++){
      for(int j=0;j<m;j++){
	cin>>des[i][j];
	cur[i][j]=100;
      }
    }
    cout<<"Case #"<<z<<": ";
    for(int i=0;i<n;i++){
      int mx=-1;
      for(int j=0;j<m;j++){
	if(des[i][j]>mx)
	  mx=des[i][j];
      }
      for(int j=0;j<m;j++){
	if(cur[i][j]>mx)
	  cur[i][j]=mx;
      }
    }
    for(int i=0;i<m;i++){
      int mx=-1;
      for(int j=0;j<n;j++){
	if(des[j][i]>mx)
	  mx=des[j][i];
      }
      for(int j=0;j<n;j++){
	if(cur[j][i]>mx)
	  cur[j][i]=mx;
      }
    }
    bool ok=true;
    for(int i=0;i<n;i++){
      for(int j=0;j<m;j++){
	if(des[i][j]!=cur[i][j])
	  ok=false;
      }
    }
    if(ok)
      cout<<"YES"<<endl;
    else
      cout<<"NO"<<endl;
  }
  return 0;
}
