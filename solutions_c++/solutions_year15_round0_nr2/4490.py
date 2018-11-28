#include <iostream>
#include <vector>

using namespace std;

//find the position of the maximum value
int find_max_index(vector<int> array){

  int max = array[0];
  int max_pos = 0;

  for (int i = 1; i < array.size(); i++){

      if (max < array[i]){

          max = array[i];
          max_pos = i;
      }
  }

  return max_pos;

}

//find the max of the maximum value
int find_max(vector<int> array){

  int max = array[0];
  int max_pos = 0;

  for (int i = 1; i < array.size(); i++){

      if (max < array[i]){

          max = array[i];
          max_pos = i;
      }
  }

  return max;

}

int main(int argc, char const *argv[]){

  int T, D;
  vector<int> panc_numbers;
  vector<int> time_for_each_max;

  cin >> T;

  for(int i(0); i < T; i++){

    //read D
    cin >> D;

    //read panc_number vector values
    for (int k(0); k < D; k++){
      int panc_num;
      cin >> panc_num;
      panc_numbers.push_back(panc_num);
    }

    int initial_max = find_max(panc_numbers);

    int min_finish_time = initial_max;

    for(int max_to_reach(1); max_to_reach <= initial_max; max_to_reach++){

      int special_count(0);

      //Do special times!
      vector<int> try_specials(panc_numbers);

      int current_max_index = find_max_index(try_specials);

      //while the max value in the vector is less than max_to reach
      while(try_specials[current_max_index] > max_to_reach){

        //Do one special minute
        try_specials.push_back(try_specials[current_max_index] - max_to_reach);

        try_specials[current_max_index] = max_to_reach;

        //increment the special minute count
        special_count++;

        current_max_index = find_max_index(try_specials);
      }

      //after performing all the special minutes, calculate the time to finish
      int new_finish_time = special_count + max_to_reach;

      //update the minimum finish time
      if(new_finish_time < min_finish_time){
        min_finish_time = new_finish_time;
      }

      try_specials.clear();

    }

    cout << "Case #" << i+1 << ": " << min_finish_time << endl;

    panc_numbers.clear();

  }

  return 0;
}


//printing vector for testing;
        /*

        */
