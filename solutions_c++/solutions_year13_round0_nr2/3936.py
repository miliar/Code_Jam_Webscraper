//
//  land.c
//  qu
//
//  Created by Julian Wu on 4/13/13.
//  Copyright (c) 2013 Julian Wu. All rights reserved.
//

#include <stdio.h>

int getval(int i, int j, int* land, int col){
  return land[i*col + j];
}

bool isSqrWorks(int i, int j, int col, int row ,int *land) {
  bool works = true;
  for (int m = 0; m < col; ++m) {
    if (getval(i, m, land, col) > getval(i, j, land, col)){
      //failed in col
      works = false;
      break;
    }
  }
  if (!works) {
    works = true;
    for (int m = 0; m < row; ++m) {
      int test= getval(m, j, land, col);
      if (getval(m, j, land, col) > getval(i, j, land, col)){
        //failed in col
        works = false;
        break;
      }
    }
  }
  return works;
}

int getLargest(int row, int col, int*land) {
  int highest = 0;
  for (int i = 0; i < row; ++i) {
    for (int j = 0; j < col; ++j) {
      if (getval(i, j, land, col) > highest) {
        highest = getval(i, j, land, col);
      }
    }
  }
  return highest;
}

bool TestLand(int row, int col, int* land) {
  int highest = getLargest(row, col, land);
  for (int i = 0; i < row; ++i) {
    for (int j = 0; j < col; ++j) {
      int aij = getval(i, j, land, col);
      if (aij < highest) {
        if (!isSqrWorks(i, j, col, row, land)){
          return false;
        }
      }
    }
  }
  return true;
}

void printLand(int col, int row, int* land){
  printf("\nA land=======\n");
  for (int i = 0; i < row; ++i) {
    for (int j = 0; j < col; ++j) {
      printf("%d ", getval(i, j, land, col));
    }
    printf("\n");
  }
//  for (int i = 0; i < row * col; ++i) {
//    printf("%d ", land[i]);
//  }
  printf("----------\n");
}
int main(){
  int cases = 0;
  scanf("%d", &cases);
  getchar();
  for (int i = 0; i < cases; ++i) {
    int col, row;
    scanf("%d %d", &row, &col);
    int * land = new int[row * col];
    for (int n = 0; n < row; ++n) {
      for (int m = 0; m < col; ++m) {
        scanf("%d", &land[n*col + m]);
//        printf("Read: %d\n", land[n*row + m]);
      }
      
    }
    printf("Case #%d: %s\n", i+1, TestLand(row, col, land)? "YES" : "NO" );
    
//    printLand(col, row, land);
    delete[] land;
  }

}