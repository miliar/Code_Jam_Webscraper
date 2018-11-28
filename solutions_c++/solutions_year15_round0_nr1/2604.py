#include <iostream>
#include <algorithm>
#include <string>

int T;
int Smax;
int S[1001];

int compute();

int main(int argc, const char* argv[]) {
  std::cin >> T;
  std::string shy;
  for (int i = 1; i <= T; i++) {
		 std::cin >> Smax >> shy;
		 for (int j = 0; j <= Smax; j++){
       S[j] = shy[j] - '0';
     }
     int r = compute();
     std::cout << "Case #" << i << ": " << r << std::endl;
  }
  return 0;
}

int compute() {
	int numStandup = 0;
	int numInvited = 0;
	for (int i = 0; i <= Smax; i++) {
		if (i <= numStandup)
			numStandup += S[i];
		else {
			int invite = i - numStandup;
			numInvited += invite;
			numStandup += S[i] + invite;
	  }
  }
  return numInvited;
}

