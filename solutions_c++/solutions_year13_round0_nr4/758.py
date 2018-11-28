//------------------------------------------------------------------------------
// Copyright (c) 2013 Mineyuki Iwasaki. All rights reserved.
//------------------------------------------------------------------------------
#include <cstdio>
#include <cstdlib>
#include <algorithm>
//#define LOG(f,...) fprintf(stderr, f, __VA_ARGS__)
#define LOG(f,...)
using namespace std;

int KEY_NUMBER, CHEST_NUMBER;
int CHEST_KEY_NUMBER[201];
int CHEST_KEY_LIST[201][201];
int ORDER[201];

struct State {
  unsigned char key_list[201];
  unsigned char chest_lock[201];
};

void PrintState(State *state) {
  LOG("Key(");
  for (int i = 0; i != 201; ++i) {
    if (state->key_list[i])
      LOG("%d*%d,", i, state->key_list[i]);
  }
  LOG(")\n");

  for (int i = 0; i != CHEST_NUMBER; ++i) {
    LOG("Chest[%d]%d (", i, state->chest_lock[i]);
    for (int j = 0; j != CHEST_KEY_NUMBER[i]; ++j) {
      LOG("%d,", CHEST_KEY_LIST[i][j]);
    }
    LOG(")\n");
  }
}

bool IsImpossible(State *state, unsigned char key) {
  bool exist = false;
  //  LOG("Imp %d", key);
  //  PrintState(state);
  for (int i = 0; i != CHEST_NUMBER; ++i) {
    //    LOG("CHECK %d/%d\n", state->chest_lock[i], key);
    if (state->chest_lock[i] == key) {
      exist = true;
      for (int j = 0; j != CHEST_NUMBER; ++j) {
        if (i != j) {
          for (int k = 0; k != CHEST_KEY_NUMBER[j]; ++k) {
            if (CHEST_KEY_LIST[j][k] == key) {
              return false;
            }
          }
        }
      }
    }
  }
  if (exist) {
    return true;
  }
  return false;
}

bool OpenChest(State* state_, int chest, int count) {
  LOG("count: %d, chest =%d\n", count, chest);
  PrintState(state_);

  // Open
  State state = *state_;
  unsigned char lock = state.chest_lock[chest];
  if ( lock != 0 && state.key_list[lock] > 0) {
    state.chest_lock[chest] = 0;
    state.key_list[lock]--;
    // Get keys.
    for (int i = 0; i != CHEST_KEY_NUMBER[chest]; ++i) {
      state.key_list[CHEST_KEY_LIST[chest][i]]++;
    }

    // Recursive
    bool end = true;
    for (int i = 0; i != CHEST_NUMBER; ++i) {
      if (state.chest_lock[i] > 0) {
        end = false;
      }
    }
    if (end) {
      LOG("CLEAR: %d, %d\n", chest, count);
      ORDER[count] = chest;
      ORDER[count+1] = -1;
      return true;
    } else {
      if (state.key_list[lock] == 0 && IsImpossible(&state, lock)) {
        LOG("DEADEND\n");
        return false;
      }

      for (int i = 0; i != CHEST_NUMBER; ++i) {
        if (state.chest_lock[i]> 0 && state.key_list[state.chest_lock[i]] > 0) {
          bool result = OpenChest(&state, i, count+1);
          if (result) {
            LOG("RETURN: %d, %d\n", chest, count);
            ORDER[count] = chest;
            return true;
          }
        }
      }
    }
  }
  return false;
}

int main() {
  int T;
  scanf("%d", &T);
  // Loop
  for (int t = 0; t != T; ++t) {
    int result = 0;
    // Input size.
    scanf("%d ", &KEY_NUMBER); // Key num
    scanf("%d", &CHEST_NUMBER); // Chest num
    LOG("---------------------------------%d, CHEST=%d --------------\n", t, CHEST_NUMBER);

    State initial;
    for (int i = 0; i != 201; ++i) {
      initial.key_list[i] = 0;
      initial.chest_lock[i] = 0;
      CHEST_KEY_NUMBER[i] = 0;
      for (int j = 0; j != 201; ++j) {
        CHEST_KEY_LIST[j][i] = 0;
      }
      ORDER[i] = -1;
    }

    for (int i = 0; i != KEY_NUMBER; ++i) {
      int a;
      scanf("%d", &a);
      initial.key_list[a]++;
    }
    for (int i = 0; i != CHEST_NUMBER; ++i) {
      scanf("%d", &initial.chest_lock[i]);
      scanf("%d", &CHEST_KEY_NUMBER[i]);
      for (int j = 0; j != CHEST_KEY_NUMBER[i]; ++j) {
        scanf("%d", &CHEST_KEY_LIST[i][j]);
      }
    }

    // Pre-test
    bool impossible = false;
    int total_exist_key[201];
    int total_need_key[201];
    for (int i = 0; i != 201; ++i) {
      total_exist_key[i] = 0;
      total_need_key[i] = 0;
    }
    for (int i = 0; i != CHEST_NUMBER; ++i) {
      total_need_key[initial.chest_lock[i]]++;
      for (int j = 0; j != CHEST_KEY_NUMBER[i]; ++j) {
        total_exist_key[CHEST_KEY_LIST[i][j]]++;
      }
    }
    for (int i = 0; i != 201; ++i) {
      total_exist_key[i] += initial.key_list[i];
      if (total_exist_key[i] || total_need_key[i]) {
        LOG("Key[%d] Lock/Exist %d/%d\n", i, total_need_key[i], total_exist_key[i]);
      }
      if (total_exist_key[i] < total_need_key[i]) {
        impossible = true;
      }
    }
    if (impossible) {
        printf("Case #%d: IMPOSSIBLE\n", t+1);
    } else {
      // Test.
      for (int i = 0; i != CHEST_NUMBER; ++i) {
        result = OpenChest(&initial, i, 0);
        if (result) {
          break;
        }
      }

      // Result.
      if (result) {
        printf("Case #%d:", t+1);
        for (int i=0; ORDER[i] != -1; ++i)
          printf(" %d", ORDER[i]+1);
        printf("\n");
      } else {
        printf("Case #%d: IMPOSSIBLE\n", t+1);
      }
    }
  }
  return 0;
}
