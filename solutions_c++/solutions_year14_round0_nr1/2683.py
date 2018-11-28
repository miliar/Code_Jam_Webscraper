#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main(){
 ifstream input;
 ofstream output;
 string file;
 cin >> file;
 output.open("output.out");
 input.open(file);
 int n;
 int r1, r2;
 int a1[4][4], a2[4][4];
 
 input >> n;
 for (int k = 0; k < n; k++){

   input >> r1;

   for (int i = 0; i < 4; i++)
     for (int j = 0; j < 4; j++)
       input >> a1[i][j];
   
   input >> r2;

   for (int i = 0; i < 4; i++)
     for (int j = 0; j < 4; j++)
       input >> a2[i][j];
   bool flag = false;
   
   int ans = 0;
   bool cheat = false; 
   r1--;
   r2--;
   for (int i = 0; i < 4; i++){
     for (int j = 0; j < 4; j++){
       if (a1[r1][i] == a2[r2][j]){
	 if (!flag){
	   ans = a1[r1][i];
	   flag = true;
	 } else {
	   cheat =true;
	 }
       }
     }
   }
   output << "Case #" << k+1 << ": ";
   if (flag == false){
 output << "Volunteer cheated!" << endl;

   } else if (cheat == true) {
     output << "Bad magician!" << endl;

       } else {
     output << ans << endl;
   }
 }
 output.close();
 input.close();

 return 0;
}


