#include <iostream>
#include <string>
using namespace std;

int first_number[4],second_number[4];
int mycount;
int card;
int row;

void solve(){
  for (int i=0; i<4; ++i){
    for (int j=0; j<4; ++j){
      if (first_number[i]==second_number[j]){
        mycount+=1;
        card = first_number[i];
      }
    }
  }
  if (mycount==1) cout<<card;
  else if (mycount>1) cout<<"Bad magician!";
  else cout<<"Volunteer cheated!";
}
int main(){
  int tc;
  cin>>tc;
  for (int i=0; i<tc; ++i){
    cout<<"Case #"<<i+1<<": ";
    mycount =0;
    cin>>row;
    for (int j=0; j<4; ++j){
      for (int k=0; k<4; ++k ){
        if (j+1==row)
          cin>>first_number[k];
        else
          cin>>card;
      }
    }
    cin>>row;
    for (int j=0; j<4; ++j){
      for (int k=0; k<4; ++k ){
        if (j+1==row)
          cin>>second_number[k];
        else
          cin>>card;
      }
    }
    solve();
    cout<<endl;
  }
}
