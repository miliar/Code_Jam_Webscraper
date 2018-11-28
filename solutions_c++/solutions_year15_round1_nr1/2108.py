#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <list>
#include <cstdlib>


int T;
int m[1001];
int N;
int x;
int y;

int compute();

int main(int argc, const char* argv[]) {
  std::cin >> T;
  for (int i = 1; i <= T; i++) {
		 std::cin >> N;
		 for (int j = 0; j < N; j++)
			 std::cin >> m[j];
     int r = compute();
     std::cout << "Case #" << i << ": " << x << " " << y << std::endl;
  }
  return 0;
}

int compute() {
	x = 0;
	y = 0;
	for (int i = 0; i < N - 1; i++)
		if (m[i] > m[i+1])
			x += m[i] - m[i+1];

	y = 0;
	float rate = 0;
	for (int i = 0; i < N - 1; i++)
		if (m[i] > m[i+1]) {
			float r = (float) (m[i] - m[i+1]);
			float current_rate = r / 10;
			rate = std::max(rate, current_rate);
		}

	for (int i = 0; i < N - 1; i++)
		y += std::min((int)(rate * 10), m[i]);
	return 0;
}
