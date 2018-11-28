#include <string>
#include <iostream>
#include <fstream>
#include <cstdlib>
#include "math.h"



using namespace std;


void solve(int i, int a, int b, int k) {
    // limit to below k
    
    int count = 0;
    
    for (int n = 0; n < a; n++)
    {
      for (int m = 0; m < b; m++)
      {
        if (k > (n & m) ) count++; 
      }
    }

    printf("Case #%d: %d\n", i, count);
}

void parse_numbers(string s, int num[], int len){
    string d = " ";
    int n = 0;
    string t = "";
    size_t pos = 0;
    while ( ((pos = s.find(d)) != string::npos) && n < len) {
        t = s.substr(0, pos);
        if (!t.empty())
          num[n++] = atoi(t.c_str());
        s.erase(0, pos + d.length());
      }
      if (n < len) {
        t = s.substr(0, pos);
        if (!t.empty())
          num[n++] = atoi(t.c_str());
      }
}

void file_getline(ifstream& infile){
    string s="";    

    int arr[3];
    
    getline(infile,s);
    int n = atoi(s.c_str());
    
    // iterate cases
    for (int i = 1; i <= n; i++)
    {
      getline(infile,s);
      parse_numbers(s, arr, 3);
      
      solve(i, arr[0], arr[1], arr[2]);
  }

}


int main(int argc, char* argv[]) {
  
  if (argc < 2)
    return -1;
    
  char* filename = argv[1];
    
  ifstream infile;
  infile.open(filename);
  if(infile) {
    file_getline(infile);
    infile.close();
  } 
}

