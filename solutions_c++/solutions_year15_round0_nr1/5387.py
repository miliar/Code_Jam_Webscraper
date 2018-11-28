#include <iostream>
#include <string>

using namespace std;


int main(int argc, char const *argv[]) {


  int T;
  int sMax;
  string shy_dist;

  cin >> T;

  for(int i(0); i < T; i++){

      int person_sum = 0;
      int friends = 0;
      cin >> sMax;
      cin >> shy_dist;

      for(int s(0); s < sMax+1; s++){

          if(person_sum >= s){
            person_sum += shy_dist[s] - '0';
          }
          else{

             int dif = s - person_sum;
             friends += dif;
             person_sum += shy_dist[s] - '0' + dif;
          }
      }
      cout << "Case #" << i+1 << ": " << friends << endl;

  }


  return 0;
}
