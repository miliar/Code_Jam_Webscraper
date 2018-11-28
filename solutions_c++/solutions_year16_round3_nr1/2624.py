#include <iostream>

using namespace::std;

void get_next_candidate(int senates[], int N, int& candidate_h, int& candidate_l) {
  int max_value = -1;
  int prev_value = -1;
  int prev_prev_value = -1;
  int max_i = -1;
  int prev_i = -1;
  int prev_prev_i = -1;

  for(int i=0; i<N; i++) {
    if(senates[i] >= max_value) {
        max_value = senates[i];
        max_i = i;
    }
  }
  for(int i=0; i<N; i++) {
    if(senates[i] >= prev_value && i != max_i) {
        prev_value = senates[i];
        prev_i = i;
    }
  }
  for(int i=0; i<N; i++) {
    if(senates[i] >= prev_prev_value && i != max_i && i != prev_i) {
        prev_prev_value = senates[i];
        prev_prev_i = i;
    }
  }

  //cout << max_i << prev_i << endl;
  if(max_i > -1 && prev_i > -1 && prev_prev_i > -1) {
      if(senates[max_i] > 0 && senates[prev_i] > 0 && senates[prev_prev_i] > 0) {
        if(senates[max_i] == 1 && senates[prev_i] == 1 && senates[prev_prev_i] == 1) {  //cannot remove 2 at a time
          candidate_h = max_i;
          candidate_l = -1;
        } else if(senates[max_i]-senates[prev_i] > 2) {
          candidate_h = max_i;
          candidate_l = max_i;
        } else {
          candidate_h = max_i;
          candidate_l = prev_i;
        }
      } else if(senates[max_i] > 0 && senates[prev_i] > 0) {
        if(senates[max_i] == 1 && senates[prev_i] == 1) {
          candidate_h = max_i;
          candidate_l = prev_i;
        } else if(senates[max_i]-senates[prev_i] > 2) {
          candidate_h = max_i;
          candidate_l = max_i;
        } else {
          candidate_h = max_i;
          candidate_l = prev_i;
        }
      } else {
        candidate_h = -1;
        candidate_l = -1;
      }
  } else if(max_i > -1 && prev_i > -1) {
    if(senates[max_i] > 0 && senates[prev_i] > 0) {
      if(senates[max_i] == 1 && senates[prev_i] == 1) {
        candidate_h = max_i;
        candidate_l = prev_i;
      } else if(senates[max_i]-senates[prev_i] > 2 && senates[prev_i] > 0) {
        candidate_h = max_i;
        candidate_l = max_i;
      } else {
        candidate_h = max_i;
        candidate_l = prev_i;
      }
    }
    else {
      candidate_h = -1;
      candidate_l = -1;
    }
  } else {
    candidate_h = -1;
    candidate_l = -1;
  }
}

char senate_id[] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' };
#define MAX_SENATORS 1001

void evacuate_senator(int t) {
  int senator_1 = -1;
  int senator_2 = -1;
  int N;
  int senators[MAX_SENATORS] = {0};

  cin >> N;
  for (int i=0; i<N; i++) { //read all the senators
    cin >> senators[i];
  }
  cout << "Case #" << t << ": ";
  do {
    get_next_candidate(senators, N, senator_1, senator_2);
    if(senator_1 > -1) {
      cout << senate_id[senator_1];
      senators[senator_1]--;
    }
    if(senator_2 > -1) {
      cout << senate_id[senator_2];
      senators[senator_2]--;
    }
    cout << " ";
  } while (senator_1 > -1); //godspeed
  cout << endl;
}

int main(void) {
  int T = 0;
  cin >> T;
  for(int i=1; i<=T; i++) {
    evacuate_senator(i);
  }
  return 0;
}
