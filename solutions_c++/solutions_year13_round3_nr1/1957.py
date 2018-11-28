//
//  main.cpp
//  gcj1a
//
//  Created by Julian Wu on 4/26/13.
//  Copyright (c) 2013 Julian Wu. All rights reserved.
//

#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <string>
#include <vector>

using namespace std;

typedef struct section {
  int a, b;
  section(int a, int b){
    this->a = a;
    this->b = b;
  }
}section;

bool isCon(char c){
  return c != 'a' and c != 'e' and c != 'i' and c != 'o' and c != 'u';
}

vector<section> preproc(string str, int n){
  vector<section>* sections = new vector<section>();
  int a = 0, b = 0;
  for (int i = 0; i < str.length() - n + 1; ++i) {
    a = i;
    b = str.length() - (i + n);
    bool con = true;
    for (int j = i; j < i + n; ++j) {
      if ( !isCon(str[j]) ) {
        con = false;
        break;
      }
    }
    if (con) {
      sections->push_back(section(a,b));
    }
  }
  return *sections;
}

long long analysis(vector<section>& secs) {
  int aip = -1;
  long long sum = 0;
  for (int i = 0; i < secs.size(); ++i) {
    sum += (secs[i].a - aip) * (secs[i].b + 1);
    aip = secs[i].a;
  }
  return sum;
}

int main(){
  int cases = 0;
  cin>>cases;
  for (int i = 0; i < cases; ++i) {
    string str;
    int n;
    cin>>str>>n;
    
    vector<section> secs = preproc(str, n);
//    for (int i = 0; i < secs.size(); ++i) {
//      printf("\ta:%d, b:%d\n", secs[i].a, secs[i].b);
//    }
    printf("Case #%d: %lld\n", i+1, analysis(secs));
    
    //    printf("Case #%d: %d\n", i+1, countop(initsize, count, A));
  }
}

