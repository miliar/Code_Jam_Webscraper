#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char const *argv[]) {

  int T, N;
  vector<int> shrooms;

  cin >> T;

  for (int i(0); i < T;i++){

    cin >> N;


    for(int k(0); k < N; k++){
      int temp;
      cin >> temp;
      shrooms.push_back(temp);
    }

    int eaten_1 = 0;
    //method 1
    for(int k(0); k < N-1; k++){
      if(shrooms[k] > shrooms[k+1]){
        eaten_1 += shrooms[k] - shrooms[k+1];
      }
    }

    int eaten_2 = 0;

    int max_dif = 0;

    for(int k(0); k < N-1; k++){

      if(shrooms[k] > shrooms[k+1]){
        int local_diff = shrooms[k] - shrooms[k+1];
        if(local_diff > max_dif)
          max_dif = local_diff;
      }
    }

    for(int k(0); k < N-1; k++){

      if(shrooms[k] >= max_dif){
        eaten_2 += max_dif;
      }
      else{
        eaten_2 += shrooms[k];
      }
    }


    cout << "Case #" << i+1 << ": " << eaten_1  << " "<< eaten_2 << endl;
    shrooms.clear();

  }

  return 0;
}
