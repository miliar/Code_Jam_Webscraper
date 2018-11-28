#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <set>
#include <vector>
using namespace std;

int main(){
  int T;
  cin>>T;
  for(int t=0;t<T;t++){
    int first_row,second_row;
    set<int> first_set;
    cin>>first_row;
    for(int i=0;i<16;i++){
      int temp;
      cin>>temp;
      //cerr<<"temp: "<<temp<<endl;
      if(i/4==first_row-1){
        //cerr<<"Interesting: "<<temp<<endl;
        first_set.insert(temp);
      }
    }
    cin>>second_row;
    int found=0;
    int what_found=-1;
    for(int i=0;i<16;i++){
      int temp;
      cin>>temp;
      if(i/4==second_row-1){
        //cerr<<"Checking: "<<temp<<endl;
        if(first_set.count(temp)){
          found++;
          what_found=temp;
        }
      }
    }

    if(found==1){
      cout<<"Case #"<<(t+1)<<": "<<what_found<<endl;
    } else if (found>1){
      cout<<"Case #"<<(t+1)<<": "<<"Bad magician!"<<endl;
    } else {
      cout<<"Case #"<<(t+1)<<": "<<"Volunteer cheated!"<<endl;
    }
  } 
}