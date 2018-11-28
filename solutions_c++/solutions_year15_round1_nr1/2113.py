#include <vector>
#include <iostream>
#include <functional>
#include <string>
#include <fstream>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <cstdlib>

using namespace std;
int mushroom1Method(string h){
  vector<int> plate_states;
  stringstream stream(h);
  int pieces_eaten = 0;
while(1) {
   int n = -1;
   stream >> n;
   if(!stream || n == -1)
      break;
   plate_states.push_back(n);
}

 int previous_state = 0;
 int delta  = 0;
 for(int i = 0; i < plate_states.size(); i++){
   if(i != 0){
    delta = previous_state - plate_states[i] ;
   }
   if(delta > 0){
     pieces_eaten += delta;
   }
   previous_state = plate_states[i];
 }
 return pieces_eaten;
}



int mushroom2Method(string h){
  vector<int> plate_states;
  stringstream stream(h);
  int pieces_eaten = 0;

while(1) {
   int n = -1;
   stream >> n;
   if(!stream || n == -1)
      break;
   plate_states.push_back(n);
}

 int previous_state = 0;
 int always_eating = 0;
 int delta  = 0;
 for(int i = 0; i < plate_states.size(); i++)
 {
   if(i != 0){
    delta = previous_state - plate_states[i] ;
   }
   if(delta > always_eating){
     always_eating = delta;
   }
   previous_state = plate_states[i];
 }
 for(int i = 0; i < plate_states.size() - 1; i++)
 {
   if(plate_states[i] < always_eating){
     pieces_eaten += plate_states[i];
   }
   else{
     pieces_eaten += always_eating;
   }
 }

 return pieces_eaten;
}
int main(int argc, char *argv[])
{
  string line, strkji;
  int T, L, X;
  int case_no = 1;
  ifstream inputf ("input-large.txt");
  if (inputf.is_open())
    {
      //test numbers
      getline (inputf,line);
      T = stoi(line);
      for (int i = 0; i < T; ++i){
        getline (inputf, line);
        istringstream iss(line);
        iss >> L;

        getline(inputf, strkji);


        int sol1 = mushroom1Method(strkji);
        int sol2 = mushroom2Method(strkji);
        cout << "Case #" << case_no << ": " << sol1 << " " << sol2 << endl;


        ++case_no;
      }
    }
  inputf.close();

  return 1;
}
