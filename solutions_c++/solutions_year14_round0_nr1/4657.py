#include<iostream>
#include<vector>

using namespace std;
#define sz 4
int main(){
  int t=0,T;
  cin>>T;
  while(t<T){
    int n1,n2,val,flag=0;
    int v1[sz][sz], v2[sz][sz];
    cin>>n1;n1--;
    for(int i=0;i<sz;i++)for(int j=0;j<sz;j++) cin>>v1[i][j];
    cin>>n2;n2--;
    for(int i=0;i<sz;i++)for(int j=0;j<sz;j++) cin>>v2[i][j];
    for(int i=0;i<sz;i++)for(int j=0;j<sz;j++) {
      if(v1[n1][i]==v2[n2][j]){
        flag++;
        val=v1[n1][i];
      }
    }
    cout<<"Case #"<<t+1<<": ";
    if(flag==1)
      cout<<val<<endl;
    else if(flag==0)
      cout<<"Volunteer cheated!\n";
    else
      cout<<"Bad magician!\n";
    t++;
  }
  return 0;
}
