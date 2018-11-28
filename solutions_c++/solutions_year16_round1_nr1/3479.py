#include <iostream>
#include <cstdio>
#include <string>

using namespace std;
int main(){
   int cases;
   cin >> cases;
   for(int blah = 0; blah < cases; ++blah){
      string input;
      cin >> input;
      string answer = "";
      char pivot = input[0];
      for(string::iterator it = input.begin(); it != input.end(); ++it){
         if(*it >= pivot){
            string temp = "";
            temp.push_back(*it);// SKETCHY AF
            answer.insert(0, temp);
            pivot = *it;
         }
         else {
            answer.push_back(*it);
         }
      }
      cout << "Case #" << blah+1<<": "<< answer << endl; 
   }
   
   return 0;
}
