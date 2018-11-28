#include<vector>
#include<iostream>
#include<fstream>


int main(int argc, char* argv[]) {
  if (argc < 2) {
    return 0;
  }
  std::ifstream f(argv[1]);
  std::ofstream g(argv[2]);
  int t;
  f >> t;
  int cards1[4][4], cards2[4][4];
  int ans1, ans2;
  for (int i = 0; i < t; i++) {
    f >> ans1;
    f >> cards1[0][0] >> cards1[0][1] >> cards1[0][2] >> cards1[0][3] >>
        cards1[1][0] >> cards1[1][1] >> cards1[1][2] >> cards1[1][3] >>
        cards1[2][0] >> cards1[2][1] >> cards1[2][2] >> cards1[2][3] >>
        cards1[3][0] >> cards1[3][1] >> cards1[3][2] >> cards1[3][3];
    f >> ans2;
    f >> cards2[0][0] >> cards2[0][1] >> cards2[0][2] >> cards2[0][3] >>
        cards2[1][0] >> cards2[1][1] >> cards2[1][2] >> cards2[1][3] >>
        cards2[2][0] >> cards2[2][1] >> cards2[2][2] >> cards2[2][3] >>
        cards2[3][0] >> cards2[3][1] >> cards2[3][2] >> cards2[3][3];
    std::vector<int> results;
    for (int k=0; k<4; k++)
      for (int j=0; j<4; j++)
        if (cards1[ans1 - 1][k] == cards2[ans2-1][j])
          results.push_back(cards1[ans1-1][k]);
    g << "Case #" << (i+1) << ": ";
    if (results.size() == 1) {
     g << results[0] << std::endl;
    }
    if (results.size() > 1) {
      g << "Bad magician!" <<std::endl;
    }
    if (results.size() == 0)  {
      g << "Volunteer cheated!" <<std::endl;
    }

  }
  return 0;
}