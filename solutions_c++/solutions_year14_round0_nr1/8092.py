#include<iostream>
#include<vector>
#include <algorithm>
#include <fstream>
using namespace std;
int main(){
    int T, answer1, answer2, card;
    vector<int> cards1[4];
    vector<int> cards2[4];
    vector<int> v_intersection;
    ifstream File;
    File.open("A-small-attempt0.in");
    ofstream File2;
    File2.open("A-small-attempt0.out");
    File>>T;
    for(int t = 1; t <= T; t++){ 
       v_intersection.clear();
       File>>answer1;
       answer1-=1;
       for (int i = 0; i < 4; i++){
           cards1[i].clear();
           for(int j = 0; j < 4; j++){
              File>> card;
              cards1[i].push_back(card);
           }
       }
       File>>answer2;
       answer2-=1;
       for (int i = 0; i < 4; i++){
           cards2[i].clear();
           for(int j = 0; j < 4; j++){
              File>> card;
              cards2[i].push_back(card);
           }
       }
       sort(cards1[answer1].begin(), cards1[answer1].end());
       sort(cards2[answer2].begin(), cards2[answer2].end());
       set_intersection(cards1[answer1].begin(), cards1[answer1].end(),cards2[answer2].begin(), cards2[answer2].end(),back_inserter(v_intersection));
       if (v_intersection.size() == 0){
          File2<<"Case #"<<t<<": Volunteer cheated!"<<endl;
       }
       else if (v_intersection.size() == 1){
          File2<<"Case #"<<t<<": "<<v_intersection[0]<<endl;
       }
       else{
          File2<<"Case #"<<t<<": Bad magician!"<<endl;
       }
    }
system("pause");
return 0;    
}
