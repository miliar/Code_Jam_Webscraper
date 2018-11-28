#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;


void mysort(double R[100], double C[100], int N) {
	for (int i = 0; i < N - 1; i++) {
		for (int j = 0; j < N - i - 1; j++) {
			if (C[j] > C[j + 1]) {
				double temp = C[j];
				C[j] = C[j + 1];
				C[j + 1] = temp;
				temp = R[j];
				R[j] = R[j + 1];
				R[j + 1] = temp;
			}
		}
	}
}



int main() {
	ifstream fin("E:\\B-small-attempt0.in");
	//ifstream fin("E:\\temp.txt");
	ofstream fout("E:\\B-small.out");
	int T;
	fin >> T;
	for (int i = 1; i <= T; i++) {
		int N;
		double V, X;
		double R[100];
		double C[100];
		fin >> N >> V >> X;
		for (int j = 0; j < N; j++) {
			fin >> R[j] >> C[j];
		}
		mysort(R, C, N);
		double high_area = 0.0;
		double low_area = 0.0;
		double correct_rate = 0.0;
		double low_rate = 0.0;
		double high_rate = 0.0;
		for (int j = 0; j < N; j++) {
			if (C[j] > X) {
				high_area = high_area + (C[j] - X) * R[j];
				high_rate = high_rate + R[j];
			}
			else {
				if (X > C[j]) {
					low_area = low_area + (X - C[j]) * R[j];
					low_rate = low_rate + R[j];
				}
				else {
					correct_rate = correct_rate + R[j];
				}
			}
		}
		if (high_area < 1e-12 || low_area < 1e-12) {
			if (correct_rate < 1e-12) {
				fout << "Case #" << i << ": " << "IMPOSSIBLE" << endl;
			}
			else {
				fout << "Case #" << i << ": " << fixed << setprecision(12) << V / correct_rate << endl;
			}
			continue;
		}

		if (low_area < high_area) {
			double difference = high_area - low_area;
			int index = N - 1;
			while (true) {
				if (index < 0) {
					break;
				}
				if (R[index] * (C[index] - X) >= difference) {
					double substract = difference / (C[index] - X);
					high_rate = high_rate - substract;
					break;
				}
				else {
					high_rate = high_rate - R[index];
					high_area = high_area - R[index] * (C[index] - X);
					difference = high_area - low_area;
					index--;
				}
			}
		}
		else {
			double difference = low_area - high_area;
			int index = 0;
			while (true) {
				if (index >= N) {
					break;
				}
				if (R[index] * (X - C[index]) >= difference) {
					double substract = difference / (X - C[index]);
					low_rate = low_rate - substract;
					break;
				}
				else {
					low_rate = low_rate - R[index];
					low_area = low_area - R[index] * (X - C[index]);
					difference = low_area - high_area;
					index++;
				}
			}
		}
		fout << "Case #" << i << ": " << fixed << setprecision(12) << V / (low_rate + high_rate + correct_rate) << endl;
	}
	return 0;
}
