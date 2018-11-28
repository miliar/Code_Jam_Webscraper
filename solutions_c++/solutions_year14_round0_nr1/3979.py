#include <iostream>
#include <map>

void getRow(std::map<int, int> &m) {
  int row;
  int tmp;
  std::cin >> row;
  //loop through rows
  for(int i=0; i<4; i++) {
    for(int j=0; j<4; j++) {
      std::cin >> tmp;
      if( (i+1) == row) {
        m[tmp]++;
      }
    }
  }
}

int main() {
  std::map<int, int> m;
  int n, row;
  int ans;
  int ansCnt;

  std::cin >> n;
  for(int i=0; i<n; i++) {
    getRow(m);
    getRow(m);
    
    ansCnt = 0;
    for(auto v : m) {
      if(v.second > 1) {
        ans = v.first;
        ansCnt++;
      }
    }

    std::cout << "Case #" << i+1 << ": ";
    if(ansCnt > 1) {
      std::cout << "Bad magician!\n";
    } else if(ansCnt == 0) {
      std::cout << "Volunteer cheated!\n";
    } else {
      std::cout << ans << std::endl;
    }
    m.clear();
  }


  return 0;
}
