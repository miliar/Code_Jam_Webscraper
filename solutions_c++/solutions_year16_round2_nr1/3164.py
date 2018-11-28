#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <iostream>
#include <string.h>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <fstream>

using namespace std;

void extract(vector<int> &a, string num){
    std::vector<int> b(26, 0);
    for(int k = 0; k < num.size(); k++){
        b[num[k] - 'A']++;
    }
    for(int k = 0; k < a.size(); k++){
        a[k] = a[k] - b[k];
    }
}


bool canextract(vector<int> a, string num){
    std::vector<int> b(26, 0);
    for(int k = 0; k < num.size(); k++){
        b[num[k] - 'A']++;
    }
    for(int k = 0; k < a.size(); k++){
        if(a[k] - b[k] < 0)return false;
    }
    return true;
}

bool check(std::vector<int> a){
  for(int i = 0; i < a.size(); i++){
      if(a[i] != 0)return false;
  }
  return true;
}

int main(){
   ifstream in("/Users/tech8/Desktop/Ainput.txt");
   ofstream out("/Users/tech8/Desktop/Aoutput.txt");
   long long int test_case;
   in >> test_case;
   string arr[10] = {"SIX", "ZERO", "TWO", "FOUR", "THREE", "ONE", "EIGHT", "FIVE", "SEVEN", "NINE" };
   int code[10] = {6, 0, 2, 4, 3, 1, 8, 5, 7, 9};

     for(long long int s = 0; s < test_case; s++) {
        string number;
        in >> number;
        std::vector<int> a(26, 0);
        for(int k = 0; k < number.size(); k++){
            a[number[k] - 'A']++;
        }
        int i = 0;
        vector<int> num;

        while(true){
          if(canextract(a, arr[i])){
              extract(a, arr[i]);
              num.push_back(code[i]);
              if(check(a))break;
          }else{
            i++;
          }
          if(i == 10)break;
        }
        sort(num.begin(), num.end());
        out << "Case #" << s + 1 << ": ";
        for(int k = 0; k < num.size(); k++){
          out << num[k];
        }
        out << endl;
    }
}

