#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
using namespace std;



int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int CaseNum;
	cin >> CaseNum;
	for (int Case = 1; Case <= CaseNum; Case++)
	{
		cout << "Case #" << Case << ": ";
		fprintf(stderr, "Case #%d\n", Case);

		long long A, B, K;
		cin >> A >> B >> K;

		long long answer = 0;

		for (int a = 0; a < A; a++){
			for (int b = 0; b < B; b++){
				if ((a&b) < K) answer++;
			}
		}

		cout << answer << endl;
	}
}