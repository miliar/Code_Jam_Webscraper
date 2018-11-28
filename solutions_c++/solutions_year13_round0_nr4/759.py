#include<iostream>
#include<cstdio>
#include<set>

using namespace std;

int nChests;
const int maxKey = 400;
const int maxChests = 200;

int sol[maxChests];
int solIndex;
bool chestUsed[maxChests+1];
int keyAvailable[maxKey+1];
int kN[maxChests+1];
int keys[maxChests+1][maxChests+1];
int cRem;
int kInHand;
int kNeeded[maxKey+1];
int kAv[maxKey+1];

bool solve() {

  /*

  printf ("Solve state (%i chests remaining):\n", cRem);
  printf("\tKeys in hand: \n\t\t");
  for (int i = 1; i <= maxKey; i++)
  {
    if (keyAvailable[i] > 0) {
      printf("%i: %i  ", i, keyAvailable[i]);
    }
  }
  printf("\n");

  printf ("\tUsed chests:\n\t\t");
  for (int i = 0; i < solIndex; i++)
  {
    printf("%i ", sol[i]);
  }
  printf("\n");
  */

  bool finished = true;
  bool optFound = false;
  for (int i = 1; i <= nChests; i++) 
  {
    if (optFound) break;

    if (chestUsed[i])
      continue;

    //try to use it...
    if (keyAvailable[kN[i]] > 0) {
      keyAvailable[kN[i]] -= 1;
      chestUsed[i] = true;
      kInHand -= 1;
      kInHand += keys[i][0];
      cRem -= 1;
      kNeeded[kN[i]] -= 1;

      sol[solIndex] = i;
      solIndex++;

      if (cRem == 0) {
        return true;
      }


      for (int j = 0; j < keys[i][0]; j++) {
        keyAvailable[keys[i][j+1]] += 1;
        if (keys[i][j+1] == kN[i]) {
          //printf("%i is the optimal chest to take\n", i);
          optFound = true;
        }
      }

      //we have all needed keys in the hand
      if (keyAvailable[kN[i]] >= kNeeded[kN[i]]) {
        //printf("%i is the optimal chest to take\n", i);
        optFound = true;
      }

      //printf("\tUsing chest %i\n", i);

      if (kInHand > 0 && solve()) {
        return true;
      }

      //undo changes
      for (int j = 0; j < keys[i][0]; j++)
        keyAvailable[keys[i][j+1]] -= 1;
      chestUsed[i] = false;
      keyAvailable[kN[i]] += 1;
      cRem += 1;
      kInHand += 1;
      kInHand -= keys[i][0];
      kNeeded[kN[i]] += 1;
      solIndex--;

      //We can't be finished
      finished = false;

    } else {
      finished = false;
    }
  }

  return finished;
}

int main() {
  int probs;
  cin >> probs;

  for (int p = 1; p<= probs; p++) {
    int k,n;
    cin >> k >> n;
    nChests = n;

    //printf("%i %i\n", k, n);

    cRem = n;
    kInHand = k;
    solIndex = 0;
    for (int i = 0; i < maxChests; i++) sol[i] = -1;

    for (int i = 0; i <= maxKey; i++) keyAvailable[i] = 0;

    chestUsed[0] = true;
    for (int i = 1; i <= n; i++) chestUsed[i] = false;


    for (int i = 0; i<= maxKey; i++) {
      kNeeded[i] = 0;
      kAv[i] = 0;
    }

    int tmp;
    for (int i = 0; i < k; i++) {
      cin >> tmp;
      keyAvailable[tmp] += 1;
      kAv[tmp] += 1;
    }

    for (int i = 0; i < n; i++) {
      cin >> kN[i+1];
      kNeeded[kN[i+1]] += 1;
      cin >> keys[i+1][0];
      for (int j = 0; j < keys[i+1][0]; j++) {
        cin >> tmp;
        keys[i+1][j+1] = tmp;
        kAv[tmp] += 1;
      }

      //printf("Chest %i has %i keys\n", i+1, keys[i+1][0]);
    }

    bool imp = false;
    for (int i = 1; i<= maxKey; i++) {
      if (kNeeded[i] > kAv[i])
      {
        imp = true;
        break;
      }
    }

    printf("Case #%i:", p);

    if (imp || !solve())
      printf(" IMPOSSIBLE");
    else {
      for (int i = 0; i < n; i++)
        printf(" %i", sol[i]);
    }
    printf("\n");
  }
  return 0;
}
