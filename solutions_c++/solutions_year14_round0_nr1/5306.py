#include <iostream>
using namespace std;

#define Rep(i,n) for(int i=0;i<(n);++i)

int main() {
  int ntest;
  int z[20];
  cin >> ntest;
  Rep(t,ntest){
    int r;
    Rep(i,20)z[i]=0;
    Rep(kk,2){
    cin>>r;
    Rep(i,4)Rep(j,4){
      int x;
      cin>>x;
      if(i+1==r)z[x]++;
    }
    }
    int total=0,res=-1;
    Rep(i,20)if(z[i]==2)++total, res=i;
    cout<<"Case #"<<t+1<<": ";
    if (total==0) cout<<"Volunteer cheated!";
    else if (total>1) cout<<"Bad magician!";
    else cout<<res;
    cout<<endl;
  }
  return 0;
}
