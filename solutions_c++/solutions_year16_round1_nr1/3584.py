#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;



int main(){
  //string input;
  //cin >>input;
  //cout <<input<<endl;

  int total_tests;
  cin >> total_tests;
  //cout <<total_tests<<endl;
  for(int j = 1; j <= total_tests; j++){
    string str;
    cin >>str;
    string final = "";
    for(size_t i = 0; i < str.size(); i++){
      char temp = str[i];
      if(i == 0) final += temp;
      else{
        if(final[0] > temp){
          final = final + temp;
        }
        else final = temp + final;
      }

    }

    //cout<<final<<endl;
    cout<<"Case #"<<j<<": "<<final<<endl;
  }


  return 0;
}