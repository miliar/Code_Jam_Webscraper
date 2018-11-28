#include <iostream>
#include <string>
#include <set>

using namespace std;

int main(int argc, char** argv) {
  int ntc;
  cin>>ntc;
  for(int tc=1;tc<=ntc;++tc) {
    set<int> cards;
    set<int> finalcards;
    int choice;
    cin>>choice;
    for(int i=1;i<=4;++i) {
      int n[4];
      cin>>n[0]>>n[1]>>n[2]>>n[3];
      if(i==choice) {
        for(int j=0;j<4;++j) {
          cards.insert(n[j]);
        }
      }
    }
    cin>>choice;
    for(int i=1;i<=4;++i) {
      int n[4];
      cin>>n[0]>>n[1]>>n[2]>>n[3];
      if(i==choice) {
        for(int j=0;j<4;++j) {
          if(cards.find(n[j])!=cards.end()) {
            finalcards.insert(n[j]);
          }
        }
        cout<<"Case #"<<tc<<": ";
        if(finalcards.size()==0) {
          cout<<"Volunteer cheated!"<<endl;
        } else if(finalcards.size()>1) {
          cout<<"Bad magician!"<<endl;
        } else {
          cout<<*(finalcards.begin())<<endl;
        }
      }
    }
  }
}
