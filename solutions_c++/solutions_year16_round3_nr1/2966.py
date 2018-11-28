#include<iostream>
#include<fstream>
#include<string>
#include<cstdio>
#include<math.h>
using namespace std;

int main(int argc, char** argv) {
	int T;
	int test_case;
	freopen("A-small-attempt1.in", "r", stdin);

	scanf("%d", &T);
	for (test_case = 1; test_case <= T; ++test_case) {
		int N;
		cin >> N;
		char A = 'A';
		int *P = new int[N];
		int index;
		int sum = 0;
		for (int i = 0; i < N; i++) { cin >> P[i]; sum += P[i]; }
		
		cout << "Case #" << test_case << ": ";
		int sumcopy = sum;
		for (int i = 0; i < sum; i++) {
			int max = P[0];
			index = 0;
			for (int j = 1; j < N; j++)
			{
				if (max < P[j])
				{
					max = P[j];
					index = j;
				}
			}
			P[index]--; 
			if (N!=2 && sumcopy == N) { 
				printf("%c ", A+index); 
			}
			else {
				printf("%c", A + index);
				if ((i + 1) % 2 == 0 && sum != 2 && sum-i != 2) cout << " ";
			}
			sumcopy--;
		}
		cout << endl;
	}
}