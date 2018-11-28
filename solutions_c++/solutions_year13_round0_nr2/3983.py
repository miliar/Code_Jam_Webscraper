// -*- compile-command:"cd c:/MinGW/bin && g++.exe -std=c++11 c:/Users/Josef/Desktop/gcj/lawn.cc -o c:/Users/Josef/Desktop/gcj/lawnometer && c:/Users/Josef/Desktop/gcj/lawnometer < c:/Users/Josef/Desktop/gcj/lawn.in" -*-
#include <iostream>
#include <algorithm>
#include <array>

int main() {
  int cases; std::cin >> cases;
  for (int case_=1; case_<=cases; ++case_) {
    int field[100][100];
    bool x_closed[100] = {false};
    bool y_closed[100] = {false};
      
    int n, m; std::cin >> n >> m;

    for (int i=0; i<n; ++i)
      for (int j=0; j<m; ++j)
	std::cin >> field[i][j];
    
    for (int cut=100; cut > 0; --cut) {
      std::vector<int> closelist_x;
      std::vector<int> closelist_y;

      for (int i=0; i<n; ++i) {
	for (int j=0; j<m; ++j) {
	  if (field[i][j] == cut) {
	    if (x_closed[i] && y_closed[j])
	      goto impossible;
	    closelist_x.push_back(i);
	    closelist_y.push_back(j);
	  }
	}
      }

      for (int x : closelist_x)
	x_closed[x] = true;
      for (int y : closelist_y)
	y_closed[y] = true;
    }
    
    std::cout << "Case #" << case_ << ": YES\n";
    continue;
  impossible:
    std::cout << "Case #" << case_ << ": NO\n";
  }
}
