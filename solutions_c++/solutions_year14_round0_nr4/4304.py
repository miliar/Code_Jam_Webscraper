#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

vector<double> removeFirstValue(vector<double> vector, int N) {
	for (int i = 0; i < N-1; i++) {
		vector[i] = vector[i+1];
	}
	return vector;
}

int cheatedGame1(vector<double> naomiBlocks, vector<double> kenBlocks, int N) {
	int currentSize = N;
	int naomiScore = 0;
	int kenScore = 0;
	for (int i = 0; i < N; i++) {
		double biggestNaomi = naomiBlocks[currentSize-1];
		double biggestKen = kenBlocks[currentSize-1];
		if (biggestNaomi > biggestKen) {
			naomiScore++;
		} else {
			kenScore++;
			naomiBlocks = removeFirstValue(naomiBlocks, currentSize);
		}
		currentSize--;
	}

	return naomiScore;
}

int cheatedGame2(vector<double> naomiBlocks, vector<double> kenBlocks, int N) {
	int currentMinimumKen = 0;
	int naomiScore = 0;
	int kenScore = 0;
	for (int i = 0; i < N; i++) {
		double lowestNaomi = naomiBlocks[i];
		double lowestKen = kenBlocks[currentMinimumKen];
		if (lowestNaomi > lowestKen) {
			// naomi will say her block is bigger thant ken's bigger, causing ken to launch his lowest block
			// naomi lowestBlock is smaller than ken's lowest, so she win
			naomiScore++;
			currentMinimumKen++;
		} else {
			// naomi knows she will loose , so she will remove ken's biggest block ( by not increasing his minimum)
			kenScore++;
			
		}
	}

	return naomiScore;
}

int fairGame(vector<double> naomiBlocks, vector<double> kenBlocks, int N) {
	int currentSize = N;
	int naomiScore = 0;
	int kenScore = 0;
	for (int i = 0; i < N; i++) {
		double biggestNaomi = naomiBlocks[currentSize-1];
		double biggestKen = kenBlocks[currentSize-1];
		if (biggestNaomi > biggestKen) {
			naomiScore++;
			kenBlocks = removeFirstValue(kenBlocks,currentSize);
		} else {
			kenScore++;
		}
		currentSize--;
	}

	return naomiScore;
}

int main() {
	int amount;
	scanf("%d",&amount);
	for (int x = 1; x <= amount; x++) {
		int N;
		scanf("%d",&N);
		vector<double> kenBlocks;
		vector<double> naomiBlocks;

		for (int i = 0; i < N; i++) {
			double valor;
			scanf("%lf",&valor);
			naomiBlocks.push_back(valor);
		}
		for (int i = 0; i < N; i++) {
			double valor;
			scanf("%lf",&valor);
			kenBlocks.push_back(valor);
		}

		sort(naomiBlocks.begin(), naomiBlocks.end());
		sort(kenBlocks.begin(), kenBlocks.end());

		int cheatedGameScore2 = cheatedGame2(naomiBlocks,kenBlocks,N);
		int fairGameScore = fairGame(naomiBlocks,kenBlocks,N);

		printf("Case #%d: %d %d\n",x,cheatedGameScore2,fairGameScore);

	}
	return 0;
}