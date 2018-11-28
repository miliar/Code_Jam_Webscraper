#include<stdio.h>
#include<vector>
#include<string>
#include<stdlib.h>
#include<queue>
#include<math.h>
using namespace std;


FILE *pFile = freopen("input.txt", "r",stdin);
FILE *oFile = freopen("output.txt", "w",stdout);

bool checksosu(vector<unsigned long long> arr) {
	bool flag = true;

	for (int k = 0; k < arr.size(); k++) {
		int check = 0;
		for (unsigned long long i = 2; i <= sqrt(arr[k]); i++) {
			if (arr[k] % i == 0) {
				check = 1;
				break;
			}
		}
		if (check == 0) {
			flag = false;
			break;
		}
	}

	return flag;
}

vector<unsigned long long> process(vector<int> input) {

	vector<unsigned long long> result;

	for (int i = 2; i <= 10; i++) {
		unsigned long long temp = 0;
		unsigned long long rate = i;
		for (int j = input.size() - 1; j >= 0; j--) {

			temp += (input[j])*rate;

			rate *= i;
		}
		temp = temp / i;
		result.push_back(temp);
	}
	return result;
}
int cnt = 0;


void print(vector<unsigned long long> arr) {
	for (int k = 0; k < arr.size(); k++) {
		for (unsigned long long i = 2; i <= sqrt(arr[k]); i++) {
			if (arr[k] % i == 0) {
				printf(" %lld", i);
				break;
			}
		}
	}
}

void recur(int index, vector<int> arr, int N, int J) {
	if (index == N - 1) {
		if (cnt < J) {
			vector<unsigned long long> result_arr = process(arr);
			if (checksosu(result_arr) == true) {

				for (int i = 0; i < arr.size(); i++) {
					printf("%d", arr[i]);
				}
				print(result_arr);
				printf("\n");
				cnt++;
			}
		}
		return;
	}

	recur(index + 1, arr, N, J);
	arr[index] = 0;
	recur(index + 1, arr, N, J);

}


int main() {

	int testcase;
	scanf("%d", &testcase);

	for (int temp = 1; temp <= testcase; temp++) {

		int N, J;
		scanf("%d %d", &N, &J);

		printf("Case #1:\n");

		int count = 0;

		vector<int> arr;
		for (int i = 0; i < N; i++) {
			arr.push_back(1);
		}
		//arr.resize(N);
		//arr[0] = arr[N - 1] = 1;

		recur(1, arr, N, J);
	}

	return 0;
}