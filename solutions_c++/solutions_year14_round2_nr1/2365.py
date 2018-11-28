#include <string>
#include <vector>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <map>
#include <list>
#include <set>
#include <numeric>
#include <queue>
#include <stack>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <cstring>
using namespace std;

int counter = 0;

void runCase() {
    printf("Case #%d: ", ++counter);
    int n; scanf("%d\n", &n);
    
    int moves = 0;
    vector<string> v;
    string s;
    for(int i = 0; i < n; i++) {       
       getline(cin, s);
       v.push_back(s);
    }
    
    
    while(true) {
       int end = 0;
       for(int i = 0; i < n; i++) {
          if(v[i] == "") {
             end++;
          }
       }
       if(end == n) {
          printf("%d\n", moves);
          return;
       } else if(end > 0 ){
          printf("Fegla Won\n");
          return;
       }
       
       char c = v[0].at(0);
    //     printf("%c\n", c);
       int sum = 0;
       int nums[n];
      
       for(int i = 0; i < n; i++) {
          if(v[i][0] != c) {
             printf("Fegla Won\n");
             return;
          }
          int j = v[i].find_first_not_of(c);
          if(j == -1) { 
             j = v[i].length();
             
             v[i] = "";
           } else {
              v[i] = v[i].substr(j, 100);
           }
          sum += j;
      
          nums[i] = j;
       }
       double avg = (double)sum / (double)n;
       
       int k = (int)round(avg);
       
       if(k == 0) {
          printf("Fegla Won\n");
          return;
       }
       for(int i = 0; i < n; i++) {
 //            printf("nums[%d] = %d\n", i,nums[i]);
          int l = nums[i] - k;
          if(l < 0) l *= -1;
          moves += l;
       }
    }
    
   
  
}


void preprocess() {
   
}

int main() {
   preprocess();
    int t; scanf("%d", &t);
    while(t--) {
        runCase();
    }
    return 0;
}

//Sort -        std::sort(ken.begin(), ken.end());
//Double -           printf("%.7f\n", t);
/*
    string s;
    getline(cin, s);
    for(int i = 0; i < s.length(); i++) {
    	char c = s.at(i);

//  n, m, 2 numbers per line
//    int n, m; scanf("%d %d", &n, &m);


// GRID - N x M  
int n, m; scanf("%d %d", &n, &m);
 for (int i=0; i<n; ++i) {
     for (int j=0; j<m; ++j) {
         scanf("%d", &t[i][j]);
     }
 }


*/

