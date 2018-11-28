#include<iostream>
#include<fstream>
using namespace std;
int T,n,m;
int a[101][101];
int nmax[101];
int mmax[101];
int main(){
  ofstream ofs("b_large_answer.txt");
  cin>>T;
  for(int t=0;t<T;t++){
    cin>>n>>m;
    int flg=1;
    string ans;
    for(int i=0;i<n;i++){
      for(int j=0;j<m;j++){
        cin>>a[i][j];
      }
    }
    for(int i=0;i<n;i++){
      nmax[i]=0;
      for(int j=0;j<m;j++){
        nmax[i]=max(nmax[i],a[i][j]);
      }
    }
    for(int j=0;j<m;j++){
      mmax[j]=0;
      for(int i=0;i<n;i++){
        mmax[j]=max(mmax[j],a[i][j]);
      }
    }
    for(int i=0;i<n;i++){
      for(int j=0;j<m;j++){
        if(nmax[i]!=a[i][j]&&mmax[j]!=a[i][j])flg=0;
      }
    }
    ans=(flg==1)?"YES":"NO";
    ofs<<"Case #"<<t+1<<": "<<ans<<endl;
  }
}
