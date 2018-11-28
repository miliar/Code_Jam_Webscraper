#include <string>
#include <cstring>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath> 

using namespace std;

#define MATRIX_SIZE 4

int main() {

   //num of test cases
   int test_cnt;
   
   cin >> test_cnt;

   for(int idx = 1; idx <= test_cnt; idx++) {
      int first_matrix[MATRIX_SIZE][MATRIX_SIZE];
      int second_matrix[MATRIX_SIZE][MATRIX_SIZE];

      //answer of 1st Q.
      int first_answer;
      cin >> first_answer;
    
      // load matrix of 1st Q.
      for(int i = 0; i < MATRIX_SIZE; i++){
         for(int j = 0; j < MATRIX_SIZE; j++){
            cin >> first_matrix[i][j];
         } 
      }
      
      //answer of 2nd Q.
      int second_answer;
      cin >> second_answer;
    
      // load matrix of 1st Q.
      for(int i = 0; i < MATRIX_SIZE; i++){
         for(int j = 0; j < MATRIX_SIZE; j++){
            cin >> second_matrix[i][j];
         } 
      }

      int cnt = 0;
      int ans = 0;

      //compare
      for(int i = 0; i < MATRIX_SIZE; i++){
         for(int j = 0; j < MATRIX_SIZE; j++){
            if(first_matrix[first_answer-1][i] == second_matrix[second_answer-1][j]){
                cnt++;
                ans = first_matrix[first_answer-1][i];
            }      
         } 
      }
        
      if (cnt == 0){
         cout << "Case #"<<idx <<": Volunteer cheated!\n";   
      }
      else if(cnt == 1){
         cout << "Case #"<<idx << ": " << ans <<"\n";   
      }
      else {
         cout << "Case #"<<idx <<": Bad magician!\n";   
      }
   }

   return 0;
}
