#include <iostream>
#include <string>
#include <vector>
#include <string>
#include <limits.h>
#include <fstream>
#include <unordered_map>
using namespace std;



int getMin(vector<int>& vec) {
    int min = INT_MAX;
    for(int i = 0; i< vec.size(); ++i) {
        if(vec[i] < min) 
            min = vec[i];
    }
    return min;
}

int getMax(vector<int>& vec) {
    int max = INT_MIN;
    for(int i = 0; i< vec.size(); ++i) {
        if(vec[i] > max) 
            max = vec[i];
    }
    return max;
}
void setMaxHalf(vector<int>& vec) {
    int max = INT_MIN;
    int max_index = 0;
    for(int i = 0; i< vec.size(); ++i) {
        if(vec[i] > max){ 
            max = vec[i];
            max_index = i;
        }
    }
    vec[max_index] = max/2;
    vec.push_back(max-max/2);
}


vector<int> setNewPlate(vector<int>& vec, int num) {
    int max = INT_MIN;
    int max_index = 0;
    vector<int> out_vec = vec;
    for(int i = 0; i< out_vec.size(); ++i) {
        if(vec[i] > max){ 
            max = out_vec[i];
            max_index = i;
        }
    }
    out_vec[max_index] = num;
    out_vec.push_back(max-num);
    return out_vec;
}
int GetPlateNum(vector<int>& plate_vec,int cur_step) {
    //end condition
    if(getMax(plate_vec) == 2){
       return 2;
    }
    if(getMax(plate_vec) == 1){
        return 1;
    }

    //just eat
    int plate_max = getMax(plate_vec);

    int cur_min = plate_max;
    if(cur_step >= cur_min) return cur_min;
    for(int i = 1; i <= plate_max/2; ++i){
        //i and plate_max-i
        vector<int> newplate = setNewPlate(plate_vec, i);
        cur_min = min(cur_min, 1 + GetPlateNum(newplate,cur_step + 1));
        newplate.clear();
    }
    return cur_min;

    //share
   // setMaxHalf(plate_vec);

   // return min(plate_max, 1 + GetPlateNum(plate_vec));
    //two possibility
    //give to others, get max, set to 1
    // vector<int> maxHalf = setMaxHalf(plate_vec);
    // GetPlateNum(maxHalf, step_need + 1, cur_min);
    
    // //eat for the minute
    // vector<int> minuOne = minusOne(plate_vec);
    // GetPlateNum(minuOne, step_need+1, cur_min);
}
int main()
{
  ifstream fin("B-small-attempt2.in");
  ofstream fout("out-B-small-brute.txt");
  int testNum;
  fin >> testNum;
  vector<int> plate_vec;
  for (int i = 1; i<= testNum; ++i) {
    cout<<i<<endl;
    int non_emp;
    int temp_plt;
    fin >> non_emp;
    for (int j = 1; j <= non_emp; ++j) {
        fin >> temp_plt;
        plate_vec.push_back(temp_plt);
    }
    //plate_vec
    int cur_min = INT_MAX;
    cur_min = GetPlateNum(plate_vec, 0);
    fout << "Case #" << i<<": "<<cur_min <<endl;
    plate_vec.clear();
  }

}
