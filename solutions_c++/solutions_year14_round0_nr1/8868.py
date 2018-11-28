#include <iostream>
#include <fstream>
#include <vector>

#define COL_SIZE 4

using namespace std;

int find_magician_number(vector<vector<int> >& first, vector<vector<int> >& second, int row_first, int row_second)
{
  int chosen_number = 0; 
  int n_chosen_numbers = 0;

  for (int i=0; i<COL_SIZE; i++) {
    for (int j=0; j<COL_SIZE; j++) {
      if(first[row_first][i] == second[row_second][j]) {
        chosen_number = first[row_first][i];
        n_chosen_numbers++;
      }
    }
  }

  if(n_chosen_numbers == 0) {
    return -1;
  } else if(n_chosen_numbers > 1) {
    return -2;
  }

  return chosen_number;
}

int x_main(int case_n, vector<vector<int> >& first, vector<vector<int> >& second, int row_first, int row_second)
{
  int val = find_magician_number(first, second, row_first, row_second);

  if(val == -1) {
    cout << "Case #" << case_n << ": Volunteer cheated!";
  }
  else if(val == -2) {
    cout << "Case #" << case_n << ": Bad magician!";
  } else {
    cout << "Case #" << case_n << ": " << val;
  }

  cout << endl;
}


int main()
{
  int n_cases; 

  ifstream file("A-small-attempt1.in.txt", ios::in);
  file >> n_cases;
  
  for (int case_no=1; case_no <= n_cases; case_no++) {
    vector<vector<int> > first;
    vector<vector<int> > second;
    int row_first;
    int row_second;

    file >> row_first;
    for (int i=0; i<COL_SIZE; i++) {
      vector<int> tmp;
      int tmp_val;
      for (int j=0; j<COL_SIZE; j++) {
        file >> tmp_val;
        tmp.push_back(tmp_val);
      }
      first.push_back(tmp);
    }
    file >> row_second;
    for (int i=0; i<COL_SIZE; i++) {
      vector<int> tmp;
      int tmp_val;
      for (int j=0; j<COL_SIZE; j++) {
        file >> tmp_val;
        tmp.push_back(tmp_val);
      }
      second.push_back(tmp);
    }

    x_main(case_no, first, second, row_first-1, row_second-1);
  }
}

