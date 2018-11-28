//
//  main.cpp
//  COdeJam
//
//  Created by Hanefi Önaldı on 11/04/15.
//  Copyright (c) 2015 hanefi. All rights reserved.
//

#include <iostream>
#include <fstream>
using namespace std;
//#define fin cin

int main(int argc, const char * argv[]) {
  
  ifstream fin("input.txt");
  ofstream fout("output.txt");
  
  int T;
  fin>>T;
  
  for (int t=1; t<=T; t++) {
    int Smax;
    char S[1111];
    fin>>Smax>>S;
    
    int total=0;
    int ans=0;
    for (int i=0; i<=Smax; i++) {
      if(i>total){
        ans+=i-total;
        total=i;
      }
      total+=S[i]-'0';
    }
    
    fout<<"Case #"<<t<<": "<<ans<<endl;
  }
  
    return 0;
}
