
#include <iostream>
#include <vector>
#include <algorithm>


using namespace std;

void printResult(int test, int result) {
      cout << "Case #" << test << ": " << result << '\n';
}

int addOrRemove(int* pme, int* moles, int molesS, int i) {
  int toRemove = molesS - i;
  
  int me = *pme;

  int toAdd = 0;
  while(true) {
    toAdd++;
    
    if(me - 1 == 0)
      break;

    me += me - 1;
    
    if(me > moles[i]) {
      me += moles[i];
      break;
    }
  }

  if(toRemove <= toAdd) {
    //printf("remove of %d, for me: %d\n", toRemove, *pme); 
    return toRemove * -1;
  }
  else {
  //printf("add of %d, for me %d, new me: %d\n", toAdd, *pme, me);
    *pme = me;
    return toAdd;
  }
}


void printT(int* tab, int size) {
   for(int i = 0; i < size; ++i) {
      printf(" %d ", tab[i]);
   }
   cout << '\n';
}
void makeTest(int test) {
  int me, their;

  cin >> me >> their;
  int* moles = (int*)malloc(sizeof(int)*their);
  for(int i = 0; i < their; ++i) {
    cin >> moles[i];
  }
  sort(moles, moles + their);

  
  int moves = 0;
  int tmp = 0;
  for(int i = 0; i < their; ++i) {
    //cout << "next: " << i << " me: " << me << " mole: " << moles[i] << '\n';
    if(moles[i] < me) {
      me += moles[i];
    }
    else { 
      tmp = addOrRemove(&me, moles, their, i);
      if(tmp < 0) {
        moves += abs(tmp);
        break;
      } else {
        moves += tmp;
      }
    }
  }
  
  free(moles);
  printResult(test, moves);
}

int main(int argc, char* argv[]) {

  ios::sync_with_stdio(false);

  int number_of_tests;
  cin >> number_of_tests;

  for(int i = 1; i <= number_of_tests; ++i) {
    makeTest(i);
  }

  return 0;
}