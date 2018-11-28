#include <cmath>
#include <cstdio>
#include <vector>

#define MAX_LENGTH 103

using namespace std;

char string[MAX_LENGTH];

int main(int argc, char *argv[]) {
  int t;
  scanf("%d", &t);
  for (int i = 1; i <= t; i++) {
    printf("Case #%d: ", i);
    size_t n;
    scanf("%lud", &n);
    getchar();
    vector<pair<char, int> > strings[n];
    for (size_t j = 0; j < n; j++) {
      fgets(string, MAX_LENGTH, stdin);
      char prev = '\0';
      int count = 0;
      for (int k = 0; k < MAX_LENGTH && 
	     (string[k] != '\n' && string[k] != '\0' && string[k] != '\t' && string[k] != ' '); k++) {
	char c = string[k];
	if (c != prev && prev != '\0') {
	  strings[j].push_back(pair<char, int>(prev, count));
	  //printf("%c%d", prev, count);
	  count = 0;
	}
	count++;
	prev = c;
      }
      strings[j].push_back(pair<char,int>(prev, count));
      //printf("%c%d\n", prev, count);
    }
    bool felga = false;
    size_t test = strings[0].size();
    for (size_t k = 1; k < n && !felga; k++) {
      if (test != strings[k].size()) {
	printf("Fegla Won\n");
	felga = true;
      }
      for(size_t x = 0; x < test && !felga; x++) {
	if (strings[0][x].first != strings[k][x].first) {
	  printf("Fegla Won\n");
	  felga = true;
	}
      }
    }

    if (felga) {
      continue;
    }
 
    int result = 0;
    /*
    for (size_t k = 0; k < test; k++) {
      double sum = 0;
      for (size_t j = 0; j < n; j++) {
	sum += strings[j][k].second;
      }
      double avg = round(sum / (double) n);
      int closest = strings[0][k].second;
      for (size_t j = 1; j < n; j++) {
	if (abs(strings[j][k].second - avg) < abs(closest - avg)) {
	  closest = strings[j][k].second;
	} 
      }
      for (size_t j = 0; j < n; j++) {
	result += abs(strings[j][k].second - closest);
      }
    }
    */
    for (size_t k = 0; k < test; k++) {
      result += abs(strings[0][k].second - strings[1][k].second);
      //printf("%d <---> %d\n", strings[0][k].second, strings[1][k].second);
    }
    printf("%d\n", result);
  }
  return 0;
}
