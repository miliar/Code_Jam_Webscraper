#include <iostream>

#include <fstream>

#include <string>

#include <Math.h>

using namespace std;

void shiftRight(int* arr, int low, int high)
{
    int root = low;
    while ((root*2)+1 <= high)
    {
        int leftChild = (root * 2) + 1;
        int rightChild = leftChild + 1;
        int swapIdx = root;
        /*Check if root is less than left child*/
        if (arr[swapIdx] < arr[leftChild])
        {
            swapIdx = leftChild;
        }
        /*If right child exists check if it is less than current root*/
        if ((rightChild <= high) && (arr[swapIdx] < arr[rightChild]))
        {
            swapIdx = rightChild;
        }
        /*Make the biggest element of root, left and right child the root*/
        if (swapIdx != root)
        {
            int tmp = arr[root];
            arr[root] = arr[swapIdx];
            arr[swapIdx] = tmp;
            /*Keep shifting right and ensure that swapIdx satisfies
            heap property aka left and right child of it is smaller than
            itself*/
            root = swapIdx;
        }
        else
        {
            break;
        }
    }
    return;
}
void heapify(int* arr, int low, int high)
{
    /*Start with middle element. Middle element is chosen in
    such a way that the last element of array is either its
    left child or right child*/
    int midIdx = (high - low -1)/2;
    while (midIdx >= 0)
    {
        shiftRight(arr, midIdx, high);
        --midIdx;
    }
    return;
}

void heapSort(int* arr, int size)
{
    /*This will put max element in the index 0*/
    heapify(arr, 0, size-1);
    int high = size - 1;
    while (high > 0)
    {
        /*Swap max element with high index in the array*/
        int tmp = arr[high];
        arr[high] = arr[0];
        arr[0] = tmp;
        --high;
        /*Ensure heap property on remaining elements*/
        shiftRight(arr, 0, high);
    }
    return;
}

int main(int argc, char *argv[])
{
  ifstream inputFile;
  inputFile.open(argv[1]);

  int numOfInput;

  inputFile >> numOfInput;

  for(int inputIndex=0; inputIndex<numOfInput; inputIndex++) {

    int startedMoteSize;
    inputFile >> startedMoteSize;

    int numOfMotes;
    inputFile >> numOfMotes;

    int motes[100];

    for(int moteIndex=0; moteIndex<numOfMotes; moteIndex++) {
      inputFile >> motes[moteIndex];
    }

    heapSort(motes, numOfMotes);

    int numOfSkipMote = 0;
    int numOfAddMote = 0;

    int currentMoteSize = startedMoteSize;

    for(int moteIndex=0; moteIndex<numOfMotes; moteIndex++) {
      int victimMoteSize = motes[moteIndex];

      if(currentMoteSize <= victimMoteSize) {
        //Cant Eat

        int numToTryAdd = 1;
        bool possibleToAdd = false;
        int tmpMoteSize = currentMoteSize;

        while(numToTryAdd<numOfMotes-moteIndex && !possibleToAdd) {

          if(tmpMoteSize + (tmpMoteSize-1) > victimMoteSize) {
            currentMoteSize = tmpMoteSize + (tmpMoteSize-1);
            currentMoteSize += victimMoteSize;
            numOfAddMote += numToTryAdd;
            possibleToAdd = true;
          } else {
            tmpMoteSize += (tmpMoteSize-1);
          }
          numToTryAdd++;
            
        }

        if(!possibleToAdd) {
          //Have to remove
          numOfSkipMote++;
        }

      } else {
        //Can Eat

        currentMoteSize += victimMoteSize;
      }
    }

    cout << "Case #" << inputIndex+1 << ": " << (numOfAddMote+numOfSkipMote) << endl;

  }

  return 0;
} 
