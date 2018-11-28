#include <iostream>
#include <string>
#include <sstream>

using namespace std;

int to_int(char ch){
  return ch - '0';
}

int standing_ovation(int s_max, const string& test_string){

  int people_at_s_i = to_int(test_string[0]);
  int total_people_standing_so_far = people_at_s_i;
  int people_needed = 0;
  int total_people_needed = people_needed;

  int i;

  for(i = 1;i <= s_max;i++){
    //cout << (i-1) << ":" << total_people_standing_so_far <<":" << total_people_needed << " ";

    people_at_s_i = to_int(test_string[i]);
    if(total_people_standing_so_far < i){
      people_needed = ( i - total_people_standing_so_far);
      total_people_needed += people_needed;
      total_people_standing_so_far += people_needed;
    }

    total_people_standing_so_far += people_at_s_i;
  }

  //cout << (i-1) << ":" << total_people_standing_so_far << ":" << total_people_needed << " ";

  return total_people_needed;
}

int main(){
  int test_cases;

  string test_line_input;
  getline(cin, test_line_input);

  istringstream iss(test_line_input);
  iss >> test_cases;

  int s_max = 0;
  string test_string;

  for(int i = 0; i < test_cases;i++){
    getline(cin, test_line_input);

    istringstream iss(test_line_input);
    iss >> s_max >> test_string;
    //cout << s_max << " " << test_string << endl;
    
    cout << "Case #" << (i+1) << ": " << standing_ovation(s_max, test_string) << endl; 

  }

  return 0;
}
