#include<iostream>
#include<iomanip>
#include<stdio.h>
#include<vector>
#include <limits>
#include <math.h>
#include <map>
using namespace std;

void testcase(int t);



int main(void){
    std::ios_base::sync_with_stdio(false);
    
    std::cout << std::setiosflags(std::ios::fixed) << std::setprecision(7);
    int t;
    cin >> t;
    for (int i=1; i<=t; ++i)testcase(i); 
    return 0;    
}

void testcase(int t){
 cout <<"Case #" << t << ": "; 
 map<int,int> row_map;
 int row;
 cin >> row;
 for(int i=1; i<=4; ++i){
    bool collect = row == i; 
    for(int j=1; j<=4; ++j){
         int a;
         cin >> a;
         if (collect) row_map[a] = 1;
    }
 }
 cin >> row;
 int counter =0;
 int number;
 for(int i=1; i<=4; ++i){
    bool collect = row == i; 
    for(int j=1; j<=4; ++j){
         int a;
         cin >> a;
         if (collect) {
             if (row_map.find(a) != row_map.end()) {
                 counter+=1;
                 number = a;
             }

         }
    }
     }
if (counter == 0) cout << "Volunteer cheated!" << endl;
    else if(counter >1) cout << "Bad magician!" << endl;
    else cout << number << endl;

}

