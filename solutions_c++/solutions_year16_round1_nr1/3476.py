#include<bits/stdc++.h>

using namespace std;

int main(){

  int T, cases = 1;
  cin>>T;
  while(T--){

    string input = "";
    list<char> output;
    cin>>input;
    output.push_back(input[0]);

    for(int i = 1; i < input.size(); i++){
      if(output.front() <= input[i]){
	output.push_front(input[i]);
      }
      else
	output.push_back(input[i]);
    }

    cout<<"Case #"<<cases++<<": ";
    list<char>::iterator it;
    for(it = output.begin(); it != output.end(); it++){
      cout<<*it;
    }
    cout<<endl;
    
  } 

  return 0;
}
