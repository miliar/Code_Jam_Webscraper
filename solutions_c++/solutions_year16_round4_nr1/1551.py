#include <stdio.h>
#include <string.h>
#include <iostream>
#include <vector>
#include <utility>
#include <unordered_map>
#include <fstream>
#include <map>
#include <set>

using namespace std;

typedef long long ll;

int col[13][3];

string ans(int n, int r, int p, int s) {
  if (max(r,max(p,s))-min(r,min(p,s)) != 1) {
    return "IMPOSSIBLE";
  }
  
  if (n == 1){
    if (r == 1 && p == 1 && s == 0) return "PR";
    if (r == 1 && p == 0 && s == 1) return "RS";
    if (r == 0 && p == 1 && s == 1) return "PS";
    
  } else if (n == 2) {
    if (r == 2 && p == 1 && s == 1) return "PRRS";
    if (r == 1 && p == 2 && s == 1) return "PRPS";
    if (r == 1 && p == 1 && s == 2) return "PSRS";
    
  } else if (n == 3) {
    if (r == 2 && p == 3 && s == 3) return "PRPSPSRS";
    if (r == 3 && p == 2 && s == 3) return "PRRSPSRS";
    if (r == 3 && p == 3 && s == 2) return "PRPSPRRS";
  }
  
  return "IMPOSSIBLE";
}

int main() {
  ifstream myfile;
  myfile.open ("awesome.in");
  ofstream a_file ( "example.out");
  
  col[0][0] = 1; col[0][1] = 0; col[0][2] = 0;
  for (int i=1; i<13; i++) {
    col[i][0] = col[i-1][0] + col[i-1][1];
    col[i][1] = col[i-1][1] + col[i-1][2];
    col[i][2] = col[i-1][0] + col[i-1][2];
  }
  
  int t; myfile >> t;
  
  for (int i=0; i<t; i++) {
    int n, r, p, s; myfile >> n >> r >> p >> s;
    a_file << "Case #" << i+1 << ": " << ans(n,r,p,s) << endl;
    
  }
  
  a_file.close();
}