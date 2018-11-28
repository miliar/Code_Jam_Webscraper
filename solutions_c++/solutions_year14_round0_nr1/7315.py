#include <iostream>
#include <stdio.h>
#include <vector>
#include <fstream>

     
 using namespace std;
     
 int main(){
   ifstream ifs("test.txt");
   ofstream ofs("out.txt");
   int t,i;
   ifs >> t;
     
   for(i=1;i<=t;i++){
     int x,y,xboard[4][4],yboard[4][4],j,k;
     vector <int> ans;
     ifs  >> x;
     for(j=0;j<4;j++){
       for(k=0;k<4;k++){
         ifs  >> xboard[j][k];
       }
     }
     ifs  >> y;
     for(j=0;j<4;j++){
       for(k=0;k<4;k++){
         ifs  >> yboard[j][k];
       }
      }
     
     for(j=0;j<4;j++){
       for(k=0;k<4;k++){
         if(xboard[x-1][j] == yboard[y-1][k]) ans.push_back(xboard[x-1][j]);
       }
     }
     
     if(ans.size() == 0){
       ofs << "Case #" << i << ": Volunteer cheated!" << endl;
     }
     if(ans.size() > 1){
       ofs << "Case #" << i << ": Bad magician!" << endl;
     }
     if(ans.size() == 1){
       ofs << "Case #" << i << ": " << ans[0] << endl;
     }
    }
     
    return 0;
     
 }
