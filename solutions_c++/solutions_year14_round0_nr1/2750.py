/*
 * main.cpp
 *
 *  Created on: Apr 12, 2014
 *      Author: Administrator
 */


#include <iostream>
#include <fstream>
#include <string>
#include <cstdio>

int main (int argc, char** argv)
{
  std::ifstream ifs(argv[1]);
  if (!ifs) {
    std::cout << "Cannot open" << argv[1] << std::endl;
    return -1;
  }

  int num_round;
  ifs >> num_round;

  for (int round = 1; round <= num_round; ++round) {
    int pos1;
    ifs >> pos1;

    int table1[4][4];
    for (int x = 0; x < 4; ++x) {
      for (int y = 0; y < 4; ++y) {
	ifs >> table1[x][y];
      }
    }

    int pos2;
    ifs >> pos2;
    int table2[4][4];
    for (int x = 0; x < 4; ++x) {
      for (int y = 0; y < 4; ++y) {
	ifs >> table2[x][y];
      }
    }

    int card = 0;
    int num = 0;
    for (int x = 0; x < 4; ++x){
      for (int y = 0; y < 4; ++y){
	if (table1[pos1-1][x] == table2[pos2-1][y]) {
	  card = table1[pos1-1][x];
	  ++num;
	}
      }
    }

    if (num == 1) {
      printf("Case #%d: %d\n", round, card);
    } else if (num > 1) {
      printf("Case #%d: Bad magician!\n", round);
    } else if (num == 0) {
      printf("Case #%d: Volunteer cheated!\n", round);
    }
   
  }
  ifs.close();
  return 0;
}
