// Google Code Jam, Qual Round, Question D

#include <iostream>
#include <stdio.h>
#include <time.h>
#include <stdlib.h>

using namespace std;

struct block {
  bool isNancy;
  double weight;
};

void quicksort(struct block *blockArray, int len);
void partition(struct block *blockArray, int low, int high);
void swap(struct block *blockArray, int a, int b);

int main() {
  int cases;
  cin >> cases;
  for (int case_num = 1; case_num < cases + 1; case_num++) {
    int numBlocks;
    struct block newBlock;
    cin >> numBlocks;
    struct block blockArray[numBlocks * 2];
    for (int isNancy = 0; isNancy < 2; isNancy++) {
      for (int i = 0; i < numBlocks; i++) {
        block newBlock;
        newBlock.isNancy = isNancy ? false : true;
        cin >> newBlock.weight;
        // store it there
        blockArray[isNancy * numBlocks + i] = newBlock;
      }
    }
    quicksort(blockArray, numBlocks * 2);
    int enemyCheatPoints = 0;
    int enemyOptimalPoints = 0;
    int ownBlockCount = 0;
    for (int i = 0; i < numBlocks * 2; i++) {
      block selectedBlock = blockArray[i];
      if (selectedBlock.isNancy) {
        ownBlockCount++;
      } else {
        if (ownBlockCount > 0) {
          ownBlockCount--;
          enemyOptimalPoints++;
        }
      }
    }
    ownBlockCount = 0;
    for (int i = numBlocks * 2 - 1; i > -1; i--) {
      block selectedBlock = blockArray[i];
      if (selectedBlock.isNancy) {
        ownBlockCount++;
      } else {
        if (ownBlockCount == 0)
          enemyCheatPoints++;
        else
          ownBlockCount--;
      }

    }
    printf("Case #%d: %d %d\n", case_num, numBlocks - enemyCheatPoints, numBlocks - enemyOptimalPoints);
  }
}

void quicksort(struct block *blockArray, int len) {
  if (len > 1)
    partition(blockArray, 0, len - 1);
}

void partition(struct block *blockArray, int low, int high) {
  int left, right;
  double pivot = blockArray[low].weight;
  for (int i=low; i < high; i++) {
  }
  // if there are 0-1 elements, just return
  if (high - low < 1) return;
  // if there are 2 only, then check if they need to be swapped, and then
  // return
  else if (high - low == 1) {
    if (blockArray[low].weight > blockArray[high].weight)
      swap(blockArray, low, high);
    return;
  }
  // Otherwise, we can do the quicksort routine
  left = low + 1;
  right = high;
  while (left < right) {
    // keep going as long as the left value is less than the pivot
    // Also make sure it doesn't exceed the right bound
    while (blockArray[left].weight < pivot && left < high) {
      left++;
    }
    // move the right down until it is less than the pivot and make sure
    // it doesn't get to the pivot
    while (blockArray[right].weight > pivot && right > low) {
      right--;
    }
    if (left < right) {
      swap(blockArray, left, right);
    }
  }
  swap(blockArray, low, right);
  // if they have at least 1 distance apart
  if ((right - 1) - low > 0) {
    partition(blockArray, low, right - 1);
  }
  if (high - (right + 1) > 0) {
    partition(blockArray, right + 1, high);
  }
}

void swap(struct block *blockArray, int a, int b) {
  struct block tempStore = blockArray[a];
  blockArray[a] = blockArray[b];
  blockArray[b] = tempStore;
}
