#include <unordered_map>
#include <list>
#include <algorithm>
#include <memory>
#include <vector>
#include <queue>

#include <stdio.h>
#include <assert.h>
#include <stdlib.h>

using namespace std;

int main() {
  FILE* read = fopen("./test.in", "r");
  FILE* write = fopen("./ans.out", "w");
  int case_number;
  fscanf(read, "%d", &case_number);
  for (int case_index = 1; case_index <= case_number; case_index++) {
    int D;
    fscanf(read, "%d", &D);

    int P[1024], candidate_answer = 0;
    for (int i = 0; i < D; i++) {
      fscanf(read, "%d", &P[i]);
      candidate_answer = max(candidate_answer, P[i]);
    }

    int answer = candidate_answer;

    for (int eating_time = 1; eating_time <= answer; eating_time++) {
      int split_time = 0;
      for(int i = 0; i < D; i++){
        split_time += (P[i] + eating_time - 1) / eating_time - 1;
      }
      answer = min(answer, split_time + eating_time);
    }

    fprintf(write, "Case #%d: %d\n", case_index, answer);
  }

  fclose(read);
  fclose(write);
  return 0;
}

/**
11 1
*/

