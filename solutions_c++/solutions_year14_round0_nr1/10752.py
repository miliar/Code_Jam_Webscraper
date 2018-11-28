#include<iostream>
#include<map>
using namespace std;

int main() {
  int T;
  cin>>T;
  int ii;
  for(ii=1;ii<=T;ii++) {
    cout<<"Case #"<<ii<<": ";
  map<int, int> tutu;
  int a,b,i,j,count=0,ans,temp;
  cin>>a;
  for(i=0;i<4;i++) {
    for(j=0;j<4;j++) {
    cin>>temp;
    if(i+1 == a){
      tutu[temp]=1;
    }
    }
  }
  cin>>b;
  for(i=0;i<4;i++) {
    for(j=0;j<4;j++) {
      cin>>temp;
      if(i+1 == b) {
        if(tutu.count(temp)){
          count++;
          ans=temp;
        }
      }
    }
  }
  if(count==1) {
    cout<<ans<<"\n";
  } else if(count==0) {
    cout<<"Volunteer cheated!\n";
  }
  else cout<<"Bad magician!\n";
}
return 0;
}
